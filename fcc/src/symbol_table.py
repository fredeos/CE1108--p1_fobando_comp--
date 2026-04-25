from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Dict, List, Any


# CONSTANTES DE MEMORIA

WORD_SIZE = 4
DATA_BASE = 0x1000
CODE_BASE = 0x0000
PARAM_REGISTER_LIMIT = 9


# DIAGNOSTICOS

@dataclass
class SemanticDiagnostic:
    line: int
    column: int
    code: str
    details: dict


# TIPOS

@dataclass
class TypeInfo:
    name: str
    is_pointer: bool = False
    array_dims: List[int] = field(default_factory=list)

    def __str__(self) -> str:
        suffix = ""
        if self.is_pointer:
            suffix += "*"
        for dim in self.array_dims:
            suffix += f"[{dim if dim > 0 else ''}]"
        return f"{self.name}{suffix}"

    @property
    def is_array(self) -> bool:
        return len(self.array_dims) > 0

    @property
    def is_void(self) -> bool:
        return self.name == "void" and not self.is_pointer and not self.is_array

    @property
    def is_bool(self) -> bool:
        return self.name == "bool" and not self.is_pointer and not self.is_array

    @property
    def is_numeric(self) -> bool:
        return self.name in {"int", "char", "float"} and not self.is_pointer and not self.is_array

    @property
    def is_integral(self) -> bool:
        return self.name in {"int", "char"} and not self.is_pointer and not self.is_array

    @property
    def has_unknown_size(self) -> bool:
        return any(dim <= 0 for dim in self.array_dims)

    def same_shape(self, other: "TypeInfo") -> bool:
        return (
            self.name == other.name
            and self.is_pointer == other.is_pointer
            and self.array_dims == other.array_dims
        )

    def base_scalar_size(self) -> int:
        if self.is_pointer:
            return WORD_SIZE

        if self.name == "int":
            return WORD_SIZE
        if self.name == "float":
            return WORD_SIZE
        if self.name == "bool":
            return WORD_SIZE
        if self.name == "char":
            return 1
        if self.name == "void":
            return 0
        if self.name == "vault":
            return WORD_SIZE

        return WORD_SIZE

    def total_size(self) -> int:
        base = self.base_scalar_size()
        if not self.array_dims:
            return base

        total_elems = 1
        for dim in self.array_dims:
            total_elems *= max(dim, 1)
        return base * total_elems

    def element_type(self) -> "TypeInfo":
        if self.is_array:
            return TypeInfo(
                name=self.name,
                is_pointer=self.is_pointer,
                array_dims=self.array_dims[1:],
            )
        if self.is_pointer:
            return TypeInfo(name=self.name)
        return self


# SIMBOLOS

@dataclass
class Symbol:
    name: str
    kind: str                # variable | function | parameter | label
    type_info: Optional[TypeInfo]
    scope_name: str
    line: int
    column: int

    # memoria
    segment: Optional[str] = None       # global | stack | param | label
    address: Optional[int] = None       # global absolute address / label address futuro
    offset: Optional[int] = None        # stack offset relativo a sp
    register: Optional[str] = None      # p0..p8 si es parametro
    size: int = 0
    alignment: int = WORD_SIZE

    # funciones
    params: List[TypeInfo] = field(default_factory=list)
    return_type: Optional[TypeInfo] = None

    # metadatos libres
    extra: Dict[str, Any] = field(default_factory=dict)


# SCOPE

@dataclass
class Scope:
    name: str
    kind: str                      # global | function | block
    parent: Optional["Scope"] = None
    symbols: Dict[str, Symbol] = field(default_factory=dict)
    children: List["Scope"] = field(default_factory=list)

    def define(self, symbol: Symbol) -> bool:
        if symbol.name in self.symbols:
            return False
        self.symbols[symbol.name] = symbol
        return True

    def resolve_local(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)


@dataclass
class FunctionFrame:
    name: str
    local_size: int = 0
    parameter_size: int = 0
    frame_size: int = 0
    max_local_offset: int = 0
    parameter_registers: List[str] = field(default_factory=list)
    stack_parameters: int = 0


# TABLA DE SIMBOLOS

class SymbolTable:
    def __init__(self):
        self.global_scope = Scope(name="global", kind="global")
        self.current_scope = self.global_scope
        self.scope_stack: List[Scope] = [self.global_scope]
        self.all_scopes: List[Scope] = [self.global_scope]

        # asignacion de memoria
        self.next_global_address = DATA_BASE
        self.next_code_address = CODE_BASE
        self.current_stack_offset = 0
        self.current_parameter_offset = 0
        self.current_function_frame: Optional[FunctionFrame] = None
        self.function_frames: Dict[str, FunctionFrame] = {}

    #  scopes

    def enter_scope(self, name: str, kind: str) -> Scope:
        new_scope = Scope(name=name, kind=kind, parent=self.current_scope)
        self.current_scope.children.append(new_scope)
        self.scope_stack.append(new_scope)
        self.all_scopes.append(new_scope)
        self.current_scope = new_scope
        return new_scope

    def exit_scope(self) -> Scope:
        if len(self.scope_stack) == 1:
            return self.current_scope

        popped = self.scope_stack.pop()
        self.current_scope = self.scope_stack[-1]
        return popped

    def reset_function_stack(self):
        self.current_stack_offset = 0
        self.current_parameter_offset = 0

    def start_function_frame(self, name: str):
        self.reset_function_stack()
        frame = FunctionFrame(name=name)
        self.function_frames[name] = frame
        self.current_function_frame = frame

    def finish_function_frame(self) -> Optional[FunctionFrame]:
        frame = self.current_function_frame
        if frame is not None:
            frame.local_size = abs(frame.max_local_offset)
            frame.frame_size = self._align(frame.local_size + frame.parameter_size, WORD_SIZE)
        self.current_function_frame = None
        return frame

    #  resolucion

    def resolve(self, name: str) -> Optional[Symbol]:
        scope = self.current_scope
        while scope is not None:
            symbol = scope.resolve_local(name)
            if symbol is not None:
                return symbol
            scope = scope.parent
        return None

    #  definicion

    def define(self, symbol: Symbol) -> bool:
        return self.current_scope.define(symbol)

    def define_global(self, symbol: Symbol) -> bool:
        return self.global_scope.define(symbol)

    #  memoria

    def _align(self, size: int, alignment: int = WORD_SIZE) -> int:
        if size <= 0:
            return 0
        return ((size + alignment - 1) // alignment) * alignment

    def allocate_global(self, size: int) -> int:
        aligned = self._align(size, WORD_SIZE)
        addr = self.next_global_address
        self.next_global_address += aligned
        return addr

    def allocate_local(self, size: int) -> int:
        aligned = self._align(size, WORD_SIZE)
        self.current_stack_offset -= aligned
        if self.current_function_frame is not None:
            self.current_function_frame.max_local_offset = min(
                self.current_function_frame.max_local_offset,
                self.current_stack_offset,
            )
        return self.current_stack_offset

    def allocate_code(self) -> int:
        address = self.next_code_address
        self.next_code_address += WORD_SIZE
        return address

    def allocate_label(self) -> int:
        return self.allocate_code()

    def assign_function_address(self, symbol: Symbol):
        symbol.segment = "code"
        symbol.address = self.allocate_code()

    def assign_global_address(self, symbol: Symbol):
        if symbol.type_info is None:
            return
        symbol.size = symbol.type_info.total_size()
        symbol.alignment = WORD_SIZE
        symbol.segment = "global"
        symbol.address = self.allocate_global(symbol.size)

    def assign_local_offset(self, symbol: Symbol):
        if symbol.type_info is None:
            return
        symbol.size = symbol.type_info.total_size()
        symbol.alignment = WORD_SIZE
        symbol.segment = "stack"
        symbol.offset = self.allocate_local(symbol.size)

    def assign_parameter_location(self, symbol: Symbol, index: int):
        if symbol.type_info is not None:
            symbol.size = WORD_SIZE if symbol.type_info.is_array else symbol.type_info.total_size()
            symbol.alignment = WORD_SIZE

        symbol.segment = "param"
        if index < PARAM_REGISTER_LIMIT:
            symbol.register = f"p{index}"
            if self.current_function_frame is not None:
                self.current_function_frame.parameter_registers.append(symbol.register)
        else:
            symbol.register = None
            aligned = self._align(symbol.size or WORD_SIZE, WORD_SIZE)
            symbol.offset = self.current_parameter_offset
            self.current_parameter_offset += aligned
            if self.current_function_frame is not None:
                self.current_function_frame.stack_parameters += 1
                self.current_function_frame.parameter_size += aligned

    #  utilidades

    def current_function_scope(self) -> Optional[Scope]:
        scope = self.current_scope
        while scope is not None:
            if scope.kind == "function":
                return scope
            scope = scope.parent
        return None

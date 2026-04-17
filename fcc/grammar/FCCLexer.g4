lexer grammar FCCLexer;

// 1. PALABRAS RESERVADAS

FUNC      : 'func';
RET       : 'ret';
VOID      : 'void';
INT       : 'int';
BOOL      : 'bool';
CHAR      : 'char';
IF        : 'if';
ELIF      : 'elif';
ELSE      : 'else';
FOR       : 'for';
WHILE     : 'while';
VAULT     : 'vault';
TRUE      : 'true';
FALSE     : 'false';
TRAIGASE  : 'traigase';
MAIN      : 'main';
CONTINUE  : 'continue';


// 2. PRAGMA / ANOTACIONES

SECURE    : '@secure';


// 3. OPERADORES DE COMPARACION

EQ            : '==';
NEQ           : '!=';
LE            : '<=';
GE            : '>=';
SHIFT_LEFT    : '<<';
SHIFT_RIGHT   : '>>';
LT            : '<';
GT            : '>';


// 4. OPERADORES DE ASIGNACION COMPUESTA

PLUS_ASSIGN    : '+=';
MINUS_ASSIGN   : '-=';
STAR_ASSIGN    : '*=';
SLASH_ASSIGN   : '/=';
PERCENT_ASSIGN : '%=';
AND_ASSIGN     : '&=';
OR_ASSIGN      : '|=';
XOR_ASSIGN     : '^=';


// 5. OPERADORES SIMPLES

PLUS       : '+';
MINUS      : '-';
STAR       : '*';
SLASH      : '/';
PERCENT    : '%';
POWER      : '~';
AMPERSAND  : '&';
OR         : '|';
XOR        : '^';
NOT        : '!';
ASSIGN     : '=';


// 6. DELIMITADORES

LBRACE    : '{';
RBRACE    : '}';
LPAREN    : '(';
RPAREN    : ')';
LBRACK    : '[';
RBRACK    : ']';
SEMI      : ';';
COMMA     : ',';
DOT       : '.';


// 7. LITERALES

HEX_LITERAL
    : '0' [xX] [0-9a-fA-F]+
    ;

INT_LITERAL
    : [0-9]+
    ;

CHAR_LITERAL
    : '\'' ( ESC_SEQ | ~['\\\r\n] ) '\''
    ;

STRING_LITERAL
    : '"' ( ESC_SEQ | ~["\\\r\n] )* '"'
    ;


// 8. IDENTIFICADORES

IDENTIFIER
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;


// 9. COMENTARIOS Y ERRORES RELACIONADOS

INVALID_HASH_OPERATOR
    : '##='
    | '##'
    | '=##'
    | '#='
    | '=#'
    ;

// Comentario multilinea correcto. Solo se cierra con la secuencia exacta *#.
BLOCK_COMMENT
    : '#*' .*? '*#' -> skip
    ;

// Si empieza con #* y nunca aparece *#, el comentario esta mal cerrado.
// Cubre finales como solo * o solo # porque ninguno equivale al cierre exacto.
UNCLOSED_BLOCK_COMMENT
    : '#*' ( ~[*] | '*' ~[#] )* '*'? EOF
    ;

// Comentario de linea. No debe tragarse #*, ## ni #=.
LINE_COMMENT
    : '#' ( ~[*#=\r\n] ~[\r\n]* )? -> skip
    ;


// 10. OPERADORES NO RECONOCIDOS

fragment OPERATOR_CHAR
    : [+\-*/%&|^!=<>~]
    ;

INVALID_OPERATOR
    : OPERATOR_CHAR OPERATOR_CHAR+
    ;


// 11. ESPACIOS EN BLANCO

WS
    : [ \t\r\n]+ -> skip
    ;


// 12. FRAGMENTOS AUXILIARES

fragment ESC_SEQ
    : '\\' [btnr"'\\]
    ;


// 13. ERROR LEXICO GENERAL

ERROR_CHAR
    : .
    ;

# Generated from fcc/grammar/FCCParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,70,406,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,1,0,5,0,104,8,0,10,
        0,12,0,107,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,115,8,1,1,2,1,2,1,2,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,135,
        8,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,5,8,145,8,8,10,8,12,8,148,9,
        8,1,9,1,9,1,9,1,10,1,10,5,10,155,8,10,10,10,12,10,158,9,10,1,10,
        5,10,161,8,10,10,10,12,10,164,9,10,1,11,1,11,1,12,1,12,3,12,170,
        8,12,1,12,1,12,1,13,1,13,5,13,176,8,13,10,13,12,13,179,9,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,193,
        8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,5,16,202,8,16,10,16,12,16,
        205,9,16,1,17,1,17,5,17,209,8,17,10,17,12,17,212,9,17,1,17,1,17,
        3,17,216,8,17,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,
        1,21,1,22,1,22,1,23,1,23,3,23,233,8,23,1,23,1,23,1,24,1,24,1,24,
        1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,5,27,
        252,8,27,10,27,12,27,255,9,27,1,27,3,27,258,8,27,1,28,1,28,1,28,
        1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,3,32,287,
        8,32,1,33,1,33,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,37,1,37,1,37,
        5,37,301,8,37,10,37,12,37,304,9,37,1,38,1,38,1,38,5,38,309,8,38,
        10,38,12,38,312,9,38,1,39,1,39,1,39,5,39,317,8,39,10,39,12,39,320,
        9,39,1,40,1,40,1,40,5,40,325,8,40,10,40,12,40,328,9,40,1,41,1,41,
        1,41,5,41,333,8,41,10,41,12,41,336,9,41,1,42,1,42,1,42,5,42,341,
        8,42,10,42,12,42,344,9,42,1,43,1,43,1,43,5,43,349,8,43,10,43,12,
        43,352,9,43,1,44,1,44,1,44,5,44,357,8,44,10,44,12,44,360,9,44,1,
        45,1,45,1,45,3,45,365,8,45,1,46,1,46,5,46,369,8,46,10,46,12,46,372,
        9,46,1,47,1,47,3,47,376,8,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,
        3,47,385,8,47,1,48,1,48,1,48,5,48,390,8,48,10,48,12,48,393,9,48,
        1,49,1,49,1,49,1,49,1,49,1,49,1,49,3,49,402,8,49,1,50,1,50,1,50,
        0,0,51,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,
        86,88,90,92,94,96,98,100,0,10,2,0,17,17,63,63,2,0,3,7,13,13,2,0,
        29,36,47,47,1,0,21,22,2,0,23,24,27,28,1,0,25,26,1,0,37,38,1,0,39,
        42,3,0,38,39,43,43,46,46,3,0,14,15,57,57,59,62,397,0,105,1,0,0,0,
        2,114,1,0,0,0,4,116,1,0,0,0,6,119,1,0,0,0,8,122,1,0,0,0,10,127,1,
        0,0,0,12,129,1,0,0,0,14,139,1,0,0,0,16,141,1,0,0,0,18,149,1,0,0,
        0,20,152,1,0,0,0,22,165,1,0,0,0,24,167,1,0,0,0,26,173,1,0,0,0,28,
        192,1,0,0,0,30,194,1,0,0,0,32,198,1,0,0,0,34,206,1,0,0,0,36,217,
        1,0,0,0,38,219,1,0,0,0,40,222,1,0,0,0,42,226,1,0,0,0,44,228,1,0,
        0,0,46,230,1,0,0,0,48,236,1,0,0,0,50,239,1,0,0,0,52,242,1,0,0,0,
        54,245,1,0,0,0,56,259,1,0,0,0,58,265,1,0,0,0,60,268,1,0,0,0,62,274,
        1,0,0,0,64,286,1,0,0,0,66,288,1,0,0,0,68,290,1,0,0,0,70,292,1,0,
        0,0,72,295,1,0,0,0,74,297,1,0,0,0,76,305,1,0,0,0,78,313,1,0,0,0,
        80,321,1,0,0,0,82,329,1,0,0,0,84,337,1,0,0,0,86,345,1,0,0,0,88,353,
        1,0,0,0,90,364,1,0,0,0,92,366,1,0,0,0,94,384,1,0,0,0,96,386,1,0,
        0,0,98,401,1,0,0,0,100,403,1,0,0,0,102,104,3,2,1,0,103,102,1,0,0,
        0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,
        0,107,105,1,0,0,0,108,109,5,0,0,1,109,1,1,0,0,0,110,115,3,4,2,0,
        111,115,3,6,3,0,112,115,3,12,6,0,113,115,3,14,7,0,114,110,1,0,0,
        0,114,111,1,0,0,0,114,112,1,0,0,0,114,113,1,0,0,0,115,3,1,0,0,0,
        116,117,5,16,0,0,117,118,5,62,0,0,118,5,1,0,0,0,119,120,3,8,4,0,
        120,121,3,12,6,0,121,7,1,0,0,0,122,123,5,20,0,0,123,124,5,50,0,0,
        124,125,5,57,0,0,125,126,5,51,0,0,126,9,1,0,0,0,127,128,7,0,0,0,
        128,11,1,0,0,0,129,130,5,1,0,0,130,131,3,20,10,0,131,132,3,10,5,
        0,132,134,5,50,0,0,133,135,3,16,8,0,134,133,1,0,0,0,134,135,1,0,
        0,0,135,136,1,0,0,0,136,137,5,51,0,0,137,138,3,26,13,0,138,13,1,
        0,0,0,139,140,3,30,15,0,140,15,1,0,0,0,141,146,3,18,9,0,142,143,
        5,55,0,0,143,145,3,18,9,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,17,1,0,0,0,148,146,1,0,0,0,149,150,3,
        20,10,0,150,151,5,63,0,0,151,19,1,0,0,0,152,156,3,22,11,0,153,155,
        5,39,0,0,154,153,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,
        1,0,0,0,157,162,1,0,0,0,158,156,1,0,0,0,159,161,3,24,12,0,160,159,
        1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,21,1,
        0,0,0,164,162,1,0,0,0,165,166,7,1,0,0,166,23,1,0,0,0,167,169,5,52,
        0,0,168,170,3,72,36,0,169,168,1,0,0,0,169,170,1,0,0,0,170,171,1,
        0,0,0,171,172,5,53,0,0,172,25,1,0,0,0,173,177,5,48,0,0,174,176,3,
        28,14,0,175,174,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,
        1,0,0,0,178,180,1,0,0,0,179,177,1,0,0,0,180,181,5,49,0,0,181,27,
        1,0,0,0,182,193,3,30,15,0,183,193,3,38,19,0,184,193,3,54,27,0,185,
        193,3,60,30,0,186,193,3,62,31,0,187,193,3,46,23,0,188,193,3,48,24,
        0,189,193,3,50,25,0,190,193,3,52,26,0,191,193,3,26,13,0,192,182,
        1,0,0,0,192,183,1,0,0,0,192,184,1,0,0,0,192,185,1,0,0,0,192,186,
        1,0,0,0,192,187,1,0,0,0,192,188,1,0,0,0,192,189,1,0,0,0,192,190,
        1,0,0,0,192,191,1,0,0,0,193,29,1,0,0,0,194,195,3,20,10,0,195,196,
        3,32,16,0,196,197,5,54,0,0,197,31,1,0,0,0,198,203,3,34,17,0,199,
        200,5,55,0,0,200,202,3,34,17,0,201,199,1,0,0,0,202,205,1,0,0,0,203,
        201,1,0,0,0,203,204,1,0,0,0,204,33,1,0,0,0,205,203,1,0,0,0,206,210,
        5,63,0,0,207,209,3,24,12,0,208,207,1,0,0,0,209,212,1,0,0,0,210,208,
        1,0,0,0,210,211,1,0,0,0,211,215,1,0,0,0,212,210,1,0,0,0,213,214,
        5,47,0,0,214,216,3,36,18,0,215,213,1,0,0,0,215,216,1,0,0,0,216,35,
        1,0,0,0,217,218,3,72,36,0,218,37,1,0,0,0,219,220,3,40,20,0,220,221,
        5,54,0,0,221,39,1,0,0,0,222,223,3,44,22,0,223,224,3,42,21,0,224,
        225,3,72,36,0,225,41,1,0,0,0,226,227,7,2,0,0,227,43,1,0,0,0,228,
        229,3,92,46,0,229,45,1,0,0,0,230,232,5,2,0,0,231,233,3,72,36,0,232,
        231,1,0,0,0,232,233,1,0,0,0,233,234,1,0,0,0,234,235,5,54,0,0,235,
        47,1,0,0,0,236,237,5,18,0,0,237,238,5,54,0,0,238,49,1,0,0,0,239,
        240,5,19,0,0,240,241,5,54,0,0,241,51,1,0,0,0,242,243,3,72,36,0,243,
        244,5,54,0,0,244,53,1,0,0,0,245,246,5,8,0,0,246,247,5,50,0,0,247,
        248,3,72,36,0,248,249,5,51,0,0,249,253,3,26,13,0,250,252,3,56,28,
        0,251,250,1,0,0,0,252,255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,
        0,254,257,1,0,0,0,255,253,1,0,0,0,256,258,3,58,29,0,257,256,1,0,
        0,0,257,258,1,0,0,0,258,55,1,0,0,0,259,260,5,9,0,0,260,261,5,50,
        0,0,261,262,3,72,36,0,262,263,5,51,0,0,263,264,3,26,13,0,264,57,
        1,0,0,0,265,266,5,10,0,0,266,267,3,26,13,0,267,59,1,0,0,0,268,269,
        5,12,0,0,269,270,5,50,0,0,270,271,3,72,36,0,271,272,5,51,0,0,272,
        273,3,26,13,0,273,61,1,0,0,0,274,275,5,11,0,0,275,276,5,50,0,0,276,
        277,3,64,32,0,277,278,5,54,0,0,278,279,3,66,33,0,279,280,5,54,0,
        0,280,281,3,68,34,0,281,282,5,51,0,0,282,283,3,26,13,0,283,63,1,
        0,0,0,284,287,3,70,35,0,285,287,3,40,20,0,286,284,1,0,0,0,286,285,
        1,0,0,0,287,65,1,0,0,0,288,289,3,40,20,0,289,67,1,0,0,0,290,291,
        3,72,36,0,291,69,1,0,0,0,292,293,3,20,10,0,293,294,3,32,16,0,294,
        71,1,0,0,0,295,296,3,74,37,0,296,73,1,0,0,0,297,302,3,76,38,0,298,
        299,5,44,0,0,299,301,3,76,38,0,300,298,1,0,0,0,301,304,1,0,0,0,302,
        300,1,0,0,0,302,303,1,0,0,0,303,75,1,0,0,0,304,302,1,0,0,0,305,310,
        3,78,39,0,306,307,5,45,0,0,307,309,3,78,39,0,308,306,1,0,0,0,309,
        312,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,77,1,0,0,0,312,310,
        1,0,0,0,313,318,3,80,40,0,314,315,5,43,0,0,315,317,3,80,40,0,316,
        314,1,0,0,0,317,320,1,0,0,0,318,316,1,0,0,0,318,319,1,0,0,0,319,
        79,1,0,0,0,320,318,1,0,0,0,321,326,3,82,41,0,322,323,7,3,0,0,323,
        325,3,82,41,0,324,322,1,0,0,0,325,328,1,0,0,0,326,324,1,0,0,0,326,
        327,1,0,0,0,327,81,1,0,0,0,328,326,1,0,0,0,329,334,3,84,42,0,330,
        331,7,4,0,0,331,333,3,84,42,0,332,330,1,0,0,0,333,336,1,0,0,0,334,
        332,1,0,0,0,334,335,1,0,0,0,335,83,1,0,0,0,336,334,1,0,0,0,337,342,
        3,86,43,0,338,339,7,5,0,0,339,341,3,86,43,0,340,338,1,0,0,0,341,
        344,1,0,0,0,342,340,1,0,0,0,342,343,1,0,0,0,343,85,1,0,0,0,344,342,
        1,0,0,0,345,350,3,88,44,0,346,347,7,6,0,0,347,349,3,88,44,0,348,
        346,1,0,0,0,349,352,1,0,0,0,350,348,1,0,0,0,350,351,1,0,0,0,351,
        87,1,0,0,0,352,350,1,0,0,0,353,358,3,90,45,0,354,355,7,7,0,0,355,
        357,3,90,45,0,356,354,1,0,0,0,357,360,1,0,0,0,358,356,1,0,0,0,358,
        359,1,0,0,0,359,89,1,0,0,0,360,358,1,0,0,0,361,362,7,8,0,0,362,365,
        3,90,45,0,363,365,3,92,46,0,364,361,1,0,0,0,364,363,1,0,0,0,365,
        91,1,0,0,0,366,370,3,98,49,0,367,369,3,94,47,0,368,367,1,0,0,0,369,
        372,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,93,1,0,0,0,372,370,
        1,0,0,0,373,375,5,50,0,0,374,376,3,96,48,0,375,374,1,0,0,0,375,376,
        1,0,0,0,376,377,1,0,0,0,377,385,5,51,0,0,378,379,5,52,0,0,379,380,
        3,72,36,0,380,381,5,53,0,0,381,385,1,0,0,0,382,383,5,56,0,0,383,
        385,5,63,0,0,384,373,1,0,0,0,384,378,1,0,0,0,384,382,1,0,0,0,385,
        95,1,0,0,0,386,391,3,72,36,0,387,388,5,55,0,0,388,390,3,72,36,0,
        389,387,1,0,0,0,390,393,1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,
        392,97,1,0,0,0,393,391,1,0,0,0,394,402,5,63,0,0,395,402,5,17,0,0,
        396,402,3,100,50,0,397,398,5,50,0,0,398,399,3,72,36,0,399,400,5,
        51,0,0,400,402,1,0,0,0,401,394,1,0,0,0,401,395,1,0,0,0,401,396,1,
        0,0,0,401,397,1,0,0,0,402,99,1,0,0,0,403,404,7,9,0,0,404,101,1,0,
        0,0,30,105,114,134,146,156,162,169,177,192,203,210,215,232,253,257,
        286,302,310,318,326,334,342,350,358,364,370,375,384,391,401
    ]

class FCCParser ( Parser ):

    grammarFileName = "FCCParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'ret'", "'void'", "'int'", 
                     "'float'", "'bool'", "'char'", "'if'", "'elif'", "'else'", 
                     "'for'", "'while'", "'vault'", "'true'", "'false'", 
                     "'traigase'", "'main'", "'continue'", "'break'", "'@secure'", 
                     "'=='", "'!='", "'<='", "'>='", "'<<'", "'>>'", "'<'", 
                     "'>'", "'+='", "'-='", "'*='", "'/='", "'%='", "'&='", 
                     "'|='", "'^='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'~'", "'&'", "'|'", "'^'", "'!'", "'='", "'{'", "'}'", 
                     "'('", "')'", "'['", "']'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "FUNC", "RET", "VOID", "INT", "FLOAT", 
                      "BOOL", "CHAR", "IF", "ELIF", "ELSE", "FOR", "WHILE", 
                      "VAULT", "TRUE", "FALSE", "TRAIGASE", "MAIN", "CONTINUE", 
                      "BREAK", "SECURE", "EQ", "NEQ", "LE", "GE", "SHIFT_LEFT", 
                      "SHIFT_RIGHT", "LT", "GT", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                      "STAR_ASSIGN", "SLASH_ASSIGN", "PERCENT_ASSIGN", "AND_ASSIGN", 
                      "OR_ASSIGN", "XOR_ASSIGN", "PLUS", "MINUS", "STAR", 
                      "SLASH", "PERCENT", "POWER", "AMPERSAND", "OR", "XOR", 
                      "NOT", "ASSIGN", "LBRACE", "RBRACE", "LPAREN", "RPAREN", 
                      "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", "HEX_LITERAL", 
                      "INVALID_REAL_LITERAL", "REAL_LITERAL", "INT_LITERAL", 
                      "CHAR_LITERAL", "STRING_LITERAL", "IDENTIFIER", "INVALID_HASH_OPERATOR", 
                      "BLOCK_COMMENT", "UNCLOSED_BLOCK_COMMENT", "LINE_COMMENT", 
                      "INVALID_OPERATOR", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_topLevelDecl = 1
    RULE_importStmt = 2
    RULE_secureFunctionDecl = 3
    RULE_secureAnnotation = 4
    RULE_functionName = 5
    RULE_functionDecl = 6
    RULE_globalVarDecl = 7
    RULE_parameterList = 8
    RULE_parameter = 9
    RULE_typeRule = 10
    RULE_baseType = 11
    RULE_arraySuffix = 12
    RULE_block = 13
    RULE_statement = 14
    RULE_varDecl = 15
    RULE_variableDeclaratorList = 16
    RULE_variableDeclarator = 17
    RULE_initializer = 18
    RULE_assignmentStmt = 19
    RULE_assignment = 20
    RULE_assignmentOperator = 21
    RULE_assignable = 22
    RULE_returnStmt = 23
    RULE_continueStmt = 24
    RULE_breakStmt = 25
    RULE_exprStmt = 26
    RULE_ifStmt = 27
    RULE_elifBranch = 28
    RULE_elseBranch = 29
    RULE_whileStmt = 30
    RULE_forStmt = 31
    RULE_forInitializer = 32
    RULE_forIncrement = 33
    RULE_forCondition = 34
    RULE_varDeclNoSemi = 35
    RULE_expression = 36
    RULE_bitwiseOrExpression = 37
    RULE_bitwiseXorExpression = 38
    RULE_bitwiseAndExpression = 39
    RULE_equalityExpression = 40
    RULE_relationalExpression = 41
    RULE_shiftExpression = 42
    RULE_additiveExpression = 43
    RULE_multiplicativeExpression = 44
    RULE_unaryExpression = 45
    RULE_postfixExpression = 46
    RULE_postfixSuffix = 47
    RULE_argumentList = 48
    RULE_primary = 49
    RULE_literal = 50

    ruleNames =  [ "program", "topLevelDecl", "importStmt", "secureFunctionDecl", 
                   "secureAnnotation", "functionName", "functionDecl", "globalVarDecl", 
                   "parameterList", "parameter", "typeRule", "baseType", 
                   "arraySuffix", "block", "statement", "varDecl", "variableDeclaratorList", 
                   "variableDeclarator", "initializer", "assignmentStmt", 
                   "assignment", "assignmentOperator", "assignable", "returnStmt", 
                   "continueStmt", "breakStmt", "exprStmt", "ifStmt", "elifBranch", 
                   "elseBranch", "whileStmt", "forStmt", "forInitializer", 
                   "forIncrement", "forCondition", "varDeclNoSemi", "expression", 
                   "bitwiseOrExpression", "bitwiseXorExpression", "bitwiseAndExpression", 
                   "equalityExpression", "relationalExpression", "shiftExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "postfixExpression", "postfixSuffix", "argumentList", 
                   "primary", "literal" ]

    EOF = Token.EOF
    FUNC=1
    RET=2
    VOID=3
    INT=4
    FLOAT=5
    BOOL=6
    CHAR=7
    IF=8
    ELIF=9
    ELSE=10
    FOR=11
    WHILE=12
    VAULT=13
    TRUE=14
    FALSE=15
    TRAIGASE=16
    MAIN=17
    CONTINUE=18
    BREAK=19
    SECURE=20
    EQ=21
    NEQ=22
    LE=23
    GE=24
    SHIFT_LEFT=25
    SHIFT_RIGHT=26
    LT=27
    GT=28
    PLUS_ASSIGN=29
    MINUS_ASSIGN=30
    STAR_ASSIGN=31
    SLASH_ASSIGN=32
    PERCENT_ASSIGN=33
    AND_ASSIGN=34
    OR_ASSIGN=35
    XOR_ASSIGN=36
    PLUS=37
    MINUS=38
    STAR=39
    SLASH=40
    PERCENT=41
    POWER=42
    AMPERSAND=43
    OR=44
    XOR=45
    NOT=46
    ASSIGN=47
    LBRACE=48
    RBRACE=49
    LPAREN=50
    RPAREN=51
    LBRACK=52
    RBRACK=53
    SEMI=54
    COMMA=55
    DOT=56
    HEX_LITERAL=57
    INVALID_REAL_LITERAL=58
    REAL_LITERAL=59
    INT_LITERAL=60
    CHAR_LITERAL=61
    STRING_LITERAL=62
    IDENTIFIER=63
    INVALID_HASH_OPERATOR=64
    BLOCK_COMMENT=65
    UNCLOSED_BLOCK_COMMENT=66
    LINE_COMMENT=67
    INVALID_OPERATOR=68
    WS=69
    ERROR_CHAR=70

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FCCParser.EOF, 0)

        def topLevelDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.TopLevelDeclContext)
            else:
                return self.getTypedRuleContext(FCCParser.TopLevelDeclContext,i)


        def getRuleIndex(self):
            return FCCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = FCCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1122554) != 0):
                self.state = 102
                self.topLevelDecl()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(FCCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importStmt(self):
            return self.getTypedRuleContext(FCCParser.ImportStmtContext,0)


        def secureFunctionDecl(self):
            return self.getTypedRuleContext(FCCParser.SecureFunctionDeclContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(FCCParser.FunctionDeclContext,0)


        def globalVarDecl(self):
            return self.getTypedRuleContext(FCCParser.GlobalVarDeclContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_topLevelDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelDecl" ):
                listener.enterTopLevelDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelDecl" ):
                listener.exitTopLevelDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelDecl" ):
                return visitor.visitTopLevelDecl(self)
            else:
                return visitor.visitChildren(self)




    def topLevelDecl(self):

        localctx = FCCParser.TopLevelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topLevelDecl)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.importStmt()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.secureFunctionDecl()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.functionDecl()
                pass
            elif token in [3, 4, 5, 6, 7, 13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.globalVarDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRAIGASE(self):
            return self.getToken(FCCParser.TRAIGASE, 0)

        def STRING_LITERAL(self):
            return self.getToken(FCCParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_importStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStmt" ):
                listener.enterImportStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStmt" ):
                listener.exitImportStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStmt" ):
                return visitor.visitImportStmt(self)
            else:
                return visitor.visitChildren(self)




    def importStmt(self):

        localctx = FCCParser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(FCCParser.TRAIGASE)
            self.state = 117
            self.match(FCCParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecureFunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def secureAnnotation(self):
            return self.getTypedRuleContext(FCCParser.SecureAnnotationContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(FCCParser.FunctionDeclContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_secureFunctionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecureFunctionDecl" ):
                listener.enterSecureFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecureFunctionDecl" ):
                listener.exitSecureFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecureFunctionDecl" ):
                return visitor.visitSecureFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def secureFunctionDecl(self):

        localctx = FCCParser.SecureFunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_secureFunctionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.secureAnnotation()
            self.state = 120
            self.functionDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecureAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SECURE(self):
            return self.getToken(FCCParser.SECURE, 0)

        def LPAREN(self):
            return self.getToken(FCCParser.LPAREN, 0)

        def HEX_LITERAL(self):
            return self.getToken(FCCParser.HEX_LITERAL, 0)

        def RPAREN(self):
            return self.getToken(FCCParser.RPAREN, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_secureAnnotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecureAnnotation" ):
                listener.enterSecureAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecureAnnotation" ):
                listener.exitSecureAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecureAnnotation" ):
                return visitor.visitSecureAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def secureAnnotation(self):

        localctx = FCCParser.SecureAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_secureAnnotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(FCCParser.SECURE)
            self.state = 123
            self.match(FCCParser.LPAREN)
            self.state = 124
            self.match(FCCParser.HEX_LITERAL)
            self.state = 125
            self.match(FCCParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FCCParser.IDENTIFIER, 0)

        def MAIN(self):
            return self.getToken(FCCParser.MAIN, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_functionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionName" ):
                listener.enterFunctionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionName" ):
                listener.exitFunctionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionName" ):
                return visitor.visitFunctionName(self)
            else:
                return visitor.visitChildren(self)




    def functionName(self):

        localctx = FCCParser.FunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not(_la==17 or _la==63):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(FCCParser.FUNC, 0)

        def typeRule(self):
            return self.getTypedRuleContext(FCCParser.TypeRuleContext,0)


        def functionName(self):
            return self.getTypedRuleContext(FCCParser.FunctionNameContext,0)


        def LPAREN(self):
            return self.getToken(FCCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(FCCParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(FCCParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(FCCParser.ParameterListContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = FCCParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(FCCParser.FUNC)
            self.state = 130
            self.typeRule()
            self.state = 131
            self.functionName()
            self.state = 132
            self.match(FCCParser.LPAREN)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8440) != 0):
                self.state = 133
                self.parameterList()


            self.state = 136
            self.match(FCCParser.RPAREN)
            self.state = 137
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalVarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(FCCParser.VarDeclContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_globalVarDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalVarDecl" ):
                listener.enterGlobalVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalVarDecl" ):
                listener.exitGlobalVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalVarDecl" ):
                return visitor.visitGlobalVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def globalVarDecl(self):

        localctx = FCCParser.GlobalVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_globalVarDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.varDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.ParameterContext)
            else:
                return self.getTypedRuleContext(FCCParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.COMMA)
            else:
                return self.getToken(FCCParser.COMMA, i)

        def getRuleIndex(self):
            return FCCParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = FCCParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.parameter()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 142
                self.match(FCCParser.COMMA)
                self.state = 143
                self.parameter()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeRule(self):
            return self.getTypedRuleContext(FCCParser.TypeRuleContext,0)


        def IDENTIFIER(self):
            return self.getToken(FCCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = FCCParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.typeRule()
            self.state = 150
            self.match(FCCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(FCCParser.BaseTypeContext,0)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.STAR)
            else:
                return self.getToken(FCCParser.STAR, i)

        def arraySuffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.ArraySuffixContext)
            else:
                return self.getTypedRuleContext(FCCParser.ArraySuffixContext,i)


        def getRuleIndex(self):
            return FCCParser.RULE_typeRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeRule" ):
                listener.enterTypeRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeRule" ):
                listener.exitTypeRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeRule" ):
                return visitor.visitTypeRule(self)
            else:
                return visitor.visitChildren(self)




    def typeRule(self):

        localctx = FCCParser.TypeRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.baseType()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 153
                self.match(FCCParser.STAR)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 159
                self.arraySuffix()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(FCCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(FCCParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(FCCParser.BOOL, 0)

        def CHAR(self):
            return self.getToken(FCCParser.CHAR, 0)

        def VOID(self):
            return self.getToken(FCCParser.VOID, 0)

        def VAULT(self):
            return self.getToken(FCCParser.VAULT, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_baseType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseType" ):
                listener.enterBaseType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseType" ):
                listener.exitBaseType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = FCCParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraySuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(FCCParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(FCCParser.RBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_arraySuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraySuffix" ):
                listener.enterArraySuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraySuffix" ):
                listener.exitArraySuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraySuffix" ):
                return visitor.visitArraySuffix(self)
            else:
                return visitor.visitChildren(self)




    def arraySuffix(self):

        localctx = FCCParser.ArraySuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arraySuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(FCCParser.LBRACK)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -431139674849624064) != 0):
                self.state = 168
                self.expression()


            self.state = 171
            self.match(FCCParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(FCCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(FCCParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.StatementContext)
            else:
                return self.getTypedRuleContext(FCCParser.StatementContext,i)


        def getRuleIndex(self):
            return FCCParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = FCCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(FCCParser.LBRACE)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -430858199872112132) != 0):
                self.state = 174
                self.statement()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(FCCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(FCCParser.VarDeclContext,0)


        def assignmentStmt(self):
            return self.getTypedRuleContext(FCCParser.AssignmentStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(FCCParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(FCCParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(FCCParser.ForStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(FCCParser.ReturnStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(FCCParser.ContinueStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(FCCParser.BreakStmtContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(FCCParser.ExprStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(FCCParser.BlockContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = FCCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.assignmentStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.whileStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                self.forStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 187
                self.returnStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 188
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 189
                self.breakStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 190
                self.exprStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 191
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeRule(self):
            return self.getTypedRuleContext(FCCParser.TypeRuleContext,0)


        def variableDeclaratorList(self):
            return self.getTypedRuleContext(FCCParser.VariableDeclaratorListContext,0)


        def SEMI(self):
            return self.getToken(FCCParser.SEMI, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = FCCParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.typeRule()
            self.state = 195
            self.variableDeclaratorList()
            self.state = 196
            self.match(FCCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.VariableDeclaratorContext)
            else:
                return self.getTypedRuleContext(FCCParser.VariableDeclaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.COMMA)
            else:
                return self.getToken(FCCParser.COMMA, i)

        def getRuleIndex(self):
            return FCCParser.RULE_variableDeclaratorList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaratorList" ):
                listener.enterVariableDeclaratorList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaratorList" ):
                listener.exitVariableDeclaratorList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaratorList" ):
                return visitor.visitVariableDeclaratorList(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaratorList(self):

        localctx = FCCParser.VariableDeclaratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variableDeclaratorList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.variableDeclarator()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 199
                self.match(FCCParser.COMMA)
                self.state = 200
                self.variableDeclarator()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FCCParser.IDENTIFIER, 0)

        def arraySuffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.ArraySuffixContext)
            else:
                return self.getTypedRuleContext(FCCParser.ArraySuffixContext,i)


        def ASSIGN(self):
            return self.getToken(FCCParser.ASSIGN, 0)

        def initializer(self):
            return self.getTypedRuleContext(FCCParser.InitializerContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarator" ):
                return visitor.visitVariableDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarator(self):

        localctx = FCCParser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_variableDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(FCCParser.IDENTIFIER)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 207
                self.arraySuffix()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 213
                self.match(FCCParser.ASSIGN)
                self.state = 214
                self.initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer" ):
                listener.enterInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer" ):
                listener.exitInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer" ):
                return visitor.visitInitializer(self)
            else:
                return visitor.visitChildren(self)




    def initializer(self):

        localctx = FCCParser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_initializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(FCCParser.AssignmentContext,0)


        def SEMI(self):
            return self.getToken(FCCParser.SEMI, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_assignmentStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStmt" ):
                listener.enterAssignmentStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStmt" ):
                listener.exitAssignmentStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStmt" ):
                return visitor.visitAssignmentStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStmt(self):

        localctx = FCCParser.AssignmentStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignmentStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.assignment()
            self.state = 220
            self.match(FCCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignable(self):
            return self.getTypedRuleContext(FCCParser.AssignableContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(FCCParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = FCCParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.assignable()
            self.state = 223
            self.assignmentOperator()
            self.state = 224
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(FCCParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(FCCParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(FCCParser.MINUS_ASSIGN, 0)

        def STAR_ASSIGN(self):
            return self.getToken(FCCParser.STAR_ASSIGN, 0)

        def SLASH_ASSIGN(self):
            return self.getToken(FCCParser.SLASH_ASSIGN, 0)

        def PERCENT_ASSIGN(self):
            return self.getToken(FCCParser.PERCENT_ASSIGN, 0)

        def AND_ASSIGN(self):
            return self.getToken(FCCParser.AND_ASSIGN, 0)

        def OR_ASSIGN(self):
            return self.getToken(FCCParser.OR_ASSIGN, 0)

        def XOR_ASSIGN(self):
            return self.getToken(FCCParser.XOR_ASSIGN, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = FCCParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140874390437888) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(FCCParser.PostfixExpressionContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_assignable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignable" ):
                listener.enterAssignable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignable" ):
                listener.exitAssignable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignable" ):
                return visitor.visitAssignable(self)
            else:
                return visitor.visitChildren(self)




    def assignable(self):

        localctx = FCCParser.AssignableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.postfixExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RET(self):
            return self.getToken(FCCParser.RET, 0)

        def SEMI(self):
            return self.getToken(FCCParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = FCCParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(FCCParser.RET)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -431139674849624064) != 0):
                self.state = 231
                self.expression()


            self.state = 234
            self.match(FCCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(FCCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(FCCParser.SEMI, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = FCCParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(FCCParser.CONTINUE)
            self.state = 237
            self.match(FCCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(FCCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(FCCParser.SEMI, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = FCCParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(FCCParser.BREAK)
            self.state = 240
            self.match(FCCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(FCCParser.SEMI, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_exprStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = FCCParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.expression()
            self.state = 243
            self.match(FCCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(FCCParser.IF, 0)

        def LPAREN(self):
            return self.getToken(FCCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(FCCParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(FCCParser.BlockContext,0)


        def elifBranch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.ElifBranchContext)
            else:
                return self.getTypedRuleContext(FCCParser.ElifBranchContext,i)


        def elseBranch(self):
            return self.getTypedRuleContext(FCCParser.ElseBranchContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = FCCParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(FCCParser.IF)
            self.state = 246
            self.match(FCCParser.LPAREN)
            self.state = 247
            self.expression()
            self.state = 248
            self.match(FCCParser.RPAREN)
            self.state = 249
            self.block()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 250
                self.elifBranch()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 256
                self.elseBranch()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifBranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(FCCParser.ELIF, 0)

        def LPAREN(self):
            return self.getToken(FCCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(FCCParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(FCCParser.BlockContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_elifBranch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElifBranch" ):
                listener.enterElifBranch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElifBranch" ):
                listener.exitElifBranch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifBranch" ):
                return visitor.visitElifBranch(self)
            else:
                return visitor.visitChildren(self)




    def elifBranch(self):

        localctx = FCCParser.ElifBranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elifBranch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(FCCParser.ELIF)
            self.state = 260
            self.match(FCCParser.LPAREN)
            self.state = 261
            self.expression()
            self.state = 262
            self.match(FCCParser.RPAREN)
            self.state = 263
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(FCCParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(FCCParser.BlockContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_elseBranch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBranch" ):
                listener.enterElseBranch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBranch" ):
                listener.exitElseBranch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBranch" ):
                return visitor.visitElseBranch(self)
            else:
                return visitor.visitChildren(self)




    def elseBranch(self):

        localctx = FCCParser.ElseBranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elseBranch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(FCCParser.ELSE)
            self.state = 266
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(FCCParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(FCCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(FCCParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(FCCParser.BlockContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = FCCParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(FCCParser.WHILE)
            self.state = 269
            self.match(FCCParser.LPAREN)
            self.state = 270
            self.expression()
            self.state = 271
            self.match(FCCParser.RPAREN)
            self.state = 272
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(FCCParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(FCCParser.LPAREN, 0)

        def forInitializer(self):
            return self.getTypedRuleContext(FCCParser.ForInitializerContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.SEMI)
            else:
                return self.getToken(FCCParser.SEMI, i)

        def forIncrement(self):
            return self.getTypedRuleContext(FCCParser.ForIncrementContext,0)


        def forCondition(self):
            return self.getTypedRuleContext(FCCParser.ForConditionContext,0)


        def RPAREN(self):
            return self.getToken(FCCParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(FCCParser.BlockContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = FCCParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(FCCParser.FOR)
            self.state = 275
            self.match(FCCParser.LPAREN)
            self.state = 276
            self.forInitializer()
            self.state = 277
            self.match(FCCParser.SEMI)
            self.state = 278
            self.forIncrement()
            self.state = 279
            self.match(FCCParser.SEMI)
            self.state = 280
            self.forCondition()
            self.state = 281
            self.match(FCCParser.RPAREN)
            self.state = 282
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclNoSemi(self):
            return self.getTypedRuleContext(FCCParser.VarDeclNoSemiContext,0)


        def assignment(self):
            return self.getTypedRuleContext(FCCParser.AssignmentContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_forInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitializer" ):
                listener.enterForInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitializer" ):
                listener.exitForInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitializer" ):
                return visitor.visitForInitializer(self)
            else:
                return visitor.visitChildren(self)




    def forInitializer(self):

        localctx = FCCParser.ForInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forInitializer)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 7, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.varDeclNoSemi()
                pass
            elif token in [14, 15, 17, 50, 57, 59, 60, 61, 62, 63]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.assignment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForIncrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(FCCParser.AssignmentContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_forIncrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForIncrement" ):
                listener.enterForIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForIncrement" ):
                listener.exitForIncrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForIncrement" ):
                return visitor.visitForIncrement(self)
            else:
                return visitor.visitChildren(self)




    def forIncrement(self):

        localctx = FCCParser.ForIncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_forCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondition" ):
                listener.enterForCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondition" ):
                listener.exitForCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = FCCParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclNoSemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeRule(self):
            return self.getTypedRuleContext(FCCParser.TypeRuleContext,0)


        def variableDeclaratorList(self):
            return self.getTypedRuleContext(FCCParser.VariableDeclaratorListContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_varDeclNoSemi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclNoSemi" ):
                listener.enterVarDeclNoSemi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclNoSemi" ):
                listener.exitVarDeclNoSemi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclNoSemi" ):
                return visitor.visitVarDeclNoSemi(self)
            else:
                return visitor.visitChildren(self)




    def varDeclNoSemi(self):

        localctx = FCCParser.VarDeclNoSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_varDeclNoSemi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.typeRule()
            self.state = 293
            self.variableDeclaratorList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseOrExpression(self):
            return self.getTypedRuleContext(FCCParser.BitwiseOrExpressionContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = FCCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.bitwiseOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseXorExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.BitwiseXorExpressionContext)
            else:
                return self.getTypedRuleContext(FCCParser.BitwiseXorExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.OR)
            else:
                return self.getToken(FCCParser.OR, i)

        def getRuleIndex(self):
            return FCCParser.RULE_bitwiseOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseOrExpression" ):
                listener.enterBitwiseOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseOrExpression" ):
                listener.exitBitwiseOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseOrExpression" ):
                return visitor.visitBitwiseOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def bitwiseOrExpression(self):

        localctx = FCCParser.BitwiseOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_bitwiseOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.bitwiseXorExpression()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 298
                self.match(FCCParser.OR)
                self.state = 299
                self.bitwiseXorExpression()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseXorExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.BitwiseAndExpressionContext)
            else:
                return self.getTypedRuleContext(FCCParser.BitwiseAndExpressionContext,i)


        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.XOR)
            else:
                return self.getToken(FCCParser.XOR, i)

        def getRuleIndex(self):
            return FCCParser.RULE_bitwiseXorExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseXorExpression" ):
                listener.enterBitwiseXorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseXorExpression" ):
                listener.exitBitwiseXorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseXorExpression" ):
                return visitor.visitBitwiseXorExpression(self)
            else:
                return visitor.visitChildren(self)




    def bitwiseXorExpression(self):

        localctx = FCCParser.BitwiseXorExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_bitwiseXorExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.bitwiseAndExpression()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 306
                self.match(FCCParser.XOR)
                self.state = 307
                self.bitwiseAndExpression()
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(FCCParser.EqualityExpressionContext,i)


        def AMPERSAND(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.AMPERSAND)
            else:
                return self.getToken(FCCParser.AMPERSAND, i)

        def getRuleIndex(self):
            return FCCParser.RULE_bitwiseAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseAndExpression" ):
                listener.enterBitwiseAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseAndExpression" ):
                listener.exitBitwiseAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseAndExpression" ):
                return visitor.visitBitwiseAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def bitwiseAndExpression(self):

        localctx = FCCParser.BitwiseAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_bitwiseAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.equalityExpression()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 314
                self.match(FCCParser.AMPERSAND)
                self.state = 315
                self.equalityExpression()
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(FCCParser.RelationalExpressionContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.EQ)
            else:
                return self.getToken(FCCParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.NEQ)
            else:
                return self.getToken(FCCParser.NEQ, i)

        def getRuleIndex(self):
            return FCCParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = FCCParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.relationalExpression()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 322
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 323
                self.relationalExpression()
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shiftExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.ShiftExpressionContext)
            else:
                return self.getTypedRuleContext(FCCParser.ShiftExpressionContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.LT)
            else:
                return self.getToken(FCCParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.LE)
            else:
                return self.getToken(FCCParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.GT)
            else:
                return self.getToken(FCCParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.GE)
            else:
                return self.getToken(FCCParser.GE, i)

        def getRuleIndex(self):
            return FCCParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = FCCParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.shiftExpression()
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 427819008) != 0):
                self.state = 330
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 427819008) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 331
                self.shiftExpression()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(FCCParser.AdditiveExpressionContext,i)


        def SHIFT_LEFT(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.SHIFT_LEFT)
            else:
                return self.getToken(FCCParser.SHIFT_LEFT, i)

        def SHIFT_RIGHT(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.SHIFT_RIGHT)
            else:
                return self.getToken(FCCParser.SHIFT_RIGHT, i)

        def getRuleIndex(self):
            return FCCParser.RULE_shiftExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftExpression" ):
                listener.enterShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftExpression" ):
                listener.exitShiftExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftExpression" ):
                return visitor.visitShiftExpression(self)
            else:
                return visitor.visitChildren(self)




    def shiftExpression(self):

        localctx = FCCParser.ShiftExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_shiftExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.additiveExpression()
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 338
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 339
                self.additiveExpression()
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(FCCParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.PLUS)
            else:
                return self.getToken(FCCParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.MINUS)
            else:
                return self.getToken(FCCParser.MINUS, i)

        def getRuleIndex(self):
            return FCCParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = FCCParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.multiplicativeExpression()
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37 or _la==38:
                self.state = 346
                _la = self._input.LA(1)
                if not(_la==37 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 347
                self.multiplicativeExpression()
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(FCCParser.UnaryExpressionContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.STAR)
            else:
                return self.getToken(FCCParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.SLASH)
            else:
                return self.getToken(FCCParser.SLASH, i)

        def PERCENT(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.PERCENT)
            else:
                return self.getToken(FCCParser.PERCENT, i)

        def POWER(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.POWER)
            else:
                return self.getToken(FCCParser.POWER, i)

        def getRuleIndex(self):
            return FCCParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = FCCParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.unaryExpression()
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0):
                self.state = 354
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 355
                self.unaryExpression()
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(FCCParser.UnaryExpressionContext,0)


        def NOT(self):
            return self.getToken(FCCParser.NOT, 0)

        def MINUS(self):
            return self.getToken(FCCParser.MINUS, 0)

        def AMPERSAND(self):
            return self.getToken(FCCParser.AMPERSAND, 0)

        def STAR(self):
            return self.getToken(FCCParser.STAR, 0)

        def postfixExpression(self):
            return self.getTypedRuleContext(FCCParser.PostfixExpressionContext,0)


        def getRuleIndex(self):
            return FCCParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = FCCParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38, 39, 43, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 79989470920704) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 362
                self.unaryExpression()
                pass
            elif token in [14, 15, 17, 50, 57, 59, 60, 61, 62, 63]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.postfixExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(FCCParser.PrimaryContext,0)


        def postfixSuffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.PostfixSuffixContext)
            else:
                return self.getTypedRuleContext(FCCParser.PostfixSuffixContext,i)


        def getRuleIndex(self):
            return FCCParser.RULE_postfixExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixExpression" ):
                listener.enterPostfixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixExpression" ):
                listener.exitPostfixExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExpression" ):
                return visitor.visitPostfixExpression(self)
            else:
                return visitor.visitChildren(self)




    def postfixExpression(self):

        localctx = FCCParser.PostfixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_postfixExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.primary()
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 77687093572141056) != 0):
                self.state = 367
                self.postfixSuffix()
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(FCCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(FCCParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(FCCParser.ArgumentListContext,0)


        def LBRACK(self):
            return self.getToken(FCCParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(FCCParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(FCCParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(FCCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_postfixSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixSuffix" ):
                listener.enterPostfixSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixSuffix" ):
                listener.exitPostfixSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixSuffix" ):
                return visitor.visitPostfixSuffix(self)
            else:
                return visitor.visitChildren(self)




    def postfixSuffix(self):

        localctx = FCCParser.PostfixSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_postfixSuffix)
        self._la = 0 # Token type
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(FCCParser.LPAREN)
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -431139674849624064) != 0):
                    self.state = 374
                    self.argumentList()


                self.state = 377
                self.match(FCCParser.RPAREN)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.match(FCCParser.LBRACK)
                self.state = 379
                self.expression()
                self.state = 380
                self.match(FCCParser.RBRACK)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 3)
                self.state = 382
                self.match(FCCParser.DOT)
                self.state = 383
                self.match(FCCParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FCCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FCCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(FCCParser.COMMA)
            else:
                return self.getToken(FCCParser.COMMA, i)

        def getRuleIndex(self):
            return FCCParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = FCCParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.expression()
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 387
                self.match(FCCParser.COMMA)
                self.state = 388
                self.expression()
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FCCParser.IDENTIFIER, 0)

        def MAIN(self):
            return self.getToken(FCCParser.MAIN, 0)

        def literal(self):
            return self.getTypedRuleContext(FCCParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(FCCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(FCCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(FCCParser.RPAREN, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = FCCParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_primary)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(FCCParser.IDENTIFIER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(FCCParser.MAIN)
                pass
            elif token in [14, 15, 57, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.literal()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
                self.match(FCCParser.LPAREN)
                self.state = 398
                self.expression()
                self.state = 399
                self.match(FCCParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(FCCParser.INT_LITERAL, 0)

        def REAL_LITERAL(self):
            return self.getToken(FCCParser.REAL_LITERAL, 0)

        def HEX_LITERAL(self):
            return self.getToken(FCCParser.HEX_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(FCCParser.STRING_LITERAL, 0)

        def CHAR_LITERAL(self):
            return self.getToken(FCCParser.CHAR_LITERAL, 0)

        def TRUE(self):
            return self.getToken(FCCParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(FCCParser.FALSE, 0)

        def getRuleIndex(self):
            return FCCParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = FCCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8791026472627257344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






TK_AN_ARRAY = 1

TK_QUOTE = 2
TK_RIGHT_PAREN = 3
TK_NOT_EQUAL = 4
TK_LEFT_PAREN = 5
TK_PLUS = 6
TK_MULTIPLY = 7
TK_MINUS = 8
TK_COMMA = 9
TK_DIVIDE = 10
TK_DOT = 11
TK_ASSIGNMENT = 12
TK_RIGHT_BRACKET = 13
TK_LEFT_BRACKET = 14
TK_SEMICOLON = 15
TK_COLON = 16
TK_EQUAL = 17
TK_LESS_THAN = 18
TK_GREATER_THAN = 19
TK_LESS_EQUAL= 20
TK_GREATER_EQUAL = 21

TK_DO = 22
TK_CHAR = 23
TK_INTEGER = 24
TK_IF = 25
TK_CONSTANT = 26
TK_FOR = 27
TK_TO = 28
TK_DOWNTO = 29
TK_PROGRAM = 30
TK_BOOLEAN = 31
TK_VAR = 32
TK_UNTIL = 33
TK_FUNCTION = 34
TK_THEN = 35
TK_BEGIN = 36
TK_REPEAT = 37
TK_ELSE = 38
TK_NOT = 39
TK_END = 40
TK_MOD = 41
TK_WHILE = 42
TK_DIV = 43
TK_OR = 44
TK_AND = 45
TK_REAL = 46
TK_PROCEDURE = 47

TK_AN_INTEGER = 48
TK_A_REAL = 49
TK_A_CHAR = 50
TK_A_BOOL = 51
TK_IDENTIFIER = 52
TK_A_VAR = 53
TK_A_DIGIT = 54

TK_WRITE = 60

token_map = {
    TK_LESS_EQUAL: "TK_LESS_EQUAL",
    TK_GREATER_EQUAL: "TK_GREATER_EQUAL",
    TK_QUOTE: "TK_QUOTE",
    TK_RIGHT_PAREN: "TK_RIGHT_PAREN",
    TK_NOT_EQUAL: "TK_NOT_EQUAL",
    TK_LEFT_PAREN: "TK_LEFT_PAREN",
    TK_PLUS: "TK_PLUS",
    TK_MULTIPLY: "TK_MULTIPLY",
    TK_MINUS: "TK_MINUS",
    TK_COMMA: "TK_COMMA",
    TK_DIVIDE: "TK_DIVIDE",
    TK_DOT: "TK_DOT",
    TK_ASSIGNMENT: "TK_ASSIGNMENT",
    TK_RIGHT_BRACKET: "TK_RIGHT_BRACKET",
    TK_LEFT_BRACKET: "TK_LEFT_BRACKET",
    TK_SEMICOLON: "TK_SEMICOLON",
    TK_COLON: "TK_COLON",
    TK_EQUAL: "TK_EQUAL",
    TK_LESS_THAN: "TK_LESS_THAN",
    TK_GREATER_THAN: "TK_GREATER_THAN",
    TK_AND: "TK_AND",
    TK_REAL: "TK_REAL",
    TK_DO: "TK_DO",
    TK_CHAR: "TK_CHAR",
    TK_INTEGER: "TK_INTEGER",
    TK_IF: "TK_IF",
    TK_CONSTANT: "TK_CONSTANT",
    TK_FOR: "TK_FOR",
    TK_TO: "TK_TO",
    TK_DOWNTO: "TK_DOWNTO",
    TK_PROGRAM: "TK_PROGRAM",
    TK_BOOLEAN: "TK_BOOLEAN",
    TK_VAR: "TK_VAR",
    TK_UNTIL: "TK_UNTIL",
    TK_FUNCTION: "TK_FUNCTION",
    TK_THEN: "TK_THEN",
    TK_BEGIN: "TK_BEGIN",
    TK_REPEAT: "TK_REPEAT",
    TK_ELSE: "TK_ELSE",
    TK_NOT: "TK_NOT",
    TK_END: "TK_END",
    TK_MOD: "TK_MOD",
    TK_WHILE: "TK_WHILE",
    TK_DIV: "TK_DIV",
    TK_OR: "TK_OR",
    TK_PROCEDURE: "TK_PROCEDURE",
    TK_A_VAR: "TK_A_VAR",
    TK_A_DIGIT: "TK_A_DIGIT",
    TK_AN_INTEGER: "TK_AN_INTEGER",
    TK_A_REAL: "TK_A_REAL",
    TK_A_CHAR: "TK_A_CHAR",
    TK_A_BOOL: "TK_A_BOOL",
    TK_IDENTIFIER: "TK_IDENTIFIER",
    TK_AN_ARRAY: "TK_AN_ARRAY",
}
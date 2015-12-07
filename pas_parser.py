
from scanner import Scanner

reserved_words = {
    'program': 'TK_PROGRAM',
    'var': 'TK_VAR',
    'procedure': 'TK_PROCEDURE',
    'function': 'TK_FUNCTION',
    'const': 'TK_CONSTANT',
    'begin': 'TK_BEGIN',
    'end': 'TK_END',

    'if': 'TK_IF',
    'then': 'TK_THEN',
    'else': 'TK_ELSE',
    'for': 'TK_FOR',
    'while': 'TK_WHILE',
    'repeat': 'TK_REPEAT',
    'do': 'TK_DO',
    'to': 'TK_TO',
    'downto': 'TK_DOWNTO',
    'until': 'TK_UNTIL',
    'and': 'TK_AND',
    'or': 'TK_OR',
    'not': 'TK_NOT',
    'div': 'TK_DIV',
    'mod': 'TK_MOD',
    'real': 'TK_REAL',
    'integer': 'TK_INTEGER',
    'bool': 'TK_BOOLEAN',
    'char': 'TK_CHAR',
}

SYMBOLS = {
    "+": "TK_PLUS",
    "-": "TK_MINUS",
    "*": "TK_MULTIPLY",
    "/": "TK_DIVIDE",

    ":=": "TK_ASSIGNMENT",
    ";": "TK_SEMICOLON",
    ":": "TK_COLON",
    ",": "TK_COMMA",

    "=": "TK_EQUAL",
    "<>": "TK_NOT_EQUAL",
    "<": "TK_LESS_THAN",
    "<=": "TK_LESS_EQUAL",
    ">": "TK_GREATER_THAN",
    ">=": "TK_GREATER_EQUAL",

    "(": "TK_LEFT_PAREN",
    ")": "TK_RIGHT_PAREN",
    "[": "TK_LEFT_BRACKET",
    "]": "TK_RIGHT_BRACKET",

    ".": "TK_DOT"
}

double_symbol = [
    "<",
    ">",
    ":"
]

def get_token_list():
    return [token for key, token in reserved_words.items()]

TK_AND = 1
TK_TREAL = 2
TK_DO = 3
TK_TCHAR = 4
TK_IF = 5
TK_END = 6
TK_FOR = 7
TK_TO = 8
TK_DOWNTO = 9
TK_PROGRAM = 10
TK_VAR = 11
TK_UNTIL = 12
TK_FUNCTION = 13
TK_THEN = 14
TK_BEGIN = 15
TK_REPEAT = 16
TK_TSTRING = 17
TK_ELSE = 18
TK_NOT = 19
TK_TINTEGER = 20
TK_MOD = 21
TK_WHILE = 22
TK_DIV = 23
TK_OR = 24
TK_PROCEDURE = 25

class Parser(object):
    _symbols = dict(SYMBOLS)
    _reserved_words = dict(reserved_words)

    def __init__(self, filename):
        self.scanner = Scanner(filename)
        self.current_token = None
        self.current_word = None

    @staticmethod
    def _is_valid_identifier(var_name):
        if not var_name:
            return False
        return var_name[0].isalpha() and var_name.isalnum()

    def get_next_token(self):
        self.current_word = self.scanner.get_word().lower()
        self.current_token = self._lookup_token(self.current_word)

        return self.current_token

    def _lookup_token(self, word):
        if not word:
            return None

        token = self._get_double_symbol(word)
        if token:
            return token

        token = self._symbols.get(word, None) or self._reserved_words.get(word, None)
        if token:
            return token

        if word.isdigit():
            return "TK_DIGIT"

        if self._is_valid_identifier(word):
            return "TK_IDENTIFIER"

        return ''

    def _get_double_symbol(self, word):
        if word in double_symbol:
            peek = self.scanner.peek_char()
            if str(word+peek) in self._symbols:
                self.scanner.get_word()
                return self._symbols.get(str(word+peek))
            else:
                return self._symbols.get(word)
        return None

    def is_done(self):
        return self.scanner.eof
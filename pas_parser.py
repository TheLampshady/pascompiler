from scanner import Scanner
from token_lookup import *

reserved_words = {
    'program': TK_PROGRAM,
    'var': TK_VAR,
    'procedure': TK_PROCEDURE,
    'function': TK_FUNCTION,
    'const': TK_CONSTANT,
    'begin': TK_BEGIN,
    'end': TK_END,

    'if': TK_IF,
    'then': TK_THEN,
    'else': TK_ELSE,
    'for': TK_FOR,
    'while': TK_WHILE,
    'repeat': TK_REPEAT,
    'do': TK_DO,
    'to': TK_TO,
    'downto': TK_DOWNTO,
    'until': TK_UNTIL,
    'and': TK_AND,
    'or': TK_OR,
    'not': TK_NOT,
    'div': TK_DIV,
    'mod': TK_MOD,
    'real': TK_REAL,
    'integer': TK_INTEGER,
    'bool': TK_BOOLEAN,
    'char': TK_CHAR,
}

SYMBOLS = {
    "+": TK_PLUS,
    "-": TK_MINUS,
    "*": TK_MULTIPLY,
    "/": TK_DIVIDE,

    ":=": TK_ASSIGNMENT,
    ";": TK_SEMICOLON,
    ":": TK_COLON,
    ",": TK_COMMA,

    "=": TK_EQUAL,
    "<>": TK_NOT_EQUAL,
    "<": TK_LESS_THAN,
    "<=": TK_LESS_EQUAL,
    ">": TK_GREATER_THAN,
    ">=": TK_GREATER_EQUAL,

    "(": TK_LEFT_PAREN,
    ")": TK_RIGHT_PAREN,
    "[": TK_LEFT_BRACKET,
    "]": TK_RIGHT_BRACKET,

    ".": TK_DOT,
    "'": TK_QUOTE
}

double_symbol = [
    "<",
    ">",
    ":"
]


def get_token_list():
    return [token for key, token in reserved_words.items()]


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
            try:
                int(word)
                return TK_AN_INTEGER
            except ValueError:
                return TK_A_REAL

        if word in ['true', 'false']:
            return TK_A_BOOL

        if self._is_valid_identifier(word):
            return TK_IDENTIFIER

        return ''

    def _get_double_symbol(self, word):
        if word in double_symbol:
            peek = self.scanner.peek_char()
            new_word = str(word+peek)
            if new_word in self._symbols:
                self.scanner.get_word()
                self.current_word = new_word
                return self._symbols.get(str(word+peek))
            else:
                return self._symbols.get(word)
        return None

    def is_done(self):
        return self.scanner.eof

    def print_token(self, token=None):
        if not token:
            token = self.current_token
        return token_map.get(token, "Unknown")
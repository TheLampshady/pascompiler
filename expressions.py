from token_lookup import *
from evaluate import *


def evaluate_array_expression(token_parser):
    while token_parser.get_next_token():
        token = token_parser.current_token
        print "Array Token: '%s' % token"

        if token == TK_RIGHT_BRACKET:
            return 1, 3
        elif token == TK_SEMICOLON:
            return None


def evaluate_expression(token_parser, symbol_table):
    allowed = [TK_PLUS, TK_MINUS, TK_LESS_EQUAL, TK_LESS_THAN, TK_GREATER_EQUAL, TK_GREATER_THAN]
    result = evaluate_expression_t(token_parser, symbol_table)
    while token_parser.current_token in allowed:

        operation = token_parser.current_token
        token_parser.get_next_token()
        result2 = evaluate_expression_t(token_parser, symbol_table)

        if operation in [TK_PLUS, TK_MINUS]:
            result = arithmetic_operation(result, result2, operation)
        else:
            result = comparison_operation(result, result2, operation)

    return result


def evaluate_expression_t(token_parser, symbol_table):
    allowed = [TK_MULTIPLY, TK_DIVIDE, TK_AND, TK_OR]
    result = evaluate_expression_f(token_parser, symbol_table)
    while token_parser.current_token in allowed:
        operation = token_parser.current_token

        token_parser.get_next_token()
        result2 = evaluate_expression_f(token_parser, symbol_table)

        if operation in [TK_MULTIPLY, TK_DIVIDE]:
            result = arithmetic_operation(result, result2, operation)
        else:
            result = bitwise_operation(result, result2, operation)

    return result


def evaluate_expression_f(token_parser, symbol_table):
    """

    :param token_parser:
    :param symbol_table: Table of avlailbe symbols for lookups
    :return:
    """
    if token_parser.current_token == TK_LEFT_PAREN:
        token_parser.get_next_token()
        result = evaluate_expression(token_parser, symbol_table)
        if token_parser.current_token != TK_RIGHT_PAREN:
            raise ValueError("Invalid Token '%s': Expecting ')'" % token_parser.print_token())

    # --------- IDS ------------
    elif token_parser.current_token == TK_IDENTIFIER:
        lookup = symbol_table.get(token_parser.current_word)
        if not lookup:
            raise ValueError("Invalid Variable: '%s'" % token_parser.print_token())
        value = lookup.get('value')
        if value is None:
            raise ValueError("Variable Not Initialized: '%s'" % token_parser.current_word)
        result = (lookup['data_type'], value)

    # --------- Literals ---------
    elif token_parser.current_token == TK_A_BOOL:
        value = bool(token_parser.current_word == 'true')
        result = TK_A_BOOL, value
        print "push %s" % value
    elif token_parser.current_token == TK_QUOTE:
        value = handle_char(token_parser)
        result = TK_A_CHAR, value
        print "push '%s'" % value
    elif token_parser.current_token == TK_AN_INTEGER:
        value = int(token_parser.current_word)
        result = TK_AN_INTEGER, value
        print "push %s" % value
    elif token_parser.current_token == TK_A_REAL:
        value = float(token_parser.current_word)
        result = 'TK_A_REAL', float(token_parser.current_word)
        print "push %s" % value

    elif token_parser.current_token == TK_NOT:
        token_parser.get_next_token()
        result = evaluate_expression_f(token_parser)
        if result[0] not in [TK_AN_INTEGER, TK_A_BOOL]:
            raise TypeError("Invalid Type for Not Operation: '%s'" % result[0])
        print "not"
    elif token_parser.current_token == TK_PLUS:
        token_parser.get_next_token()
        result = evaluate_expression_f(token_parser)
        if result[0] not in [TK_AN_INTEGER, TK_A_REAL]:
            raise TypeError("Invalid Type for Plus Operation: '%s'" % result[0])
    elif token_parser.current_token == TK_MINUS:
        token_parser.get_next_token()
        result = evaluate_expression_f(token_parser)
        if result[0] not in [TK_AN_INTEGER, TK_A_REAL]:
            raise TypeError("Invalid Type for Minus Operation: '%s'" % result[0])
        result = (result[0], result[1]*-1)
        print "neg"
    else:
        raise ValueError("Invalid Variable: '%s'" % token_parser.print_token())

    token_parser.get_next_token()
    return result


def handle_char(token_parser):
    token_parser.get_next_token()
    if len(token_parser.current_word) > 1:
        raise ValueError("Invalid Token '%s': Expecting '\''" % token_parser.current_word[1])
    result = token_parser.current_word
    token_parser.get_next_token()
    if token_parser.current_token != TK_QUOTE:
        raise ValueError("Invalid Token '%s': Expecting '\''" % token_parser.print_token())
    return result
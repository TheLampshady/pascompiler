
def evaluate_array_expression(token_parser):
    while token_parser.get_next_token():
        token = token_parser.current_token
        print "Array Token: '%s' % token"

        if token == "TK_RIGHT_BRACKET":
            return 1, 3
        elif token == 'TK_SEMICOLON':
            return None


def evaluate_expression(token_parser, symbol_table):
    result = evaluate_expression_t(token_parser, symbol_table)
    while token_parser.current_token == 'TK_PLUS' or\
            token_parser.current_token == 'TK_MINUS':

        operation = token_parser.current_token
        token_parser.get_next_token()
        result2 = evaluate_expression_t(token_parser, symbol_table)

        if operation == 'TK_PLUS':
            result = add_operation(result, result2)
        else:
            result = minus_operation(result, result2)

    return result


def evaluate_expression_t(token_parser, symbol_table):
    result = evaluate_expression_f(token_parser, symbol_table)
    while token_parser.current_token == 'TK_MULTIPLY' or \
            token_parser.current_token == 'TK_DIVIDE':
        operation = token_parser.current_token

        token_parser.get_next_token()
        result2 = evaluate_expression_f(token_parser, symbol_table)

        if operation == 'TK_MULTIPLY':
            result = mul_operation(result, result2)
        else:
            result = div_operation(result, result2)

    return result

def evaluate_expression_f(token_parser, symbol_table):
    """

    :param token_parser:
    :param symbol_table: Table of avlailbe symbols for lookups
    :return:
    """
    if token_parser.current_token == "TK_LEFT_PAREN":
        token_parser.get_next_token()
        result = evaluate_expression(token_parser, symbol_table)
        if token_parser.current_token != "TK_RIGHT_PAREN":
            raise ValueError("Invalid Token '%s': Expecting ')'" % token_parser.current_token)

    # --------- IDS ------------
    elif token_parser.current_token == 'TK_IDENTIFIER':
        lookup = symbol_table.get(token_parser.current_word)
        if not lookup:
            raise ValueError("Invalid Variable: '%s'" % token_parser.current_token)
        value = lookup.get('value')
        if value is None:
            raise ValueError("Variable Not Initialized: '%s'" % token_parser.current_word)
        result = (lookup['data_type'], value)

    # --------- Literals ---------
    elif token_parser.current_token == 'TK_A_BOOLEAN':
        result = 'TK_A_BOOLEAN', token_parser.current_word
    elif token_parser.current_token == "TK_QUOTE":
        result = 'TK_A_CHAR', handle_char(token_parser)
    elif token_parser.current_token == 'TK_AN_INTEGER':
        result = 'TK_AN_INTEGER', int(token_parser.current_word)
    elif token_parser.current_token == 'TK_A_REAL':
        result = 'TK_A_REAL', float(token_parser.current_word)

    elif token_parser.current_token == 'TK_NOT':
        # TODO Flip sign
        token_parser.get_next_token()
        result = evaluate_expression_f(token_parser)
    elif token_parser.current_token == 'TK_PLUS':
        token_parser.get_next_token()
        result = evaluate_expression_f(token_parser)
    elif token_parser.current_token == 'TK_MIUNS':
        # TODO Flip sign
        token_parser.get_next_token()
        result = evaluate_expression_f(token_parser)
    else:
        raise ValueError("Invalid Variable: '%s'" % token_parser.current_token)

    token_parser.get_next_token()
    return result

def handle_char(token_parser):
    token_parser.get_next_token()
    if len(token_parser.current_token) > 1:
        raise ValueError("Invalid Token '%s': Expecting '\''" % token_parser.current_token[1])
    result = token_parser.current_word
    token_parser.get_next_token()
    if token_parser.current_token != "TK_QUOTE":
        raise ValueError("Invalid Token '%s': Expecting '\''" % token_parser.current_token)
    return result

def add_operation(result, result2):
    print "ADDING: %s|%s" % (str(result), str(result2))
    return result[0], result[1] + result2[1]

def minus_operation(result, result2):
    print "SUBTRACTING: %s|%s" % (str(result), str(result2))
    return result2[0], result[1] - result2

def mul_operation(result, result2):
    print "MULTIPLYING: %s|%s" % (str(result), str(result2))
    return result[0], result[1] * result2[1]

def div_operation(result, result2):
    print "DIVIDING: %s|%s" % (str(result), str(result2))
    return result2[0], result[1] / result2[1]

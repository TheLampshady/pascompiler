from evaluate import *

type_size = {
    'TK_A_BOOLEAN': 1,
    'TK_A_CHAR': 1,
    'TK_AN_INTEGER': 4,
    'TK_A_REAL': 8,
}


def get_identifier_props(token_parser):
    type_token = token_parser.get_next_token()

    if type_token == 'TK_BOOLEAN':
        token_prop = {
            'var_type': "TK_A_VAR",
            'data_type': 'TK_A_BOOLEAN',
            'address': 0,
            'size': type_size['TK_A_BOOLEAN']
        }
    elif type_token == 'TK_CHAR':
        token_prop = {
            'var_type': "TK_A_VAR",
            'data_type': 'TK_A_CHAR',
            'address': 0,
            'size': type_size['TK_A_CHAR']
        }
    elif type_token == 'TK_INTEGER':
        token_prop = {
            'var': True,
            'data_type': 'TK_AN_INTEGER',
            'address': 0,
            'size': type_size['TK_AN_INTEGER']
        }
    elif type_token == 'TK_REAL':
        token_prop ={
            'var_type': "TK_A_VAR",
            'data_type': 'TK_A_REAL',
            'address': 0,
            'size': type_size['TK_A_REAL']
        }
    else:
        raise ValueError("Invalid Data Type: '%s'" % type_token)

    next_token = token_parser.get_next_token()
    if next_token == "TK_LEFT_BRACKET":
        array_props = {'var_type': "TK_AN_ARRAY"}
        result = evaluate_array_expression(token_parser)

        if not result:
            raise ValueError("Invalid Expression in Array Index")

        array_props['index_type'] = 'TK_INTEGER'
        array_props['low'] = result[0]
        array_props['high'] = result[1]
        array_props['size'] = type_size['size'] * (result[1] - result[0])
        token_prop.update(array_props)

    return token_prop





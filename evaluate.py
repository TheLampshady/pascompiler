from token_lookup import *



def add_operation(result, result2):
    data_type = handle_arithmetic_data_type(result[0], result2[0])
    instruction = "add" if data_type == TK_AN_INTEGER else "fadd"
    print instruction
    return data_type, result[1] + result2[1]


def minus_operation(result, result2):
    data_type = handle_arithmetic_data_type(result[0], result2[0])
    instruction = "sub" if data_type == TK_AN_INTEGER else "fsub"
    print instruction
    return data_type, result[1] - result2


def mul_operation(result, result2):
    data_type = handle_arithmetic_data_type(result[0], result2[0])
    instruction = "mul" if data_type == TK_AN_INTEGER else "fmul"
    print instruction
    return data_type, result[1] * result2[1]


def div_operation(result, result2):
    data_type = handle_arithmetic_data_type(result[0], result2[0])
    instruction = "div" if data_type == TK_AN_INTEGER else "fdiv"
    print instruction
    return data_type, result[1] / result2[1]


def and_operation(result, result2):
    data_type = handle_bitwise_data_type(result[0], result2[0])
    instruction = "band" if data_type == TK_AN_INTEGER else "and"
    print instruction
    return data_type, result[1] & result2[1]


def or_operation(result, result2):
    data_type = handle_bitwise_data_type(result[0], result2[0])
    instruction = "bor" if data_type == TK_AN_INTEGER else "or"
    print instruction
    return data_type, result[1] | result2[1]


def handle_arithmetic_data_type(type1, type2):
    allowed = [TK_AN_INTEGER, TK_A_REAL]
    if type1 not in allowed or type2 not in allowed:
        raise TypeError("Invalid Type for Arithmetic Operation: '%s'" %
                        token_map.get(type1))

    return handle_int_real_conversion(type1, type2)


def handle_bitwise_data_type(type1, type2):
    allowed = [TK_AN_INTEGER, TK_A_BOOL]
    if type1 not in allowed or type2 not in allowed:
        raise TypeError("Invalid Type for Bitwise Operation: '%s'" %
                        token_map.get(type1))

    return handle_int_real_conversion(type1, type2)


def handle_comparison_data_type(type1, type2):
    allowed = [TK_AN_INTEGER, TK_A_BOOL, TK_A_CHAR, TK_A_REAL]
    if type1 not in allowed or type2 not in allowed:
        raise TypeError("Invalid Type for Bitwise Operation: '%s'" % type1)

    return handle_int_real_conversion(type1, type2)


def handle_int_real_conversion(type1, type2, assignment=False):
    if type1 == type2:
        return type1

    if type1 == TK_AN_INTEGER:
        if type2 == TK_A_REAL and not assignment:
            print "exch"
            print "conv float"
            print "exch"
        else:
            raise TypeError("Cannot Operate Integer with '%s" %
                            token_map.get(type2))

    elif type2 == TK_A_REAL:
        if type2 == TK_AN_INTEGER:
            print "conv float"
        else:
            raise TypeError("Cannot Operate Real with '%s" %
                            token_map.get(type2))
    else:
        raise TypeError("Cannot Operate '%s' with '%s" %
                        (token_map.get(type1), token_map.get(type2)))

    return TK_A_REAL



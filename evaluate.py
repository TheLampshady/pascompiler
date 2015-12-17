from token_lookup import *
import operator

INSTRUCTIONS = {
    TK_PLUS: "add",
    TK_MINUS: "sub",
    TK_MULTIPLY: "mul",
    TK_DIVIDE: "div",
    TK_AND: "and",
    TK_OR: "or",
    TK_EQUAL: "eq",
    TK_NOT_EQUAL: "ne",
    TK_LESS_THAN: "lss",
    TK_LESS_EQUAL: "lse",
    TK_GREATER_THAN: "gtr",
    TK_GREATER_EQUAL: "gte",
}

OPERATOR = {
    TK_PLUS: operator.add,
    TK_MINUS: operator.sub,
    TK_MULTIPLY: operator.mul,
    TK_DIVIDE: operator.div,
    TK_AND: operator.and_,
    TK_OR: operator.or_,
    TK_EQUAL: operator.eq,
    TK_NOT_EQUAL: operator.ne,
    TK_LESS_THAN: operator.lt,
    TK_LESS_EQUAL: operator.le,
    TK_GREATER_THAN: operator.gt,
    TK_GREATER_EQUAL: operator.ge,
}


def arithmetic_operation(result, result2, operation):
    data_type = handle_arithmetic_data_type(result[0], result2[0])
    instruction = INSTRUCTIONS[operation]
    print "f%s" % instruction if data_type == TK_A_REAL else instruction
    return data_type, OPERATOR.get(operation)(result[1], result2[1])


def bitwise_operation(result, result2, operation):
    data_type = handle_bitwise_data_type(result[0], result2[0])
    instruction = INSTRUCTIONS[operation]
    print "b%s" % instruction if data_type == TK_AN_INTEGER else instruction
    return data_type, OPERATOR.get(operation)(result[1], result2[1])


def comparison_operation(result, result2, operation):
    data_type = handle_comparison_data_type(result[0], result2[0])
    instruction = INSTRUCTIONS[operation]
    print "f%s" % instruction if data_type == TK_A_REAL else instruction
    return data_type, OPERATOR.get(operation)(result[1], result2[1])


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

    handle_int_real_conversion(type1, type2)
    return TK_A_BOOL


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

    elif type1 == TK_A_REAL:
        if type2 == TK_AN_INTEGER:
            print "conv float"
        else:
            raise TypeError("Cannot Operate Real with '%s" %
                            token_map.get(type2))
    else:
        raise TypeError("Cannot Operate '%s' with '%s" %
                        (token_map.get(type1), token_map.get(type2)))

    return TK_A_REAL



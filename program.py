from pas_parser import Parser
from variable_functions import *


class Program(object):
    def __init__(self, filename):
        self.pascal_parser = Parser(filename)
        self.symbol_table = dict()
        self.symbol_address = 0

    def run(self, mode=1):
        token = self.pascal_parser.get_next_token()
        if token == "TK_PROGRAM":
            self.run_program_name()

        if self.run_program() != "TK_DOT":
            raise ValueError("Invalid End. Requires period.")

        self.run_comments()

    def run_program_name(self):
        token = "None"
        while token is not None and token != "TK_SEMICOLON":
            token = self.pascal_parser.get_next_token()
            #print "PROGRAM: %s" % self.pascal_parser.current_word

    def run_program(self):
        function_mode = None
        while not self.pascal_parser.scanner.eof:
            token = self.pascal_parser.get_next_token()

            if token == "TK_VAR":
                self.pascal_parser.get_next_token()
                function_mode = self.declare_variables

            if token == "TK_CONSTANT":
                function_mode = self.run_default
            if token == "TK_FUNCTION":
                function_mode = self.run_default
            if token == "TK_PROCEDURE":
                function_mode = self.run_default

            if token == "TK_BEGIN":
                self.run_begin()
                token = self.pascal_parser.get_next_token()
                return token

            if not function_mode:
                raise ValueError("Invalid Token: '%s'" % token)

            function_mode()

    def run_default(self):
        token = "None"
        while token and token != "TK_SEMICOLON":
            token = self.pascal_parser.get_next_token()
            print "DEFAULT: %s" % token

        return

    def run_begin(self):
        token = self.pascal_parser.get_next_token()
        while token and token != "TK_END":
            word = self.pascal_parser.current_word
            if token == 'TK_IDENTIFIER':
                assignment = self.symbol_table.get(word, None)
                if not assignment:
                    raise ValueError("Identifier does not exist: '%s'" % word)
                if self.pascal_parser.get_next_token() != "TK_ASSIGNMENT":
                    raise ValueError("Expected Assignment: Got %s" %
                                     self.pascal_parser.current_word)

                self.pascal_parser.get_next_token()
                result = evaluate_expression(self.pascal_parser, self.symbol_table)
                assignment['value'] = result[1]
                if self.pascal_parser.current_token != "TK_SEMICOLON":
                    raise ValueError("Invalid Expression at '%s'" % self.pascal_parser.current_word)
            else:
                print "Operation '%s': Not supported"
                while self.pascal_parser.get_next_token() and \
                    self.pascal_parser.current_token != "TK_SEMICOLON": pass

            token = self.pascal_parser.get_next_token()

        return

    def run_comments(self):
        while not self.pascal_parser.scanner.eof:
            token = self.pascal_parser.get_next_token()
            print "COMMENTS: %s" % token

    def declare_variables(self):
        var_list = self.get_var_list()

        result_props = get_identifier_props(self.pascal_parser)
        for var_name in var_list:
            if var_name in self.symbol_table:
                raise ValueError("Identifier already exists: '%s'" % var_name)
            var_entry = {var_name: dict(result_props)}
            var_entry[var_name]['address'] = self.symbol_address
            var_entry[var_name]['var_name'] = var_name
            self.symbol_address += var_entry[var_name]['size']
            self.symbol_table.update(var_entry)

    def get_var_list(self):
        var_list = list()
        token = self.pascal_parser.current_token
        while True:
            word = self.pascal_parser.current_word
            if token != 'TK_IDENTIFIER':
                raise ValueError("Unexpected Identifier, got '%s'" % word)

            var_list.append(word)

            token = self.pascal_parser.get_next_token()
            if token == 'TK_COLON':
                return var_list
            elif token != 'TK_COMMA':
                word = self.pascal_parser.current_word
                raise ValueError("Invalid Token: '%s'. Expected comma or colon" % word)

            token = self.pascal_parser.get_next_token()

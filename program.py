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
            raise("Invalid End. Requires period.")

        self.run_comments()

    def run_program_name(self):
        token = "None"
        while token is not None and token != "TK_SEMICOLON":
            token = self.pascal_parser.get_next_token()
            print "PROGRAM: %s" % self.pascal_parser.current_word

    def run_program(self):
        function_mode = None
        while not self.pascal_parser.scanner.eof:
            token = self.pascal_parser.get_next_token()

            if token == "TK_VAR":
                function_mode = self.declare_variables

            if token == "TK_CONSTANT":
                function_mode = self.run_var
            if token == "TK_FUNCTION":
                function_mode = self.run_var
            if token == "TK_PROCEDURE":
                function_mode = self.run_var

            if token == "TK_BEGIN":
                self.run_begin()
                token = self.pascal_parser.get_next_token()
                return token

            if not function_mode:
                raise ValueError("Invalid Token: '%s'" % token)

            function_mode()

    def run_var(self):
        token = "None"
        while token and token != "TK_SEMICOLON":
            token = self.pascal_parser.get_next_token()
            print "VAR: %s" % token

        return

    def run_const(self):
        token = "None"
        while token and token != "TK_SEMICOLON":
            token = self.pascal_parser.get_next_token()
            print "CONST: %s" % token

        return

    def run_begin(self):
        token = "None"
        while token and token != "TK_END":
            token = self.pascal_parser.get_next_token()
            print "BEGIN: %s" % token

        return

    def run_comments(self):
        while not self.pascal_parser.scanner.eof:
            token = self.pascal_parser.get_next_token()
            print "COMMENTS: %s" % token

    def declare_variables(self):
        var_list = list()
        while True:
            token = self.pascal_parser.get_next_token()
            word = self.pascal_parser.current_word
            if token != 'TK_IDENTIFIER':
                raise ValueError("Expected Identifier, got '%s'" % word)

            if word in self.symbol_table:
                raise ValueError("Identifier already exists: '%s'" % word)

            var_list.append(word)

            token = self.pascal_parser.get_next_token()
            if token == 'TK_COLON':
                break
            elif token != 'TK_COMMA':
                ValueError("Invalid Token: '%s'. Expected comma of colon" % word)

        result_props = get_identifier_props(self.pascal_parser)
        for var_name in var_list:
            var_entry = {var_name: dict(result_props)}
            var_entry[var_name]['address'] = self.symbol_address
            self.symbol_address += var_entry[var_name]['size']
            self.symbol_table.update(var_entry)


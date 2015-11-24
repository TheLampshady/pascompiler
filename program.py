from pas_parser import Parser


class Program(object):

    def __init__(self, filename):
        self.pascal_parser = Parser(filename)

    def run(self, mode=1):
        token = self.pascal_parser.get_token()
        if token == "TK_PROGRAM":
            self.run_program_name()

        if self.run_program() != "TK_DOT":
            raise("Invalid End. Requires period.")

        self.run_comments()

    def run_program_name(self):
        token = "None"
        while token and token != "TK_SEMICOLON":
            token = self.pascal_parser.get_token()
            print "PROGRAM: %s" % token

    def run_program(self):
        function_mode = None
        while not self.pascal_parser.scanner.eof:
            token = self.pascal_parser.get_token()

            if token == "TK_VAR":
                function_mode = self.run_var

            if token == "TK_CONSTANT":
                function_mode = self.run_var
            if token == "TK_FUNCTION":
                function_mode = self.run_var
            if token == "TK_PROCEDURE":
                function_mode = self.run_var

            if token == "TK_BEGIN":
                self.run_begin()
                token = self.pascal_parser.get_token()
                return token

            if not function_mode:
                raise ValueError("Invalid Token: '%s'" % token)

            function_mode()

    def run_var(self):
        token = "None"
        while token and token != "TK_SEMICOLON":
            token = self.pascal_parser.get_token()
            print "VAR: %s" % token

        return

    def run_const(self):
        token = "None"
        while token and token != "TK_SEMICOLON":
            token = self.pascal_parser.get_token()
            print "CONST: %s" % token

        return

    def run_begin(self):
        token = "None"
        while token and token != "TK_END":
            token = self.pascal_parser.get_token()
            print "BEGIN: %s" % token

        return

    def run_comments(self):
        while not self.pascal_parser.scanner.eof:
            token = self.pascal_parser.get_token()
            print "COMMENTS: %s" % token

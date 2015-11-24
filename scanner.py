
double_symbol = [
    "<",
    ">",
    ":"
]

class Scanner(object):

    whitespace = [' ', '\n']

    def __init__(self, filename):
        #TODO Try
        self.file = open(filename, 'r')

        self.ch = self.get_any_char()
        self.eof = bool(self.ch == '')

    def get_any_char(self):
        ch = self.file.read(1)
        while ch in self.whitespace:
            ch = self.file.read(1)
        return ch

    def peek_char(self):
        return self.ch or ' '

    def get_char(self):
        ch = self.file.read(1)
        if ch == '':
            self.eof = True
            raise EOFError("End of File.")
        return None if ch in self.whitespace else ch

    def get_word(self):
        word = ''

        try:
            if not self.ch:
                self.ch = self.get_any_char()
        except EOFError:
            return None

        while True:
            word += self.ch
            try:
                self.ch = self.get_char()
            except EOFError:
                return word
            if not self.ch or not self._is_valid_word(word):
                break

        return word

    def _is_valid_word(self, word):
        if self.ch.isalnum():
            return True

        if word.isdigit() and self.ch == ".":
            return True

        return False



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

    def get_char(self):
        ch = self.file.read(1)
        if ch == '':
            self.eof = True
            raise EOFError("End of File.")
        return None if ch in self.whitespace else ch

    def get_word(self):
        word = ''

        while True:
            word += self.ch
            try:
                self.ch = self.get_char()
            except EOFError:
                return word
            if not self.ch or not self.ch.isalnum():
                break
        if not self.ch:
            self.ch = self.get_any_char()
        return word

    # @staticmethod
    # def is_word(word):
    #     if not len(word):
    #         return True
    #     if len(word) == 1:
    #         if not word.isalpha():
    #             return False
    #
    #     elif not word.isalnum():
    #         return False
    #
    #     return True


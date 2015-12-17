from tests.base import TestBase
from pas_parser import Parser
class TestParser(TestBase):


    def test_real_token(self):
        file_name = "tests/mock_pas/reals.pas"
        pascal_parser = Parser(file_name)
        pascal_parser.get_next_token()
        pascal_parser.is_real()
        self.assertEquals(pascal_parser.current_word, '1.75')

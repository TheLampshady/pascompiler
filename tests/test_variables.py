from tests.base import TestBase
from pascal.program import Program

class TestVariables(TestBase):

    def test_pass_valid_var(self):
        file_name = "tests/mock_pas/all_var.pas"
        pascal_program = Program(file_name)
        pascal_program.run()

        self.assertEqual(len(pascal_program.symbol_table), 7)
        self.assertEqual(pascal_program.symbol_address, 23)

    def test_pass_assign(self):
        file_name = "tests/mock_pas/variables.pas"
        pascal_program = Program(file_name)
        pascal_program.run()

from tests.base import TestBase
from program import Program


class TestExpressions(TestBase):

    def test_pass_valid_var(self):
        file_name = "tests/mock_pas/math_complex.pas"
        pascal_program = Program(file_name)
        pascal_program.run()
        lookup_one = pascal_program.symbol_table.get('num1', None)
        lookup_mult = pascal_program.symbol_table.get('num2', None)
        lookup_paren = pascal_program.symbol_table.get('num3', None)
        lookup_no_space = pascal_program.symbol_table.get('num4', None)

        self.assertEqual(lookup_one.get('value', None), 5)
        self.assertEqual(lookup_mult.get('value', None), 7)
        self.assertEqual(lookup_paren.get('value', None), 9)
        self.assertEqual(lookup_no_space.get('value', None), 9)

    def test_pass_valid_assign(self):
        file_name = "tests/mock_pas/add_assign.pas"
        pascal_program = Program(file_name)
        pascal_program.run()
        lookup_one = pascal_program.symbol_table.get('num1', None)
        lookup_two = pascal_program.symbol_table.get('num2', None)
        lookup_sum = pascal_program.symbol_table.get('sum', None)

        self.assertEqual(lookup_one.get('value', None), 1)
        self.assertEqual(lookup_two.get('value', None), 5)
        self.assertEqual(lookup_sum.get('value', None), 6)

    def test_invalid_expression(self):
        file_name = "tests/mock_pas/invalid_exp.pas"
        pascal_program = Program(file_name)
        with self.assertRaises(Exception) as context:
            pascal_program.run()

            self.assertTrue('Invalid Expression' in context.exception)




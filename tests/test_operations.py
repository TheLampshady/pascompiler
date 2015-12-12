from tests.base import TestBase
from program import Program


class TestExpressions(TestBase):

    def test_pass_valid_var(self):
        file_name = "tests/mock_pas/bitwise_assign.pas"
        pascal_program = Program(file_name)
        pascal_program.run()
        lookup_int1 = pascal_program.symbol_table.get('num1', None)
        lookup_int2 = pascal_program.symbol_table.get('num2', None)
        lookup_bool1 = pascal_program.symbol_table.get('bool1', None)
        lookup_bool2 = pascal_program.symbol_table.get('bool2', None)

        self.assertEqual(lookup_int1.get('value', None), 0)
        self.assertEqual(lookup_int2.get('value', None), 7)
        self.assertFalse(lookup_bool1.get('value', True))
        self.assertTrue(lookup_bool2.get('value', False))

    def test_pass_valid_var(self):
        file_name = "tests/mock_pas/type_error.pas"
        pascal_program = Program(file_name)

        self.assertRaises(TypeError, pascal_program.run)

    # def test_pass_valid_assign(self):
    #     file_name = "tests/mock_pas/compare_assign.pas"
    #     pascal_program = Program(file_name)
    #     pascal_program.run()
    #     lookup_int1 = pascal_program.symbol_table.get('num1', None)
    #     lookup_int2 = pascal_program.symbol_table.get('num2', None)
    #     lookup_char1 = pascal_program.symbol_table.get('char1', None)
    #     lookup_char2 = pascal_program.symbol_table.get('char2', None)
    #
    #     self.assertEqual(lookup_int1.get('value', None), 5)
    #     self.assertEqual(lookup_int2.get('value', None), 5)
    #     self.assertEqual(lookup_char1.get('value', None), 7)
    #     self.assertEqual(lookup_char2.get('value', None), 7)
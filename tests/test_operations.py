from tests.base import TestBase
from pascal.program import Program


class TestOperations(TestBase):

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

    def test_pass_invalid_var(self):
        file_name = "tests/mock_pas/type_error.pas"
        pascal_program = Program(file_name)

        self.assertRaises(TypeError, pascal_program.run)

    def test_pass_valid_compare(self):
        file_name = "tests/mock_pas/compare_assign.pas"
        pascal_program = Program(file_name)
        pascal_program.run()
        lookup_bool1 = pascal_program.symbol_table.get('bool1', None)
        lookup_bool2 = pascal_program.symbol_table.get('bool2', None)
        lookup_bool3 = pascal_program.symbol_table.get('bool3', None)

        self.assertFalse(lookup_bool1.get('value', None))
        self.assertTrue(lookup_bool2.get('value', None))
        self.assertTrue(lookup_bool3.get('value', None))

    def test_pass_valid_real_operation(self):
        file_name = "tests/mock_pas/math_real.pas"
        pascal_program = Program(file_name)
        pascal_program.run()
        lookup_one = pascal_program.symbol_table.get('real1', None)
        lookup_two = pascal_program.symbol_table.get('real2', None)

        self.assertEqual(lookup_one.get('value', None), 5.5)
        self.assertEqual(lookup_two.get('value', None), 3.2)

    def test_pass_valid_real_int_convert(self):
        file_name = "tests/mock_pas/math_convert.pas"
        pascal_program = Program(file_name)
        pascal_program.run()
        lookup_one = pascal_program.symbol_table.get('real1', None)
        lookup_two = pascal_program.symbol_table.get('real2', None)

        self.assertEqual(lookup_one.get('value', None), 8.5)
        self.assertEqual(lookup_two.get('value', None), 7.5)
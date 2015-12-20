from tests.base import TestBase
from pascal.program import Program


class TestCommands(TestBase):

    def test_pass_valid_var(self):
        file_name = "tests/mock_pas/write.pas"
        pascal_program = Program(file_name)
        pascal_program.run()
        from printer import OutputBuffer

        self.assertEqual(len(OutputBuffer.instructions), 8)

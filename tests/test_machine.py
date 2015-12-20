from tests.base import TestBase
from skynet import Skynet


class TestMachine(TestBase):

    def test_pass_valid_int_machine(self):
        file_name = "tests/mock_machine/add.o"
        machine_program = Skynet(file_name)
        machine_program.run()

        lookup_buffer = machine_program.buffer

        self.assertEqual(lookup_buffer[0],24)


class TestMachine(TestBase):

    def test_pass_valid_real_machine(self):
        file_name = "tests/mock_machine/int_real.o"
        machine_program = Skynet(file_name)
        machine_program.run()

        lookup_buffer = machine_program.buffer
        self.assertEqual(len(lookup_buffer), 2)
        self.assertEqual(lookup_buffer[0],24)
        self.assertEqual(lookup_buffer[1],7.75)


class TestMachine(TestBase):

    def test_pass_valid_real_machine(self):
        file_name = "tests/mock_machine/machine.o"
        machine_program = Skynet(file_name)
        machine_program.run()

        lookup_buffer = machine_program.buffer
        self.assertEqual(len(lookup_buffer), 5)
        self.assertEqual(lookup_buffer[0], 24)
        self.assertEqual(lookup_buffer[1], 7.75)
        self.assertEqual(lookup_buffer[2], "a")
        self.assertEqual(lookup_buffer[3], False)
        self.assertEqual(lookup_buffer[4], True)
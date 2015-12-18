#!/usr/bin/env python

import sys
import argparse

from pascal.program import Program
from printer import OutputBuffer


arg_parser = argparse.ArgumentParser(prog='Pascal Compiler')

arg_parser.add_argument('-p', '--pascal', required=True,
                        dest='filename',
                        help='location of pascal program')
arg_parser.add_argument('-o', '--outfile',
                        dest='out_filename',
                        help='file to output operations')

args = arg_parser.parse_args()


def main():
    pascal_program = Program(args.filename)

    pascal_program.run()
    OutputBuffer.print_output(args.out_filename or None)
    sys.exit(0)


if __name__ == "__main__":
    main()


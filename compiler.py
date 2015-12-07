#!/usr/bin/env python

import sys
import argparse
import json
from program import Program

arg_parser = argparse.ArgumentParser(prog='Pascal Compiler')

arg_parser.add_argument('-f', '--filename', required=True,
                    dest='filename',
                    help='location of pascal program')

args = arg_parser.parse_args()


def main():
    pascal_program = Program(args.filename)

    pascal_program.run()
    print json.dumps(pascal_program.symbol_table, indent=2)
    sys.exit(0)


if __name__ == "__main__":
    main()


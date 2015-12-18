#!/usr/bin/env python

import sys
import argparse

from skynet import Skynet


arg_parser = argparse.ArgumentParser(prog='Pascal Compiler')

arg_parser.add_argument('-f', '--filename', required=True,
                        dest='filename',
                        help='location of machine instr')

arg_parser.add_argument('-d', '--debug',
                        dest='debug',
                        action='store_true')

args = arg_parser.parse_args()


def main():
    machine_program = Skynet(args.filename, debug=args.debug)

    machine_program.run()
    sys.exit(0)


if __name__ == "__main__":
    main()


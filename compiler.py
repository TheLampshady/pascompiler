#!/usr/bin/env python

import sys
import argparse
from scanner import Scanner

parser = argparse.ArgumentParser(prog='Pascal Compiler')

parser.add_argument('-f', '--filename', required=True,
                    dest='filename',
                    help='location of pascal program')

args = parser.parse_args()


def main():
    scanner = Scanner(args.filename)

    while not scanner.eof:
        word = scanner.get_word()
        print word
    sys.exit(0)


if __name__ == "__main__":
    main()  # Calls main
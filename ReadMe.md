# Python Pascal Compiler

Through the magic of python pascal is compiled

## Installation

git clone https://github.com/TheLampshady/pascompiler.git

## Usage

### Pascal Compiler
python compiler.py -p programs/sample.pas -o machine.o

Help:

* python compiler.py -h

optional arguments:

* -h, --help                                show this help message and exit
* -p FILENAME, --pascal FILENAME            location of pascal program
* -o OUT_FILENAME, --outfile OUT_FILENAME   file to output operations


### Instruction Compiler
python pyssemble.py -f machine.o -d

Help:

* python pyssemble.py -h

optional arguments:

* -h, --help                            show this help message and exit
* -f FILENAME, --filename FILENAME      location of machine instruction
* -d, --debug                           shows the stack and memory after each instruction

## Credits

Zach Goldstein

## License

Apache
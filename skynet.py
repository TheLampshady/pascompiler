import collections

def parse_line(instr):
    split_line = instr.split()
    return split_line[0], ' '.join(split_line[1:])


class Skynet(object):

    def __init__(self, filename, debug=False):
        self.instr_file = open(filename, 'r')
        self.memory = dict()
        self.stack = list()
        self.debug = debug
        self.buffer = list()

    def run(self):

        for line in self.instr_file:
            instr, value = parse_line(line)
            if instr == 'push':
                self.stack.append(value)
            elif instr == 'pusha':
                self.memory[int(value)] = self.stack.pop()
            elif instr == 'pop ':
                self.stack.pop()
            elif instr == 'addr':
                self.stack.append(self.memory.get(int(value)))
            elif instr == 'write ':
                self.buffer.append(self.stack.pop())
            elif instr == 'convf':
                a = self.stack.pop()
                self.stack.append(float(a))
            elif instr == 'exch':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a)
                self.stack.append(b)
            elif instr == 'add':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(a) + int(b))
            elif instr == 'fadd':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(float(a) + float(b))
            elif instr == 'sub':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(a) - int(b))
            elif instr == 'fsub':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(float(a) - float(b))
            elif instr == 'mul':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(a) - int(b))
            elif instr == 'fmul':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(float(a) - float(b))
            elif instr == 'div':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(a) - int(b))
            elif instr == 'fdiv':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(float(a) - float(b))
            elif instr == 'and':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(bool(a) - bool(b))
            elif instr == 'band':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(a) - int(b))
            elif instr == 'or':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(bool(a) - bool(b))
            elif instr == 'bor':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(a) & int(b))
            elif instr == 'lss':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a < b)
            elif instr == 'gtr':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a > b)
            elif instr == 'lse':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a <= b)
            elif instr == 'gte':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a >= b)
            elif instr == 'eq':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a == b)
            elif instr == 'eq':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a != b)
            else:
                print "Unknown: %s" % instr
            self.print_state("%s %s" % (instr, value))

        self._print_output()

    def _print_output(self):
        if self.buffer:
            print 'Output:'
            print '-------\n\n:'
            print '\n'.join(self.buffer)

    def print_state(self, instruction):
        print "Instruction: %s" % instruction
        print "Memory: \n%s" % '\n'.join(["%s:%s" % (k,v) for k,v in sorted(self.memory.items())])
        print ''
        print "Stack: \n%s" % self.stack
        print ''
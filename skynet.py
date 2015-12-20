

def parse_line(instr):
    split_line = instr.split()
    x, y = split_line[0], ' '.join(split_line[1:])
    if y.lower() == 'true':
        y = True
    elif y.lower() == 'false':
        y = False

    return x, y

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
            elif instr == 'write':
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
                self.stack.append(int(b) - int(a))
            elif instr == 'fsub':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(float(b) - float(a))
            elif instr == 'mul':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(a) * int(b))
            elif instr == 'fmul':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(float(a) * float(b))
            elif instr == 'div':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(b) / int(a))
            elif instr == 'fdiv':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(float(b) / float(a))
            elif instr == 'and':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(bool(a) & bool(b))
            elif instr == 'band':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(a) & int(b))
            elif instr == 'or':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(bool(a) | bool(b))
            elif instr == 'bor':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(int(a) | int(b))
            elif instr == 'lss':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(b < a)
            elif instr == 'gtr':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(b > a)
            elif instr == 'lse':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(b <= a)
            elif instr == 'gte':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(b >= a)
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
            if self.debug:
                self.print_state("%s %s" % (instr, value))

        self._print_output()

    def _print_output(self):
        if self.buffer:
            print 'Output:'
            print '-------\n'
            print '\n'.join([str(x) for x in self.buffer])

    def print_state(self, instruction):
        print "Instruction: %s" % instruction
        print "Memory: \n%s" % '\n'.join(["%s:%s" % (k,v) for k,v in sorted(self.memory.items())])
        print ''
        print "Stack: \n%s" % self.stack
        print ''
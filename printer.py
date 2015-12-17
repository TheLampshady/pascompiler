# def singleton(class_):
# instances = {}
#
#     def get_instance(*args, **kwargs):
#         if class_ not in instances:
#             instances[class_] = class_(*args, **kwargs)
#         return instances[class_]
#
#     return get_instance


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance



class OutputBuffer(Singleton, object):
    instructions = list()

    @classmethod
    def add(cls, instr):
        cls.instructions.append(instr)

    @classmethod
    def print_output(cls, filename=False):
        if filename:
            with open(filename, 'w') as f:
                f.write('\n'.join(cls.instructions))
        else:
            print '\n'.join(cls.instructions)


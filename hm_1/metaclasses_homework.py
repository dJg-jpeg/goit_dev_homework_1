class MetaNumber(type):
    children_number = 0

    def __new__(mcs, name, bases, attrs):
        attrs_in_dict = dict(attrs)
        attrs_in_dict['class_number'] = MetaNumber.children_number
        MetaNumber.children_number += 1
        return type(name, bases, attrs_in_dict)


class Cls1(metaclass=MetaNumber):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=MetaNumber):
    def __init__(self, data):
        self.data = data


class Cls3(metaclass=MetaNumber):
    def __init__(self, data):
        self.data = data


class Cls4(metaclass=MetaNumber):
    def __init__(self, data):
        self.data = data


if __name__ == "__main__":
    assert (Cls1.class_number, Cls2.class_number, Cls3.class_number, Cls4.class_number) == (0, 1, 2, 3)
    a, b, c, d = Cls1('a'), Cls2('b'), Cls3('c'), Cls4('d')
    assert (a.class_number, b.class_number, c.class_number, d.class_number) == (0, 1, 2, 3)
    print(Cls1.class_number)
    print(Cls2.class_number)
    print(Cls3.class_number)
    print(Cls4.class_number)

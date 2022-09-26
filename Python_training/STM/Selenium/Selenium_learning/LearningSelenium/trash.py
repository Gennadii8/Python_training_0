class A:
    def hi(self):
        print("A")


class B(A):
    def hi(self):
        print("B")


class C(A):
    def hi(self):
        print("C")


class D(B, C):
    pass


d = D()
d.hi()


def test():
    print("Hi")
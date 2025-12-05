class A:
    label = "Print A"

class B(A):
    label = "Print B"

class C(A):
    label = "Print C"

class D(B,C):
    pass


print_label = D()
print(print_label.label)
print(D.__mro__)
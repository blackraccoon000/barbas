# from package_test import utils
# from package_test.talk import human


# r = utils.say_twice("hello")
# print(r)
# print(human.__doc__)
def outer(a, b):
    def inner(c, d):
        return c + d

    r1 = inner(a, b)
    r2 = inner(a, b)

    return r1 + r2


print(outer(1, 2))

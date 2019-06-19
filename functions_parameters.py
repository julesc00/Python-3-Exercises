# Functions with parameters

# def parameters(a):
#     print(a)
#
#
# parameters("This is a parameter")
#
#
# def add(a, b):
#     c = a + b
#     return c
#
# def substract(a, b):
#     c = a - b
#     return c
#
# def times(a, b):
#     c = a * b
#     return  c
#
# def division(a, b):
#     c = a / b
#     return c
#
# subs_result = substract(2019, 1975)
# sum_result = add(12, 5)
#
# # With strings
# sum_strings = add("Te amo ", "Claudia")
#
# print(sum_strings)
# print(subs_result)
# print(sum_result)

# def default_param(a, b = 4, c = 5):
#     return a + b + c
#
# result = default_param(3)
# print(result)
#########################################

#Nested functions.

# def scope(a):
#     a = a + 1
#     print(a)
#     return a
# scope(5)

# def outer(a):
#
#     def nested(b):
#         return b * a;
#     a = nested(a)
#     return a
#
# print(outer(4))

def f(a):
    def g(b):
        def h(c):
            return a * b * c

        return h

    return g

print(f(5)(2)(3))








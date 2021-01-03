# def mu_decorator(func):
#     def func_wraper():
#         print("CODE before")
#         func()
#         print("CODE after")
#     return func_wraper
#
# @mu_decorator
# def func_test():
#     print("hello im func test")
#
#
# # test = mu_decorator(func_test)
# # test()
#
#
# func_test()


def make_title(fn):
    def wrapped():
        title = fn()
        title = title.capitalize()
        title = title.replace(",", "")
        return title
    return wrapped


@make_title
def hi():
    return "hello, world!"


print(hi())


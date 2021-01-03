class Person:
    # default values:
    name = "Username"
    __age = 20

    def __init__(self, name, age):
        # print("construct")
        self.name = name
        self.__age = age

    def print_info(self):
        print(f"Name: {self.name}, Age:{self.__age}")

    def get_age(self):
        return self.__age

    def set_age(self, value):
        try:
            new_age = int(value)
            if 1 < new_age < 120:
                self.__age = value
            else:
                print("age out of range 1-120")
        except ValueError:
            print("bad value")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        try:
            new_age = int(value)
            if 1 < new_age < 120:
                self.__age = value
            else:
                print("age out of range 1-120")
        except ValueError:
            print("bad value")



# p1 = Person("John", 30)
# # print(p1.age)
# # p1.age = 35
# p1.print_info()















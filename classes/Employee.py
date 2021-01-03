from classes.Person import Person


class Employee(Person):
    company = "Google"

    def __init__(self, name, age, company):
        super().__init__( name, age)
        self.company = company

    def more_info(self):
        print(
            f"Name: {self.name}",
            f"Age:{self.age}",
            f"Company: {self.company}",
            sep="\n", end="\n\n")

    def __str__(self):
        return f"{self.__class__.__name__} \nName: {self.name},"\
            f"Age:{self.age},"\
            f"Company: {self.company}"

    def __int__(self):
        return self.age



# em1 = Employee("Nick", 27, "compTest")
# em1.print_info()
# em1.more_info()
# print(int(em1))
# print(em1)









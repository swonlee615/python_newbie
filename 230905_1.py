class MyStatus:
    def __init__(self,age,name,height,weight):
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

    def print_height(self):
        print(self.height)

    def print_weight(self):
        print(self.weight)

    def attack(self, person):
        print(person)


# print(MyStatus(34,"yamada",170,34).age)
# print(MyStatus(34,"swonlee",170,66).age)
a = MyStatus(34,"yamada",170,78)
a.print_name()
a.attack("yekang")

def attack(person) :
    print(person)

attack("yekang")

a.print_weight()
print(a.weight)
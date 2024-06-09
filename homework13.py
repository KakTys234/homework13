class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.say_info()


    def say_info(self):
        print(f'Название: {self.name}, Количество этажей: {self.number_of_floors}')




h1 = House('ЖК Эльбрус',30)


def go_to(new_floor):
    if new_floor <= 30:
        return new_floor
    else:
        return 'Такой этаж не существует'

h1 = go_to(1)
h2 = go_to(2)
h3 = go_to(3)
h4 = go_to(4)
h5 = go_to(5)
h6 = go_to(31)

print(h1)
print(h2)
print(h3)
print(h4)
print(h5)
print(h6)
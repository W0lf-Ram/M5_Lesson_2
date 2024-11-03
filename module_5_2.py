class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
    def __len__(self):
        return self.numbers_of_floors
    def __str__(self):
        return (f'Название: {self.name}, Количество этажей: {self.numbers_of_floors}')
    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print('Такого этажа не существует')
            return None
        for i in range(new_floor + 1):
            if i > 0:
                print(i)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

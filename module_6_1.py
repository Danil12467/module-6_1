class Animal:
    def __init__(self, name):
        self.alive = True  # Живое существо
        self.fed = False  # Накормлено
        self.name = name  # Имя животного

class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобное
        self.name = name  # Имя растения

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Fruit):
            print(f'{self.name} сьел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Fruit):
            print(f'{self.name} сьел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобные

a1 = Predator('Тигр')
a2 = Mammal('Заяц')
p1 = Flower('Лютик')
p2 = Fruit('Морковка')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


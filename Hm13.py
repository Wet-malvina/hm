class Animal():
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print("Я ем ")

class Bird (Animal):
    def make_sound(self):
        print("чирик-чирик")


class Mammal (Animal):
    def make_sound(self):
        print("Я млекопитающее")


class Peptile (Animal):
    def make_sound(self):
        print("ШШШШ")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee.name}")


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")
        animal.eat()


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

bird = Bird("черныш", 8)
cow = Mammal("Кристофер", 20)
snake = Peptile ("Мармеладик",10)

zookeeper = ZooKeeper("Виктория")
veterinarian = Veterinarian("Марина")

animals = [bird, cow, snake]
for animal in animals:
    animal.make_sound()

zookeeper.feed_animal(bird)
zookeeper.feed_animal(cow)

veterinarian.heal_animal(snake)


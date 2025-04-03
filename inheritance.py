class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Job(Person):
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender)
        self.position = position

    def information(self):
        if self.gender == "Male":
            gender = "He"
        else:
            gender = "She"
        print(f"{gender} name is {self.name} and age is {self.age} position is {self.position}")

p1 = Job("Hulusi", 18, "Male", "Software Developer")
p1.information()
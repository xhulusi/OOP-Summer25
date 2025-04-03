class person:
    def __init__(self, country, gender, name, location):
        self.country = country
        self.gender = gender
        self.name = name
        self.location = location
        
    def change_location(self, newlocation):
        self.location = newlocation
        
    def information(self):
        if self.gender == "Male":
            gend = "He"
        else:
            gend = "She"
            
        return f"{gend}`s from {self.country} and who name is {self.name} live in {self.location}"
        
p1 = person("Poland", "Male", "Piotr", "Warsaw")
p1.change_location("Poznan")
print(p1.information())

p2 = person("Turkiye", "Female", "Ece", "Istanbul")
print(p2.information())

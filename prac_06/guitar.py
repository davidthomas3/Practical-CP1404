CURRENT_YEAR = 2019  # constant value
VINTAGE_AGE = 50  # constant value
class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):  # checks how old the guitar is
        return CURRENT_YEAR - self.year

    def is_vintage(self):  # takes value from get_age and checks the value. if value more than 50 it will return the value
        return self.get_age() >= VINTAGE_AGE


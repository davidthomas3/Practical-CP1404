class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """takes the value from the list in this order"""
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def __str__(self):
        """takes values from above and prints out the values"""
        return "{}, {}, {}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                         self.year)

    def is_dynamic(self):
        """function to check if the language is dynamic"""
        return self.typing == "Dynamic"


def user_print():
    """function to print the statement"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)


if __name__ == "__main__":
    user_print()

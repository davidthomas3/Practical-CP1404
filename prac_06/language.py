from prac_06.programming_language import ProgrammingLanguage
"""import the class from the file"""


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False,
                                       1991)
    """the ProgrammingLanguage is the class. it will take the varaibles from the list and catagories it in order"""

    programming_list = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for programming_language in programming_list:
        """will take the typing value from the list as an expression"""
        if programming_language.is_dynamic():
            """checks from ProgrammingLanguage file if language is Dynamic. if it is then it is returned"""
            print(programming_language.name)


if __name__ == "__main__":
    main()

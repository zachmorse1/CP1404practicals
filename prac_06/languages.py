"""
CP1404 - Prac 6
Estimate - 20 minutes
Actual time taken - 15 minutes

"""

from programming_language import ProgrammingLanguage


def main():
    """Determines if programming languages are dynamically typed."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [python, ruby, visual_basic]
    print(python)
    print(ruby)
    print(visual_basic)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.field)


main()

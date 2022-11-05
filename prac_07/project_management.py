"""
CP1404 - Prac 7
Estimate - 30 minutes
Actual time taken - 35 minutes
"""
from prac_07.project import ProjectManagement

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- " \
       "(A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = []
    print(MENU)
    menu_choice = input(">>> ").lower
    while menu_choice != "q":
        if menu_choice == "l":
            filename = get_valid_input("Filename: ", "Filename cannot be empty")
            load_file("projects.txt")
        elif menu_choice == "s":
            save_project()
        elif menu_choice == "d":
            display_projects()
        elif menu_choice == "f":
            filter_projects()
        elif menu_choice == "a":
            add_new_project()
        elif menu_choice == "u":
            update_projects()
        else:
            print("Invalid menu choice")
        menu_choice = input(">>> ").lower


def get_valid_input(prompt, error_message):
    """Get valid user input."""
    user_input = input(prompt)
    while user_input == "":
        print(error_message)
        user_input = input(prompt)
    return user_input


def load_file(filename):
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split("\t")
            print(parts)


def update_projects():
    pass


def add_new_project():
    pass


def filter_projects():
    pass


def display_projects():
    pass


def save_project():
    pass


main()

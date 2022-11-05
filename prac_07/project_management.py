"""
CP1404 - Prac 7
Estimate - 30 minutes
Actual time taken - 35 minutes
"""
from prac_07.project import ProjectManagement
import datetime

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- " \
       "(A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = []
    print(MENU)
    menu_choice = input(">>> ").lower
    while menu_choice != "q":
        if menu_choice == "l":
            filename = get_valid_input("Filename: ", "Filename cannot be empty")
            load_file(projects, "projects.txt")
        elif menu_choice == "s":
            filename = get_valid_input("Filename: ", "Filename cannot be empty")
            save_projects(projects, "projects.txt")
        elif menu_choice == "d":
            display_projects(projects)
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


def load_file(projects, filename):
    """Loads projects from a file."""
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            projects.append(ProjectManagement(parts[0], parts[1], int(parts[2]), float(parts[3])), int(parts[4]))
            print(f"{filename} loaded.")


def update_projects():
    pass


def add_new_project():
    pass


def filter_projects():
    get_valid_input("Show projects that start after date (dd/mm/yy): ")


def display_projects(projects):
    """Display the projects sorted by priority and completion status"""
    projects.sort()
    for project in projects:
        print(project)


def save_projects(contents, filename):
    """Saves content to a file passed to it"""
    with open(filename, "w", encoding="utf8") as out_file:
        for content in contents:
            print(f"{content}", file=out_file)


main()

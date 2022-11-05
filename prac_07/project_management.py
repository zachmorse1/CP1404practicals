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
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "l":
            # filename = get_valid_input("Filename: ", "Filename cannot be empty")
            load_file(projects, "projects.txt")
        elif menu_choice == "s":
            # filename = get_valid_input("Filename: ", "Filename cannot be empty")
            save_projects(projects, "projects.txt")
        elif menu_choice == "d":
            display_projects(projects)
        elif menu_choice == "f":
            filter_projects(projects)
        elif menu_choice == "a":
            add_new_project(projects)
        elif menu_choice == "u":
            update_projects(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")


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
            project = ProjectManagement(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
        print(f"{filename} loaded")


def update_projects(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    index = get_valid_number("Project choice: ", len(projects))
    print(projects[index])
    new_percentage = get_valid_number("New Percentage (0-100): ", 100)
    new_priority = get_valid_number("New Priority(0-9): ", 9)
    projects[index].priority = new_priority
    projects[index].percentage_completed = new_percentage
    print(f"project {index} updated.")


def get_valid_number(prompt, maximum_value):
    """Get valid number from user."""
    is_finished = False
    number = 0
    while not is_finished:
        try:
            number = int(input(prompt))
            while number < 0 or number > maximum_value:
                if number < 0:
                    print("Number must be >= 0")
                elif number > maximum_value:
                    print("Number out of range")
                number = int(input(prompt))
            is_finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


def add_new_project(projects):
    pass


def filter_projects(projects):
    # get_valid_input("Show projects that start after date (dd/mm/yy): ")
    date_string = "20/7/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    projects.sort()
    for project in projects:
        print(project)


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

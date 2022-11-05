"""
CP1404 - Prac 7
Estimate - 40 minutes
Actual time taken - 120 minutes
"""
from prac_07.project import ProjectManagement
import datetime
import math
from operator import itemgetter

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- " \
       "(A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = []
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "l":
            filename = get_valid_input("Filename: ", "Filename cannot be empty")
            load_file(projects, filename)
        elif menu_choice == "s":
            filename = get_valid_input("Filename: ", "Filename cannot be empty")
            save_file(projects, filename)
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
    index = get_valid_number("Project choice: ", len(projects) - 1)
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
                elif number >= maximum_value:
                    print("Number out of range")
                number = int(input(prompt))
            is_finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


def add_new_project(projects):
    print("Let's add a new project")
    name = get_valid_input("Name: ", "Name cannot be blank.")
    start_date = get_valid_input("Start date (dd/mm/yy): ", "Date cannot be blank.")
    priority = get_valid_input("Priority: ", "Priority cannot be blank.")
    cost_estimate = get_valid_number("Cost estimate:", math.inf)
    percent_completed = get_valid_number("Percent complete: ", 100)
    new_project = ProjectManagement(name, start_date, int(priority), float(cost_estimate), int(percent_completed))
    projects.append(new_project)
    print(f"{name} project added.")


def filter_projects(projects):
    date_string = get_valid_input("Show projects that start after date (dd/mm/yyyy): ", "Invalid date")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        projects = sorted(projects, key=lambda x: datetime.datetime.strptime(f"{project.start_date}", "%d/%m/%Y"),
                          reverse=False)
        if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date:
            print(project)


def display_projects(projects):
    """Display the projects sorted by priority and completion status"""
    projects.sort()
    completed_projects = [project for project in projects if project.is_completed()]
    incomplete_projects = [project for project in projects if not project.is_completed()]
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Complete projects: ")
    for project in completed_projects:
        print(f"\t{project}")


def save_file(contents, filename):
    """Saves content to a file passed to it"""
    with open(filename, "w", encoding="utf8") as out_file:
        print("Name	Start Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for content in contents:
            print(f"{content.name}\t{content.start_date}\t{content.priority}\t{content.cost_estimate}"
                  f"\t{content.percentage_completed}", file=out_file)
        print(f"Projects saved to {filename}")


main()

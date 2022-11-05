class ProjectManagement:
    """Manages projects loaded from a file"""

    def __init__(self, name, start_date, priority, cost_estimate, percentage_completed):
        """Initiates a project"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage_completed = percentage_completed

    def __str__(self):
        """Returns details of project in a string."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: $" \
               f"{self.cost_estimate:.2f}, completion: {self.percentage_completed}%"

    def __lt__(self, other):
        """Less than, used for sorting projects by priority."""
        return self.priority < other.priority

    def __gt__(self, date):
        """Greater than, used for sorting projects by date"""
        return self.start_date > date.start_date

    def is_completed(self):
        """Determines if a project is completed."""
        return self.percentage_completed == 100


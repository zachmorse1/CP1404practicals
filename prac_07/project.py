class ProjectManagement:
    """Manages projects loaded from a file"""
    def __init__(self, name, start_date, priority, cost_estimate, percentage_completed):
        """Initiates a project"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage_completed = percentage_completed


class Team:
    def __init__(self):
        self.managers = set()
        self.employees = set()
        self.projects = set()

        raise NotImplementedError

    def add_manager(self, manager):
        self.managers.add(manager)

    def remove_manager(self, manager):
        self.managers.remove(manager)

    def add_employee(self, employee):
        self.employees.add(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def add_project(self, project):
        self.projects.add(project)

    def remove_project(self, project):
        self.projects.remove(project)

class StoryPointsTeam(Team):
    # Team that uses story points

    def __init__(self):
        self.story_point_velocity
        raise NotImplementedError


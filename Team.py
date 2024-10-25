class Team:
    def __init__(self):
        self.managers = []
        self.employees = []
        self.projects = []


        raise NotImplementedError

    def add_manager(self, manager):
        self.managers.append(manager)


    def add_employee(self, employee):
        self.employees.append(employee)

    def add_project(self, project):
        self.projects.append(project)


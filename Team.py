import math


class Team:
    def __init__(self):
        self.managers = set()
        self.employees = set()
        self.projects = set()
        # Finished tasks go in sprints
        self.sprints = []

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


    def start_sprint(self):
        self.sprints.append([])

    def finish_task(self, task):
        self.sprints[-1].append(task)

class StoryPointsTeam(Team):
    # Team that uses story points

    def __init__(self):
        self.story_point_velocity = 0
        raise NotImplementedError


    def recalculate_velocity(self):
        # uses geometric function to calculate velocity
        n = len(self.sprints) - 1
        count = 1
        self.story_point_velocity = 0
        for i in range(n-1, -1, -1):
            s = sum(sprint.get_points() for sprint in self.sprints[i])
            if i == 0:
                count -= 1
            self.story_point_velocity += s * math.pow(0.5, count)
            count += 1










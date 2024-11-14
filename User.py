class TooManyTasksError(Exception):
    def __str__(self):
        return "You cannot have more than one current task"
class InvalidAccessError(Exception):
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"You do not have access to do {self.type}"

class InvalidTaskError(Exception):
    def __init__(self, task):
        self.task = task

    def __str__(self):
        return f"{self.task} is already owned by someone. You can only change to tasks that are currently availiable."

class User:
    def __init__(self, name, salary=0):
        self.salary = salary
        self.name = name

    def change_salary(self, new_salary):
        self.salary = new_salary

    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name



class Admin(User):
    def __init__(self, name, salary=0):
        super.__init__(name, salary)

    def change_required_return(self, required_return):
        raise NotImplementedError

class Manager(User):


    def __init__(self, name, can_see_salaries = True, salary=0):
        self.can_see_salaries = can_see_salaries
        super.__init__(name, salary)


    def get_salary(self, employee):
        if self.can_see_salaries == False:
            raise InvalidAccessError
        else:
            return employee.salary


    raise NotImplementedError


class Employee(User):

    def __init__(self):
        self.competencies = set()
        self.team = None
        self.current_task = None
        raise NotImplementedError

    def add_competency(self, competency):
        self.competencies.add(competency)

    def remove_competency(self, competency):
        self.competencies.remove(competency)

    def complete_current_task(self):
        self.complete_task(self.current_task)

    def change_task(self, task=None):
        if task:
            if task not in self.team.get_project().get_availiable_tasks:
                raise InvalidTaskError(Exception)
            self.remove_task(self.current_task)
            self.current_task = task
            self.team.get_project().move_task_to_in_progress(task)
        else:
            self.remove_task(self.current_task)
            self.get_task()

    def complete_task(self, task):
        task.project.finish_task(task)
        self.current_task = None

    def remove_task(self):
        self.team.get_project().remove_task_from_in_progress(self.current_task)
        self.current_task = None

    def get_task(self):
        if self.current_task:
            raise TooManyTasksError
        else:
            for task in self.team.get_project().get_avaliable_tasks():
                for competency in task.get_competencies():
                    if competency in self.competencies:
                        self.current_task = task
                        self.team.get_project().move_task_to_in_progress(task)
                        return





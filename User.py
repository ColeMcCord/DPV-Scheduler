import Company
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
        super().__init__(name, salary)
        self.company = Company.Company.get_instance()

    def change_required_return(self, required_return):
        self.company.update_required_rate_of_return(required_return)

    def create_manager(self):
        raise NotImplementedError

    def create_team(self):
        raise NotImplementedError

    def create_employee(self):
        raise NotImplementedError

    def create_admin(self):
        raise NotImplementedError


class Manager(User):

    def __init__(self, name, can_see_salaries=True, salary=0):
        super().__init__(name, salary)
        self.can_see_salaries = can_see_salaries


    def get_salary(self, employee):
        if not self.can_see_salaries:
            raise InvalidAccessError
        else:
            return employee.salary

    def assign_task(self, employee, task):
        raise NotImplementedError

    def create_project(self):
        raise NotImplementedError

    # raise NotImplementedError


class Employee(User):

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.competencies = set()
        self.team = None
        self.current_task = None
        self.can_add_tasks = True
        # raise NotImplementedError

    def set_team(self, team):
        self.team = team

    def add_competency(self, competency):
        self.competencies.add(competency)

    def remove_competency(self, competency):
        self.competencies.remove(competency)

    def complete_current_task(self):
        self.complete_task(self.current_task)
        self.current_task = None

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
        self.team.get_project().finish_task(task)
        # self.current_task = None

    def remove_task(self):
        self.team.get_project().remove_task_from_in_progress(self.current_task)
        self.current_task = None

    def add_task(self, task):
        if self.can_add_tasks:
            self.team.get_project().add_task(task)

    #     Else Error!!!!



    def get_current_task(self):
        return self.current_task
    def get_task(self):
        if self.current_task:
            raise TooManyTasksError
        else:
            for task in self.team.get_project().get_availiable_tasks():
                for competency in task.get_competencies():
                    if competency in self.competencies:
                        self.current_task = task
                        self.team.get_project().move_task_to_in_progress(task)
                        return
            for task in self.team.get_project().get_availiable_tasks():
                self.current_task = task
                self.team.get_project().move_task_to_in_progress(task)
                return

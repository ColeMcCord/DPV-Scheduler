
class InvalidAccessError(Exception):
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"You do not have access to do {self.type}"


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
        if self.can_see_salaries = False:
            raise


    raise NotImplementedError


class Employee(User):

    def __init__(self):
        self.competencies = []
        raise NotImplementedError

    def add_competency(self):
        raise NotImplementedError

    def remove_competency(self):
        raise NotImplementedError




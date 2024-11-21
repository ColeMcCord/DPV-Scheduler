from Task import Task
from Team import Team
from User import *
from Company import Company
from Project import *


def create_company():
    company = Company.Company.get_instance()
    team_a = Team()
    team_b = Team()
    company.add_team(team_a)
    company.add_team(team_b)
    m1 = Manager("john", True, 500)
    m2 = Manager("beth", False, 1)
    e1 = Employee("amy", 5000)
    e2 = Employee("karen", 2)
    a1 = Admin("seth", 0)
    team_a.add_manager(m1)
    team_b.add_manager(m2)
    team_a.add_employee(e1)
    team_b.add_employee(e2)
    e1.add_competency("ski")
    e2.add_competency("bread")
    p1 = Project("Project 1")
    team_a.add_project(p1)
    task_1 = Task("Eath Pots")
    e1.add_task(task_1)
    print(e1.team.get_project().availiable_tasks)
    e1.get_task()
    print(e1.current_task)
    e1.complete_current_task()
    print(e1.current_task)
    print(e1.team.get_project().availiable_tasks)



create_company()

class InfiniteValueError(Exception):
    def __str__(self):
        return "This project has infinite value. Please refer problem to admin"


class RecursionError(Exception):
    def __init__(self, task):
        self.task = task

    def __str__(self):
        return f"{self.task} is its own prerequisite. Please modify project task dependencies before sorting tasks."

class Project:
    def __init__(self, name, team, company):
        self.name = name
        self.team = team
        self.task_list = []
        self.finished_tasks = []
        self.required_by = None
        self.growth_rate = 0
        self.instant_return = 0
        self.continous_return = 0
        self.company = company
        self.length = 0

        self.availiable_tasks = set()

    def add_task(self, task):
        self.task_list.append(task)
        self.sort_tasks()

    def sort_tasks(self):
        topological_sort = []
        visited = set()
        current = set()
        def dfs(task):
            if task in current:
                raise RecursionError(task)
            if task in visited: return
            visited.add(task)
            current.add(task)
            for prerequisite in task.get_prerequisites():
                dfs(prerequisite)
            topological_sort.append(task)

        for task in self.task_list:
            if task not in visited:
                current = set()
                dfs(task)
        self.task_list = topological_sort
        return self.task_list

    def remove_task(self, task):
        for t in self.task_list:
            if task in t.get_prerequisites():
                t.remove_prerequisite(task)
        self.task_list.remove(task)
        self.update()

    def finish_task(self, task):
        # TODO:
        # Deal with how this affects user
        self.remove_task(task)
        self.finished_tasks.append(task)

    def pop_task(self):
        return self.task_list[0]

    def update(self):
        self.sort_tasks()
        self.availiable_tasks = set()
        for task in self.task_list:
            if len(task.get_prerequisites()) == 0:
                self.availiable_tasks.add(task)

    def get_length(self):
        self.length = sum([task.get_length() for task in self.task_list])
        return self.length

    def get_DPV(self):
        temp = self.instant_return
        if self.continous_return > 0:
            if self.company.required_rate_of_return == 0:
                raise InfiniteValueError
            temp += self.continous_return/(self.company.required_rate_or_return - self.growth_rate)
        return temp * ((1 - self.company.required_rate_of_return) ** self.length)

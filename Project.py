class Project:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)
        self.sort_tasks()

    def sort_tasks(self):
        raise NotImplementedError

    def remove_task(self, task):
        raise NotImplementedError

    def finish_task(self, task):
        raise NotImplementedError

    def pop_task(self):
        raise NotImplementedError

    def edit_task(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError


    class Timeline:
        # Project timeline

        def __init__(self):
            raise NotImplementedError



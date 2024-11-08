

class ProjectSchedule:
    def __init__(self):
        self.project_order = []

        raise NotImplementedError

    def calculate_schedule_order(self, projects):
        self.project_order = [(project, project.get_DPV) for project in projects]
        self.project_order.sort(key=lambda x: x[1], reverse=True)
        return self.project_order







    raise NotImplementedError

class TaskSchedule:
    raise NotImplementedError
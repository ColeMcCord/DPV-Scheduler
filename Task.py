import User
class Task:
    def __init__(self, name, description=None, length=0):
        self.name = name
        self.description = description
        # Fix Length!!!!!!!
        self.length = 0
        self.prerequisites = set()
        self.competencies = set()

    def __str__(self):
        return self.name

    def add_competency(self, competency):
        self.competencies.add(competency)

    def remove_competency(self, competency):
        self.competencies.remove(competency)

    def get_competencies(self):
        return self.competencies

    def add_prerequisite(self, task):
        self.prerequisites.add(task)

    def remove_prerequisite(self, task):
        self.prerequisites.remove(task)

    def get_description(self):
        return self.description

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_prerequisites(self):
        return self.prerequisites


class Story_Task(Task):
    # Tasks measured in story points
    def __init__(self, story_points):
        super()
        self.story_points = story_points

        raise NotImplementedError

    def get_points(self):
        return self.story_points

    def vote_on_difficulty(self, points):
        # An employee can determine how difficult they think a task will be
        raise NotImplementedError

    def update_story_points(self, points):
        self.story_points = points

class Time_Task(Task):
    # Tasks measured in days

    def __init__(self, length):
        self.length = length





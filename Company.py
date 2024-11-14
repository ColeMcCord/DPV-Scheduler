class Company:

    def update_required_rate_of_return(self, rr):
        self.required_rate_of_return = rr

# class Company:
    _instance = None  # Private class attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # If there's no instance yet, create it
            cls._instance = super(Company, cls).__new__(cls)
            # Initialize your instance variables here if needed
        return cls._instance

    def __init__(self,):
        if not hasattr(self, 'initialized'):  # Avoid re-initialization
            self.initialized = True  # Mark the instance as initialized
            self.required_rate_of_return = 0
            self.teams = set()
    @staticmethod
    def get_instance():
        if Company._instance is None:
            Company()  # Initialize the singleton instance if it hasn't been already
        return Company._instance

    def get_required_rate_of_return(self):
        return self.required_rate_of_return

    def add_team(self, team):
        self.teams.add(team)

    def remove_team(self, team):
        self.teams.remove(team)

    def get_teams(self):
        return self.teams
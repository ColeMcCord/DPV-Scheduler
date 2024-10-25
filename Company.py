class Company:
    def __init__(self):
        self.required_rate_of_return = 0
        self.teams = set()
        raise NotImplementedError

    def update_required_rate_of_return(self, rr):
        self.required_rate_of_return = rr

    def add_team(self, team):
        self.teams.add(team)

    def remove_team(self, team):
        self.teams.remove(team)


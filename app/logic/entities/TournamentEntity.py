from app.logic.entities.BaseEntity import BaseEntity


class TournamentEntity(BaseEntity):
    def __init__(self, id_, name, date, place, competitors, categories):
        super().__init__(id_, 'tournament')
        self.name = name
        self.date = date
        self.place = place
        self.competitors = competitors
        self.categories = categories

from dataclasses import dataclass
from datetime import date

from players.position import Position


@dataclass(frozen=True)
class Player:
    first_name: str
    last_name: str
    shirt_number: int
    position: Position
    dob: date

    def calculate_age(self):
        today = date.today()
        if self.dob > today:
            raise ValueError('Invalid date of birth.')
        return today.year - self.dob.year - (
            (today.month, today.day) < (self.dob.month, self.dob.day))

    def is_goalkeeper(self):
        return self.position == Position.GOALKEEPER

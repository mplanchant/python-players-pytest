from dataclasses import replace
from datetime import date

import pytest

from players.player import Player
from players.position import Position


class TestPlayer:
    test_player = Player("Dan", "Burn", 33, Position.DEFENCE,
                         date(1980, 1, 29))

    def test_player_creation(self):
        assert self.test_player.first_name == "Dan"
        assert self.test_player.last_name == "Burn"
        assert self.test_player.shirt_number == 33
        assert self.test_player.position == Position.DEFENCE
        assert self.test_player.dob == date(1980, 1, 29)

    @pytest.mark.parametrize(
        "player, expected_age",
        [(test_player, 46),
         (replace(test_player, dob=date(1990, 1, 29)), 36),
         (replace(test_player, dob=date(2001, 1, 29)), 25)])
    def test_player_age(self, player, expected_age):
        assert player.calculate_age() == expected_age

    def test_player_age_invalid_dob(self):
        with pytest.raises(ValueError):
            invalid_player = replace(self.test_player, dob=date(2100, 1, 29))
            invalid_player.calculate_age()

    @pytest.mark.parametrize(
        "player, expected",
        [(test_player, False),
         (replace(test_player, position=Position.DEFENCE), False),
         (replace(test_player, position=Position.ATTACK), False),
         (replace(test_player, position=Position.GOALKEEPER), True)])
    def test_player_is_goalkeeper(self, player, expected):
        assert player.is_goalkeeper() == expected

from dataclasses import replace
from datetime import date

import pytest

from players.player import Player
from players.position import Position


class TestPlayer:

    @pytest.fixture
    def player(self):
        return Player("Dan", "Burn", 33, Position.DEFENCE, date(1980, 1, 29))

    def test_player_creation(self, player):
        assert player.first_name == "Dan"
        assert player.last_name == "Burn"
        assert player.shirt_number == 33
        assert player.position == Position.DEFENCE
        assert player.dob == date(1980, 1, 29)

    @pytest.mark.parametrize("dob, expected_age", [
        (date(1980, 1, 29), 46),
        (date(1990, 1, 29), 36),
        (date(2001, 1, 29), 25),
    ])
    def test_player_age(self, player, dob, expected_age):
        player = replace(player, dob=dob)
        assert player.calculate_age() == expected_age

    def test_player_age_invalid_dob(self, player):
        with pytest.raises(ValueError):
            invalid_player = replace(player, dob=date(2100, 1, 29))
            invalid_player.calculate_age()

    @pytest.mark.parametrize("position, expected", [
        (Position.MIDFIELD, False),
        (Position.DEFENCE, False),
        (Position.ATTACK, False),
        (Position.GOALKEEPER, True),
    ])
    def test_player_is_goalkeeper(self, player, position, expected):
        player = replace(player, position=position)
        assert player.is_goalkeeper() == expected

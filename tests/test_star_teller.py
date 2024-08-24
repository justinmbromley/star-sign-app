import pytest

from src.star_teller import star_sign

class TestStarTeller:
    def test_star_sign_working(self):
        assert star_sign(21, 3) == "Aries"
        assert star_sign(20, 4) == "Taurus"
        assert star_sign(21, 5) == "Gemini"
        assert star_sign(22, 6) == "Cancer"
        assert star_sign(24, 7) == "Leo"
        assert star_sign(24, 9) == "Virgo"
        assert star_sign(17, 10) == "Libra"
        assert star_sign(25, 10) == "Scorpius"
        assert star_sign(17, 12) == "Saggitarius"
        assert star_sign(13, 1) == "Capricornus"
        assert star_sign(17, 2) == "Aquarius"
        assert star_sign(10, 3) == "Pisces"

    def test_star_sign_working_fail(self):
        assert star_sign(43, 345) ==  "Invalid date entered"
import pytest

from  import star_teller.core.star_sign import star_sign

class TestStarTeller:
    def test_star_sign_working(self):
        assert star_sign("2024", "3", "23") == "Aries"
        assert star_sign("2024", "4", "20") == "Taurus"
        assert star_sign("2024", "5", "21") == "Gemini"
        assert star_sign("2024", "6", "22") == "Cancer"
        assert star_sign("2024", "7", "24") == "Leo"
        assert star_sign("2024", "8", "24") == "Virgo"
        assert star_sign("2024", "10", "17") == "Libra"
        assert star_sign("2024", "10", "25") == "Scorpio"
        assert star_sign("2024", "12", "17") == "Sagittarius"
        assert star_sign("2024", "12", "31") == "Capricorn"
        assert star_sign("2024", "2", "17") == "Aquarius"
        assert star_sign("2024", "3", "10") == "Pisces"

    def test_star_sign_working_fail(self):
        assert star_sign("234", "43", "345") ==  "Invalid date entered"

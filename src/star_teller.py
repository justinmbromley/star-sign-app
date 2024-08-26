from datetime import datetime

def star_sign(year: str, month: str, day: str) -> str:
    date_str = f"{year}{month}{day}"
    print(f"Date string: {date_str}")
    # See whether the date entered is valid
    try:
        date = datetime.strptime(date_str, "%Y%m%d")

    except:
        return "Invalid date entered"

    # Covering all star signs
    if datetime(date.year, 3, 21) <= date <= datetime(date.year, 4, 19):
        return "Aries"
    elif datetime(date.year, 4, 20) <= date <= datetime(date.year, 5, 20):
        return "Taurus"
    elif datetime(date.year, 5, 21) <= date <= datetime(date.year, 6, 20):
        return "Gemini"
    elif datetime(date.year, 6, 21) <= date <= datetime(date.year, 7, 22):
        return "Cancer"
    elif datetime(date.year, 7, 23) <= date <= datetime(date.year, 8, 22):
        return "Leo"
    elif datetime(date.year, 8, 23) <= date <= datetime(date.year, 9, 22):
        return "Virgo"
    elif datetime(date.year, 9, 23) <= date <= datetime(date.year, 10, 22):
        return "Libra"
    elif datetime(date.year, 10, 23) <= date <= datetime(date.year, 11, 21):
        return "Scorpio"
    elif datetime(date.year, 11, 22) <= date <= datetime(date.year, 12, 21):
        return "Sagittarius"
    elif datetime(date.year, 12, 22) <= date <= datetime(date.year, 12, 31) or datetime(date.year, 1, 1) <= date <= datetime(date.year, 1, 19):
        return "Capricorn"
    elif datetime(date.year, 1, 20) <= date <= datetime(date.year, 2, 18):
        return "Aquarius"
    elif datetime(date.year, 2, 19) <= date <= datetime(date.year, 3, 20):
        return "Pisces"
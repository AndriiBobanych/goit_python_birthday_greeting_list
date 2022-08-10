from collections import defaultdict
from typing import Dict, List
from datetime import datetime, timedelta
from random import randint


def get_weekday_by_id(weekday_id: int):

    weekday_map: Dict[int, str] = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    return weekday_map[weekday_id]


def generate_date() -> datetime.date:

    month_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    year = randint(1970, 2005)
    month = randint(1, 12)
    day = randint(1, month_days[month])
    return datetime(year=year, month=month, day=day).date()


users: List[Dict[str, datetime.date]] = [
    {
        "user 1": generate_date(),
        "user 2": generate_date(),
        "user 3": generate_date(),
    },
    {
        "user 4": generate_date(),
        "user 5": generate_date(),
        "user 6": generate_date(),
    },
    {
        "user 7": generate_date(),
        "user 8": generate_date(),
        "user 9": generate_date(),
    },
    {
        "user 10": generate_date(),
        "user 11": generate_date(),
        "user 12": generate_date(),
    },
    {
        "user 13": generate_date(),
        "user 14": generate_date(),
        "user 15": generate_date(),
    },
]
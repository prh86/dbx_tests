from typing import List
import holidays
import datetime
from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def set(cls):
        return set(map(lambda c: c.value, cls))

class Holidays(ExtendedEnum):
    NEWYEAR: str = "Capodanno"
    EPIPHANY: str = "Epifania del Signore"
    EASTER: str = "Pasqua di Resurrezione"
    EASTERMONDAY: str = "Lunedì dell'Angelo"
    LIBERATIONDAY: str = "Festa della Liberazione"
    LABORDAY: str = "Festa dei Lavoratori"
    REPUBLICDAY: str = "Festa della Repubblica"
    MIDAUGUSTDAY: str = "Assunzione della Vergine"
    SAINTSDAY: str = "Tutti i Santi"
    IMMACULATECONCEPTION: str = "Immacolata Concezione"
    CHRISTMAS: str = "Natale"
    SAINTSTEPHEN: str = "Santo Stefano"


def get_all_holidays(years: List[int], lst_holidays: List[str] = Holidays.list(), for_pension: bool = False) -> List:
    """
    Creates a list with all the holidays in the provided years, including the Good Friday.

    :param years: The list of years of interest.
    :type years: List[int]
    :param lst_holidays: The list of holidays to consider.
    :type lst_holidays: List[str]
    :param for_pension: Whether to consider the exception to the 2nd of January.
    :type for_pension: bool
    :return: The list of holidays datetime in the requested years.
    :rtype: List
    """
    lholidays = []
    italian_holidays = holidays.country_holidays("IT", years=years)
    for hol_day, hol_name in italian_holidays.items():
        if hol_name in lst_holidays:
            lholidays.append(hol_day)
            if hol_name == Holidays.EASTER.value:
                lholidays.append(hol_day + datetime.timedelta(days=-2))
            if hol_name == Holidays.NEWYEAR.value and for_pension:
                lholidays.append(hol_day + datetime.timedelta(days=1))

    return lholidays
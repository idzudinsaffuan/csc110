from dataclasses import dataclass
from python_ta.contracts import check_contracts
import datetime

@check_contracts
@dataclass
class FoodContainer:
    """A container that can store different foods."""
    label: str
    contents: list[str]

Mario = FoodContainer('Mario lunch box', ['sushi, chocolate'])
print(Mario.label)

def num_contents(food_containers: list[FoodContainer]) -> int:
    """Return the total number of items contained in the given food_containers.

    >>> container1 = FoodContainer('David', ['ham', 'cheese', 'chocolate'])
    >>> container2 = FoodContainer('Tom', ['sushi', 'chips'])
    >>> num_contents([container1, container2])
    5
    """
    sum([len(container.contents) for container in food_containers])

    sum_so_far = 0
    for c in food_containers:
        sum_so_far = sum_so_far + len(c.contents)
    return sum_so_far

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

@check_contracts
@dataclass
class Student:
    """A student at the University of Toronto.

    Representation Invariants:
    - len(self.utorid) <= 8 
    - self.year_of_study > 0
    - given_name != '' and family_name != '' and utorid != ''
    """
    given_name: str
    family_name: str
    year_of_study: int
    utorid: str


@dataclass
class Cssu:
    """The Computer Science Student Union at the University of Toronto.

    Instance Attributes:
        - president: The Student who is the president
        - vice_president: The Student who is vice-president
        - events: The names of events that the CSSU holds throughout the year

    Representation Invariants:
    - self.president.year_of_study >= 3
    - self.president.given_name == self.vice_president.given_name
    - self.president != self.vice_president
    - all([event.isalpha() and event != '' for event in self.events])
    """
    president: Student
    vice_president: Student
    events: list[str]

@check_contracts
@dataclass
class MarriageData:
    """
    Record the number of marriage licenses issued in a month
    
    Instance Attriubutes:
    - id: identified for this record
    - civic_cenre: short form for the name of civic centre
    - num_licenses: number of licenses issued in a month
    - month: the month these licenses were issued

    Representation Invariants:
    - data.civic_centre in {'TO', 'ET', 'NY', 'SC'}
    - data.num_licenses >= 0
    """
    id : int
    civic_centre : str
    num_licences : int
    month : datetime.date


def civic_centres(data: list[MarriageData]) -> set[str]:
    """Return a set of all the civic centres found in data.
    """
    list_of_cc = [i.civic_centre for i in data]
    return set(list_of_cc)


def civic_centre_meets_threshold(data: list[MarriageData], civic_centre: str,
                                 num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every
    month.

    You only need to worry about the rows that appear in data; don't worry about
    "missing" months.

    Preconditions:
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}

    HINT: you'll need to use a filtering comprehension.
    """
    num_for_cc = [i.num_licences for i in data if i.civic_centre == civic_centre]
    all([i >= num for i in num_for_cc])
    
def summarize_licences_by_centre(data: list[MarriageData]) -> dict[str, int]:
    """Return the total number of licences issued by each civic centre in <data>.

    Returns a dictionary where keys are civic centre names and values are the
    total number of licences issued by that civic centre.

    HINT: you will find it useful to write a function that calculates the total
    number of licences issued for a given civic centre as a parameter,
    e.g. total_licenses_for_centre(data, civic_centre).
    """











id_1660 = MarriageData(1660, 'TO', 367, datetime.date(2011, 2, 1))

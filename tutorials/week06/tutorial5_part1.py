"""CSC110 Tutorial 5: Data Classes and Loops, Exercise 1

Module Description
==================
This module contains the data classes and functions you should complete for Exercise 1.
Note that this file is very similar to tutorial4_part2.py from last week, so you should
have that file open while you're working on this exercise.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""
import csv
from dataclasses import dataclass
import datetime

from python_ta.contracts import check_contracts


###############################################################################
# The new data class
###############################################################################
@dataclass
class Delay:
    """A data type representing a specific subway delay instance.

    This corresponds to one row of the tabular data found in ttc-subway-delays.csv.

    Attributes:
        Date: The date when the following data is recorded.
        Time: The time during which the following data is recorded.
        Day: The day when the following data is recorded.
        Station: The station of the data
        Code: The code of the station
        Min Delay: Minimum delay
        Min Gap: Minimum Gap?
        Bound: Station to which the vehicle is heading
        Line: Line which the vehicle was operating in
        Vehicle: ID of the vehicle

    Representation invariants:
        - TODO: fill in representation invariants here
    """
    date: datetime.date
    time: datetime.time
    day: str
    station: str
    code: str
    min_delay: int
    min_gap: int
    bound: str
    line: str
    vehicle: int



@check_contracts
def read_csv_file(filename: str) -> tuple[list[str], list[Delay]]:
    """Return the headers and data stored in a csv file with the given filename.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of Delays (using the data class you just defined).

    Preconditions:
      - filename refers to a valid csv file with headers
        (notice that we can't express this as a Python expression)

    HINT: you can reuse almost exactly the same code as your tutorial4_part2.py from
    last week. We didn't write this code for you here because we want you to take a
    moment to review that code and copy it here yourself.

    >>> read_csv_file('/Users/idzudinsaffuan/Desktop/University of Toronto/csc110/tutorials/week06/oneline.csv')
    (['Date', 'Time', 'Day', 'Station', 'Code', 'Min Delay', 'Min Gap', 'Bound', 'Line', 'Vehicle'], \
[Delay(date=datetime.date(2014, 1, 1), time=datetime.time(0, 21), day='Wednesday', \
station='VICTORIA PARK STATION', code='MUPR1', min_delay=55, min_gap=60, bound='W', line='BD', vehicle=5111)])
    """
    with open(filename) as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [process_row(row) for row in reader]

    return (header, data)



@check_contracts
def process_row(row: list[str]) -> Delay:
    """Convert a row of subway delay data to a Delay object.

    Notes:
    - This function is very similar to the process_row function from tutorial4_part2.py,
      except now you're returning a Delay object instead of a list.
    - You'll need the str_to_date and str_to_time helper functions from
      tutorial4_part2.py; copy them into this file below process_row.

    Preconditions:
        - row has the correct format for the TTC subway delay data set

    >>> process_row(['01/01/2014', '00:21', 'Wednesday', 'VICTORIA PARK STATION', 'MUPR1', '55', '60', 'W', 'BD', \
'5111'])
    Delay(date=datetime.date(2014, 1, 1), time=datetime.time(0, 21), day='Wednesday', \
station='VICTORIA PARK STATION', code='MUPR1', min_delay=55, min_gap=60, bound='W', line='BD', vehicle=5111)
    """
    return Delay(
        str_to_date(row[0]),
        str_to_time(row[1]),
        str(row[2]),
        str(row[3]),
        str(row[4]),
        int(row[5]),
        int(row[6]),
        str(row[7]),
        str(row[8]),
        int(row[9])
    )

def str_to_date(str_date: str) -> datetime.date:
    """Return a date in the form of datetime.date
    """
    components = str_date.split('/')
    return datetime.date(int(components[2]), int(components[1]), int(components[0]))

def str_to_time(str_time: str) -> datetime.time:
    """Return a time in the form of datetime.time"""
    components = str_time.split(':')
    return datetime.time(int(components[0]), int(components[1]))

###############################################################################
# From nested lists to data classes
###############################################################################
@check_contracts
def longest_delay_v1(data: list[Delay]) -> int:
    """Return the longest delay in the given data.

    Preconditions:
        - data != []

    >>> delay_data = read_csv_file('/Users/idzudinsaffuan/Desktop/University of Toronto/csc110/tutorials/week06/twolines.csv')
    >>> longest_delay_v1(delay_data[1])
    55
    """
    return max([i.min_delay for i in data])



@check_contracts
def average_delay_v1(data: list[Delay]) -> float:
    """Return the average subway delay in data.

    Preconditions:
        - data != []

    >>> delay_data = read_csv_file('/Users/idzudinsaffuan/Desktop/University of Toronto/csc110/tutorials/week06/twolines.csv')
    >>> average_delay_v1(delay_data[1])
    29.0
    """
    sum_of_delays = sum([i.min_delay for i in data])
    return sum_of_delays / len(data)


@check_contracts
def num_delays_by_month_v1(data: list[Delay], year: int, month: int) -> int:
    """Return the number of delays that occurred in the given month and year.

    Preconditions:
        - 1 <= month <= 12
        - 2014 <= year <= 2019

    Hint: given a datetime.date value my_date, you can access three instance attributes
    to obtain the year, month, and day of the date.

        >>> my_date = datetime.date(2022, 10, 7)
        >>> my_date.year
        2022
        >>> my_date.month
        10
        >>> my_date.day
        7

    >>> delay_data = read_csv_file('/Users/idzudinsaffuan/Desktop/University of Toronto/csc110/tutorials/week06/twolines.csv')
    >>> num_delays_by_month_v1(delay_data[1], 2014, 1)
    2
    >>> num_delays_by_month_v1(delay_data[1], 2014, 2)
    0
    """
    delays_by_month = [i for i in data if i.date.month == month and i.date.year == year]
    return len(delays_by_month)


###############################################################################
# From comprehensions to loops
###############################################################################
@check_contracts
def longest_delay_v2(data: list[Delay]) -> int:
    """Return the longest delay in the given data.

    Preconditions:
        - data != []

    >>> delay_data = read_csv_file('twolines.csv')
    >>> longest_delay_v2(delay_data[1])
    55
    """


@check_contracts
def average_delay_v2(data: list[Delay]) -> float:
    """Return the average subway delay in data.

    Preconditions:
        - data != []

    >>> delay_data = read_csv_file('twolines.csv')
    >>> average_delay_v2(delay_data[1])
    29.0
    """


@check_contracts
def num_delays_by_month_v2(data: list[Delay], year: int, month: int) -> int:
    """Return the number of delays that occurred in the given month and year.

    Preconditions:
    - 1 <= month <= 12
    - 2014 <= year <= 2019

    >>> delay_data = read_csv_file('twolines.csv')
    >>> num_delays_by_month_v2(delay_data[1], 2014, 1)
    2
    >>> num_delays_by_month_v2(delay_data[1], 2014, 2)
    0
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

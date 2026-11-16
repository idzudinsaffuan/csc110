"""CSC110 Tutorial 4: Proofs, Tabular Data and For Loops, Exercise 2

Module Description
==================
Write your functions for Exercise 2 in this file.

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
import datetime


def read_csv_file(filename: str) -> tuple[list[str], list[list[str]]]:
    """Return the headers and data stored in a csv file with the given filename.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of lists of strings, where each inner list
      stores a row in the csv file.

    Hints:
    - Use open and a with statement to open the file, and csv.reader
      to read its rows, like we did in lecture.
    - next(reader) returns the next row of the reader (as a list of strings).
    - You can use a list comprehension to get the remaining rows.

    Preconditions:
      - filename refers to a valid csv file with headers
        (notice that we can't express this as a Python expression)

    >>> read_csv_file('oneline.csv')
    (['Date', 'Time', 'Day', 'Station', 'Code', 'Min Delay', 'Min Gap', 'Bound', 'Line', 'Vehicle'], \
[['01/01/2014', '00:21', 'Wednesday', 'VICTORIA PARK STATION', 'MUPR1', '55', '60', 'W', 'BD', '5111']])
    """
    with open(filename) as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [process_row(row) for row in reader]

    return (header, data)





def process_row(row: list[str]) -> list:
    """Convert a row of subway delay data to a list with more appropriate data types.

    Notes:
    - You can use int(...) to convert from a string to an integer
    - You'll need to complete the str_to_date and str_to_time functions below
      to use them here.
    - We've left some comments to help you keep track of the values you're returning.

    Preconditions:
        - row has the correct format for the TTC subway delay data set

    >>> process_row(['01/01/2014', '00:21', 'Wednesday', 'VICTORIA PARK STATION', 'MUPR1', '55', '60', 'W', 'BD', \
'5111'])
    [datetime.date(2014, 1, 1), datetime.time(0, 21), 'Wednesday', 'VICTORIA PARK STATION', 'MUPR1', 55, 60, 'W', \
'BD', 5111]
    """
    return [
        str_to_date(row[0]),  # date
        str_to_time(row[1]),  # time
        row[2],  # day
        row[3],  # station
        row[4],  # code
        int(row[5]),  # min delay
        int(row[6]),  # min gap
        row[7],  # bound
        row[8],  # line
        int(row[9])  # vehicle
    ]


def str_to_date(date_string: str) -> datetime.date:
    """Convert a string in mm/dd/yyyy format to a datetime.date.

    Hints:
    1. You can use str.split(date_string, '/') to first obtain
       the three strings corresponding to month, day, and year separately.
    2. Create a new datetime.date value by calling this type on three arguments:
       datetime.date(year, month, day).

    Preconditions:
    - date_string has format mm/dd/yyyy

    >>> str_to_date('01/01/2014')
    datetime.date(2014, 1, 1)
    """
    components = date_string.split('/')
    return datetime.date(int(components[0]), int(components[1]), int(components[2]))


def str_to_time(time_string: str) -> datetime.time:
    """Convert a string in HH:mm format to a datetime.time.

    The hours are specified in 24-hour format (from 00 to 23).

    Similar hint as str_to_date. datetime.time takes two arguments:
    hour and minute, in that order.

    >>> str_to_time('00:21')
    datetime.time(0, 21)
    """
    components = time_string.split(':')
    return datetime.time(int(components[0], int(components[1])))


###############################################################################
# Operating on the data
###############################################################################
def longest_delay(data: list[list]) -> int:
    """Return the longest delay in the given data.

    Preconditions:
    - data != []
    - data is in the format of the TTC subway delays csv file

    >>> delay_data = read_csv_file('twolines.csv')
    >>> longest_delay(delay_data[1])
    55
    """


def average_delay(data: list[list]) -> float:
    """Return the average subway delay in data.

    Preconditions:
    - data != []
    - data is in the format of the TTC subway delays csv file

    >>> delay_data = read_csv_file('twolines.csv')
    >>> average_delay(delay_data[1])
    29.0
    """


def num_delays_by_month(data: list[list], year: int, month: int) -> int:
    """Return the number of delays that occurred in the given month and year.

    Preconditions:
    - data is in the format of the TTC subway delays csv file
    - 1 <= month <= 12
    - 2014 <= year <= 2019

    >>> delay_data = read_csv_file('twolines.csv')
    >>> num_delays_by_month(delay_data[1], 2014, 1)
    2
    >>> num_delays_by_month(delay_data[1], 2014, 2)
    0
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()

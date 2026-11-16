import datetime

marriage_data = [
    [1657, 'ET', 80, datetime.date(2011, 1, 1)],
    [1658, 'NY', 136, datetime.date(2011, 1, 1)],
    [1659, 'SC', 159, datetime.date(2011, 1, 1)],
    [1660, 'TO', 367, datetime.date(2011, 1, 1)],
    [1661, 'ET', 109, datetime.date(2011, 2, 1)],
    [1662, 'NY', 150, datetime.date(2011, 2, 1)],
    [1663, 'SC', 154, datetime.date(2011, 2, 1)],
    [1664, 'TO', 383, datetime.date(2011, 2, 1)]
]

def civic_centres(data: list[list]) -> set[str]:
    """Return a set of all the civic centres found in data.

    Preconditions:
        - data satisfies all of the properties described in Exercise 2
    """
    return {row[1] for row in data}


def civic_centre_meets_threshold(data: list[list], civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data; don't worry about
    "missing" months.

    Preconditions:
        - num > 0
        - data satisfies all of the properties described in Exercise 2
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}

    HINT: you'll need to use a filtering comprehension.
    """

    january = [row[1] for row in data if (row[3] == datetime.date(2011, 1, 1) and row[2] >= num)]
    february = [row[1] for row in data if (row[3] == datetime.date(2011, 2, 1) and row[2] >= num)]
    return (civic_centre in january) and (civic_centre in february)


print(civic_centre_meets_threshold(marriage_data, 'TO', 370))


import csv

def read_csv_file(filename: str) -> tuple[list[str], list[list[str]]]:
    """Return the headers and data stored in a csv file with the given filename.

    The return value is a list consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of lists of strings, where each inner list
      stores a row in the csv file.

    Preconditions:
      - filename refers to a valid csv file with headers
        (notice that we can't express this precondition as a Python expression)
    """
    with open(filename) as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]

        return (header, data)


import datetime

def process_row(row: list[str]) -> list:
    """Return a new list containing the elements from the given row of marriage data,
    with each element converted to more appropriate data types, if needed.

    Notes:
    - You can use int(...) to convert from a string to an integer
    - You'll need to complete the helper function str_to_date below
      to use it here.

    Preconditions:
        - row has the correct format for the marriage licence dataset

    >>> data = read_csv_file('marriage_data.csv')
    >>> process_row(data[1][1])
    [1658, 'NY', 136, datetime.date(2011, 1, 1)]
    """
    return [int(row[0]), row[1], int(row[2]), str_to_date(row[3])]
    




def str_to_date(date_string: str) -> datetime.date:
    """Convert a string in yyyy/mm/dd format to a datetime.date.

    Hints:
    1. You can use str.split(date_string, '/') to first obtain a list containing
       the three strings corresponding to month, day, and year separately.
    2. Convert the three strings into integers and use them to create a new datetime.date value
        by calling this type on three arguments: datetime.date(year, month, day).

    Preconditions:
    - date_string has format yyyy/mm/dd

    >>> str_to_date('2014/01/01')
    datetime.date(2014, 1, 1)
    """
    components = date_string.split('/')
    return datetime.date(int(components[0]), int(components[1]), int(components[2]))


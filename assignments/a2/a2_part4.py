"""CSC110 Fall 2026 Assignment 2, Part 4: Toronto paramedic incidents

Module Description
==================
The data in paramedic-incidents.csv is a cleaned teaching subset of the City
of Toronto's Paramedic Services Incident Data, used under the Open Government
Licence - Toronto:
https://open.toronto.ca/dataset/paramedic-services-incident-data/

It is not a representative sample. See the assignment handout.

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
from dataclasses import dataclass


@dataclass
class Incident:
    """A Toronto Paramedic Services incident.

    Instance Attributes:
        date: The date the first paramedic unit was assigned to the incident.
        time: The time the first paramedic unit was assigned to the incident.
        incident_type: The general category of the incident.
        priority: The triaged priority number assigned when the call was dispatched.
        units_arrived: The number of paramedic units that arrived on scene.
        fsa: The first three characters of the postal code where the incident occurred.

    Representation Invariants:
        - units_arrived > 0
        - incident_type in {'Medical', 'Motor Vehicle Collision', 'Fire', 'Emergency Transfer', 'Airport Standby'}
    """

    date: datetime.date
    time: datetime.time
    incident_type: str
    priority: int
    units_arrived: int
    fsa: str


def read_csv_file(filename: str) -> tuple[list[str], list[Incident]]:
    """Return the header and incident rows contained in filename.

    Use process_row to convert every non-header row to an Incident.

    >>> read_csv_file('assignments/a2/datasets/incidents/oneline.csv')
    (['Date', 'Time', 'Incident Type', 'Priority', 'Units Arrived', 'FSA'], \
[Incident(date=datetime.date(2021, 1, 1), time=datetime.time(0, 0), incident_type='Medical', \
priority=3, units_arrived=1, fsa='M4G')])
    """
    with open(filename) as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [process_row(row) for row in reader]

    return (header, data)


def process_row(row: list[str]) -> Incident:
    """Return an Incident made from one CSV row.

    Preconditions:
        - len(row) == 6
        - row has the format described in the Part 4 handout

    >>> process_row(['2021-01-01', '00:19', 'Motor Vehicle Collision', '4', '1', 'M5V'])
    Incident(date=datetime.date(2021, 1, 1), time=datetime.time(0, 19), \
incident_type='Motor Vehicle Collision', priority=4, units_arrived=1, fsa='M5V')
    """
    return Incident(
        str_to_date(row[0]),
        str_to_time(row[1]),
        str(row[2]),
        int(row[3]),
        int(row[4]),
        str(row[5])
    )


def str_to_date(date_string: str) -> datetime.date:
    """Return the date represented by date_string in YYYY-MM-DD format.

    Preconditions:
        - date_string is a valid date in YYYY-MM-DD format

    >>> str_to_date('2021-01-01')
    datetime.date(2021, 1, 1)
    """
    components = date_string.split('-')
    return datetime.date(int(components[0]), int(components[1]), int(components[2]))


def str_to_time(time_string: str) -> datetime.time:
    """Return the time represented by time_string in HH:MM format.

    Preconditions:
        - time_string is a valid time in HH:MM format

    >>> str_to_time('00:19')
    datetime.time(0, 19)
    """
    components = time_string.split(':')
    return datetime.time(int(components[0]), int(components[1]))


def incidents_by_type(data: list[Incident]) -> dict[str, int]:
    """Return a mapping from each incident type in data to its frequency.

    >>> sample = [Incident(datetime.date(2025, 1, 1), datetime.time(9, 0),
    ...                    'Medical', 3, 1, 'M5S'),
    ...           Incident(datetime.date(2025, 1, 2), datetime.time(10, 0),
    ...                    'Medical', 4, 2, 'M5S')]
    >>> incidents_by_type(sample)
    {'Medical': 2}
    >>> incident_data = read_csv_file('assignments/a2/datasets/incidents/fivelines.csv')
    >>> result = incidents_by_type(incident_data[1])
    >>> result == {'Medical': 2, 'Motor Vehicle Collision': 1, 'Emergency Transfer': 1, 'Fire': 1}
    True
    """
    incidents_type_so_far = set()
    for i in data:
        incidents_type_so_far.add(i.incident_type)

    dict_so_far = {}
    for j in incidents_type_so_far:
        if j not in dict_so_far:
            dict_so_far[j] = 0
    for j in incidents_type_so_far:
        for i in data:
            if i.incident_type == j:
                dict_so_far[j] = dict_so_far[j] + 1

    return dict_so_far


def num_incidents_in_fsa(data: list[Incident], fsa: str) -> int:
    """Return the number of incidents in data that occurred in fsa.

    Preconditions:
        - len(fsa) == 3

    >>> incident_data = read_csv_file('assignments/a2/datasets/incidents/fivelines.csv')
    >>> num_incidents_in_fsa(incident_data[1], 'M5V')
    1
    >>> num_incidents_in_fsa(incident_data[1], 'M5S')
    0
    """
    num_incidents_so_far = 0
    for i in data:
        if i.fsa == fsa:
            num_incidents_so_far += 1

    return num_incidents_so_far


def num_incidents_by_month(data: list[Incident], year: int, month: int) -> int:
    """Return the number of incidents in data from the given year and month.

    Preconditions:
        - 1 <= month <= 12

    >>> incident_data = read_csv_file('assignments/a2/datasets/incidents/fivelines.csv')
    >>> num_incidents_by_month(incident_data[1], 2021, 1)
    5
    >>> num_incidents_by_month(incident_data[1], 2021, 2)
    0
    """
    incidents_so_far = 0
    for i in data:
        if i.date.year == year and i.date.month == month:
            incidents_so_far = incidents_so_far + 1

    return incidents_so_far


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In VSCode, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta

    python_ta.check_all(config={'extra-imports': ['csv', 'datetime', 'dataclasses'],
                                'allowed-io': ['read_csv_file'],
                                'max-line-length': 120})

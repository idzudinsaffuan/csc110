from dataclasses import dataclass
import datetime


@dataclass
class MarriageData:
    """A record of the number of marriage licenses issued in a civic centre
    in a given month.

    Instance Attributes:
      - id: a unique identifier for the record
      - civic_centre: the name of the civic centre
      - num_licenses: the number of licenses issued
      - month: the month these licenses were issued

    Representation Invariant omitted.
    """
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date

def filter_by_name(data: list[MarriageData], civic_centre: str) -> list[MarriageData]:
    """Return all rows in data whose civic_centre is civic_centre.

    Equivalent to:
      [row for row in data if row.civic_centre == civic_centre]
    """
    list_so_far = []
    for row in data:
        if row.civic_centre == civic_centre:
            list_so_far.append(row)

    return list_so_far

def num_issued_by(data: list[MarriageData], civic_centre: str) -> set[int]:
    """Return the unique numbers of marriage licenses issued per month at the given
    civic_centre.

    Equivalent to:
      {row.num_licenses for row in data if row.civic_centre == civic_centre}
    """
    set_so_far = set()
    for row in data:
        if row.civic_centre == civic_centre:
            set_so_far.add(row.num_licenses)

    return set_so_far

def marriages_by_centre(data: list[MarriageData],
                        month: datetime.date) -> dict[str, int]:
    """Return a mapping from civic centre name to the number of marriage licenses
    issued by that centre in the given month.

    Preconditions:
        - Each civic centre has only one row of MarriageData for the given month.

    Equivalent to:
      {row.civic_centre: row.num_licenses for row in data if row.month == month}
    """
    mapping_so_far = {}
    for row in data:
        if row.civic_centre not in mapping_so_far:
            mapping_so_far[row.civic_centre] = row.num_licenses
        else:
            r

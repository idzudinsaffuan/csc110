"""CSC110 Fall 2026 Assignment 2, Part 2: Symptom-report debugging

Instructions (READ THIS FIRST!)
===============================

This Python module contains the program and tests described in Assignment 2,
Part 2. You can run this file as given to see the pytest report. Your task is
to fix the errors in the program so that each test passes (see the assignment
handout for details). The tests and their expected values are correct, so do
not change them.

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
import pytest


PUNCTUATION = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~'

# A small fictional scale used only for this programming exercise.
WORD_TO_SEVERITY = {
    'comfortable': 0.5,
    'mild': 1.0,
    'uncomfortable': 2.0,
    'moderate': 2.5,
    'painful': 3.0,
    'severe': 4.0,
}


def assess_symptom_report(report: str) -> tuple[str, float]:
    """Return the urgency label and average severity for report.

    Severity words not in WORD_TO_SEVERITY are ignored. An average below 1.5
    is labelled 'routine', an average below 2.5 is labelled 'monitor', and an
    average of at least 2.5 is labelled 'urgent'.

    Preconditions:
        - report contains at least one word in WORD_TO_SEVERITY
    """
    word_list = clean_text(report)
    occurrences = count_severity_words(word_list)
    average = calculate_average_severity(occurrences)

    if average < 1.5:
        return 'routine', average
    elif average < 2.5:
        return 'monitor', average
    else:
        return 'urgent', average


def clean_text(text: str) -> list[str]:
    """Return the words in text, with punctuation removed and letters lowercased."""
    for punctuation_mark in PUNCTUATION:
        text = text.replace(punctuation_mark, ' ')

    txt = text.lower()
    return txt.split() #### txt



def count_severity_words(word_list: list[str]) -> dict[str, int]:
    """Return a frequency mapping of severity words in word_list."""
    occurrences_so_far = {}

    for word in word_list:
        if word in WORD_TO_SEVERITY:
            if word not in occurrences_so_far:
                occurrences_so_far[word] = 0
                occurrences_so_far[word] = occurrences_so_far[word] + 1
            else: occurrences_so_far[word] = occurrences_so_far[word] + 1 ### add else

    return occurrences_so_far


def calculate_average_severity(occurrences: dict[str, int]) -> float:
    """Return the average severity of the given word occurrences.

    Preconditions:
        - occurrences != {}
        - all({occurrences[word] >= 1 for word in occurrences})
    """
    num_words = sum([occurrences[word] for word in occurrences])
    total = sum([WORD_TO_SEVERITY[word] * occurrences[word] for word in occurrences])
    return total / num_words


def read_symptom_report(filename: str) -> str:
    """Return the fictional symptom report stored in filename."""
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        row = next(reader)
        return row[len(row) - 1]


###############################################################################
# Unit Tests
#
# The tests below are correct. Do not modify them; fix the program above instead.
###############################################################################
def test_routine_report() -> None:
    """Test a report containing lowercase, non-repeated severity words."""
    # DO NOT MODIFY ANY OF THE LINES IN THIS TEST
    report = read_symptom_report('assignments/a2/datasets/assessments/routine_report.csv')
    actual = assess_symptom_report(report)
    assert actual[0] == 'routine'
    assert actual[1] == pytest.approx(0.75)


def test_monitor_report() -> None:
    """Test a report containing capitalized severity words."""
    # DO NOT MODIFY ANY OF THE LINES IN THIS TEST
    report = read_symptom_report('assignments/a2/datasets/assessments/monitor_report.csv')
    actual = assess_symptom_report(report)
    assert actual[0] == 'monitor'
    assert actual[1] == pytest.approx(2.0)


def test_urgent_report() -> None:
    """Test a report containing a repeated severity word."""
    # DO NOT MODIFY ANY OF THE LINES IN THIS TEST
    report = read_symptom_report('assignments/a2/datasets/assessments/urgent_report.csv')
    actual = assess_symptom_report(report)
    assert actual[0] == 'urgent'
    assert actual[1] == pytest.approx(3.0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    pytest.main(['assignments/a2/a2_part2.py', '-v'])

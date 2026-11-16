"""CSC110 Fall 2026 Assignment 2, Part 3: Student tests

Module Description
==================
Complete each test below. Each test should check only the behaviour named in
its docstring. To earn full credit, each test only needs to catch one buggy
implementation supplied by our auto-marking tests.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""

import pytest
from hypothesis import given
from hypothesis.strategies import integers, text, tuples

from a2_part3 import (
    PatientAssessment,
    DoctorChart,
    assessment_difference,
    update_notes,
    add_patient,
)


ASSESSMENT_SCORES = tuples(integers(min_value=0, max_value=4),
                           integers(min_value=0, max_value=4),
                           integers(min_value=0, max_value=4))


@given(scores1=ASSESSMENT_SCORES, scores2=ASSESSMENT_SCORES)
def test_assessment_difference_symmetry(scores1: tuple[int, int, int],
                                        scores2: tuple[int, int, int]) -> None:
    """Test that swapping the two assessments does not change the difference
    computed by assessment_difference."""
    actual = assessment_difference(scores1, scores2)
    expected = assessment_difference(scores2, scores1)
    assert actual == expected


@given(patient_id=integers(min_value=1, max_value=1000),
       scores=ASSESSMENT_SCORES,
       notes=text(min_size=1, max_size=20),
       new_note=text(min_size=1, max_size=20))
def test_update_notes_correctness(patient_id: int, scores: tuple[int, int, int],
                                  notes: str, new_note: str) -> None:
    """Test that update_notes returns the correct PatientAssessment."""
    TestPatient = PatientAssessment(patient_id, scores, notes)
    updated = update_notes(TestPatient, new_note)
    expected = PatientAssessment(patient_id, scores, notes + ' ' + new_note)
    actual = updated
    assert expected == actual


@given(patient_id=integers(min_value=1, max_value=1000),
       scores=ASSESSMENT_SCORES,
       notes=text(min_size=1, max_size=20),
       new_note=text(min_size=1, max_size=20))
def test_update_notes_no_mutation(patient_id: int, scores: tuple[int, int, int],
                                  notes: str, new_note: str) -> None:
    """Test that update_notes does not mutate the argument patient assessment."""
    TestPatient = PatientAssessment(patient_id, scores, notes)
    update_notes(TestPatient, new_note)
    assert TestPatient == PatientAssessment(patient_id, scores, notes)


def test_add_patient_mutation() -> None:
    """Test that add_patient mutates the given DoctorChart correctly."""
    chart = DoctorChart('test', [])
    patient = PatientAssessment(1, (0, 0, 0), 'notes')
    add_patient(chart, patient)
    assert chart.patients == [patient]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    pytest.main(['assignments/a2/test_a2_part3.py', '--disable-warnings'])

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In VSCode, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    #
    python_ta.check_all(config={
        'extra-imports': ['pytest', 'hypothesis', 'hypothesis.strategies', 'a2_part3'],
        'disable': ['C9103', 'W1114'],
        'max-line-length': 120,
    })

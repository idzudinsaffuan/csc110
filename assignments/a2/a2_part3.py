"""CSC110 Fall 2026 Assignment 2, Part 3: Patient assessment functions

Module Description
==================
This module contains the functions described in Part 3. THIS FILE IS NOT GRADED.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""

from dataclasses import dataclass


@dataclass
class PatientAssessment:
    """A patient's symptom assessment.

    Instance Attributes:
        - patient_id: a unique positive identifier for the patient
        - scores: discomfort, mobility, and fatigue scores, in that order
        - notes: notes recorded with this assessment

    Representation Invariants:
        - self.patient_id > 0
        - all({0 <= score <= 4 for score in self.scores})
    """

    patient_id: int
    scores: tuple[int, int, int]
    notes: str


@dataclass
class DoctorChart:
    """A doctor's chart of patient assessments.

    Instance Attributes:
        - doctor: the doctor's name
        - patients: the assessments on this chart

    Representation Invariants:
        - self.doctor != ''
        - len({patient.patient_id for patient in self.patients}) == len(self.patients)
    """

    doctor: str
    patients: list[PatientAssessment]


def assessment_difference(scores1: tuple[int, int, int],
                          scores2: tuple[int, int, int]) -> int:
    """Return the total difference between two symptom assessments.

    Preconditions:
        - all({0 <= score <= 4 for score in scores1})
        - all({0 <= score <= 4 for score in scores2})
    Postconditions:
        - 0 <= $return_value <= 12
        - ($return_value == 0) == (scores1 == scores2)
    """
    return (abs(scores1[0] - scores2[0])
            + abs(scores1[1] - scores2[1])
            + abs(scores1[2] - scores2[2]))


def update_notes(patient: PatientAssessment, new_note: str) -> PatientAssessment:
    """Return a new assessment with new_note appended to patient's notes.

    A single space is inserted between the existing notes and new_note. The
    given patient is not mutated.

    Preconditions:
        - patient.notes != ''
        - new_note != ''
    """
    return PatientAssessment(patient.patient_id, patient.scores, patient.notes + ' ' + new_note)




def add_patient(chart: DoctorChart, patient: PatientAssessment) -> None:
    """Add patient to the end of chart's patients, mutating chart.

    Preconditions:
        - all({other.patient_id != patient.patient_id for other in chart.patients})
    """
    return chart.patients.append(patient)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

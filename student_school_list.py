# ECOR 1042 Lab 3 - Individual submission for student_school_list function
# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Lucas Warburton"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101276823"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-018"


# ==========================================#
# Place your student_school_list function after this line

def student_school_list(file_name: str, school: str) -> list[dict]:
    """
    Returns a list of students that attended the given school.

    Preconditions: N/A

    >>> student_school_list('student-mat.csv', 'GP')
    [ {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3,
      'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },
      {another element},
      …
    ]
    >>> student_school_list('student-mat.csv', 'School')
    []
    """
    infile = open(file_name, "r")
    students, headers = [], []

    for line in infile:
        line = line[:-1].split(",")
        if not headers:
            headers = line[1:]
        elif line[0] == school:
            students += [dict(zip(headers, [int(line[1]), float(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8])]))]
    return students

# Do NOT include a main script in your submission

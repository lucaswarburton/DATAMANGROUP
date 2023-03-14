# ECOR 1042 Lab 3 - Individual submission for student_age_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Samuel Burt"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101260404"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-018"

#==========================================#
# Place your student_age_list function after this line


def student_age_list(file_name: str, age: int) -> list[dict]:
    """
    Returns a list of students of a certain age from a given data sheet.
    
    Preconditions: N/A
    
    >>> student_age_list('student-mat.csv', 15)
    [ {'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10,
      'G1': 7, 'G2': 8, 'G3': 10},
      {another element},
      …
    ] 
    >>> student_age_list('student-mat.csv', 99)
    []
    """
    file = open(file_name, "r")
    students, keys = [], []
    for line in file:
        if keys:
            values = [line[:-1].split(",")[0]] +\
                     [int(line[:-1].split(",")[1])] +\
                     [float(line[:-1].split(",")[2])] +\
                     [int(item) for item in (line[:-1].split(","))[3:]]
            student = dict(zip(keys, values))
            if student['Age'] == age:
                del student['Age']
                students += [student]
        else:
            keys = line[1:-1].split(",")
    return students


# Do NOT include a main script in your submission

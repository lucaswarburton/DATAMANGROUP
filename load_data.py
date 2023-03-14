# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Lucas Warburton, Alexandre Radaelli, Samuel Burt, Agri Tahami Nasab"

# Update "" with your team (e.g. T102)
__team__ = "T018"


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


# ==========================================#
# Place your student_health_list function after this line
def student_health_list(file_name: str, health: int) -> list[dict]:
    """Returns a list of dictionaries of the students who have the same health
    value thats inputed into the function


    >>> student_health_list('student-mat.csv', 2)
    [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10,
    'G1': 9, 'G2': 11, 'G3': 7},
    {another element},
    …
    ]

    >>>student_health_list('student-mat.csv', 8)
    []
    """
    studentinfo = open(file_name, 'r')
    students, keys = [], []

    for line in studentinfo:
        if keys:
            line = line[:-1].split(',')
            if int(line[4]) == health:
                student = {
                    keys[0]: str(line[0]),
                    keys[1]: int(line[1]),
                    keys[2]: float(line[2]),
                    keys[3]: int(line[3]),
                    keys[5]: int(line[5]),
                    keys[6]: int(line[6]),
                    keys[7]: int(line[7]),
                    keys[8]: int(line[8]),
                }
                students += [student]

        else:
            keys = line[1:-1].split(',')

    return students


# ==========================================#
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
            values = [line[:-1].split(",")[0]] + \
                     [int(line[:-1].split(",")[1])] + \
                     [float(line[:-1].split(",")[2])] + \
                     [int(item) for item in (line[:-1].split(","))[3:]]
            student = dict(zip(keys, values))
            if student['Age'] == age:
                del student['Age']
                students += [student]
        else:
            keys = line[1:-1].split(",")
    return students


# ==========================================#
# Place your student_failures_list function after this line

def student_failures_list(data: str, failure: int) -> list[dict]:
    """Returns a list of dictionaries composed of students in the data (Parameter 1) who have the same number f failures as Parameter 2.

    Preconditions: N/A

    >>> student_failures_list('student-mat.csv', 3)
    [{'School': 'GP', 'Age': 15, 'Study Time': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}

    {'School': 'GP', 'Age': 17, 'Study Time': 1.0, 'Health': 5, 'Absences': 16, 'G1': 6, 'G2': 5, 'G3': 5}
    ...
    ]

    >>> student_failures_list('student-mat.csv', 20)
    []

    """

    jlst = []
    infile = open(data, "r")
    flag = True

    for line in infile:
        if flag:
            flag = False
        else:
            students = {}
            lst = line[:-1].split(",")

            students['School'] = str(lst[0])
            students['Age'] = int(lst[1])
            students['Study Time'] = float(lst[2])
            students['Failures'] = int(lst[3])
            students['Health'] = int(lst[4])
            students['Absences'] = int(lst[5])
            students['G1'] = int(lst[6])
            students['G2'] = int(lst[7])
            students['G3'] = int(lst[8])

            jlst += [students]

    flst = []

    for i in jlst:
        if failure == int(i['Failures']):
            del i['Failures']
            flst.append(i)

    return flst


# ==========================================#
# Place your load_data function after this line

def load_data(file_name: str, attribute: tuple) -> list[dict]:
    """
    Returns a list of students, filtered according to the tuple and
    missing the information it is filtered by.

    Preconditions: N/A

    >>>load_data("student-mat.csv", ("School", "GP"))
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3,
      'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },
      {another element},
      …
    ]
    >>>load_data('student-mat.csv', (‘All’, -1))
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
      'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14},
      {another element},
     …
    ]
    """
    infile = open(file_name, "r")
    students, headers, is_all, attribute_index = [], [], False, 0

    for line in infile:
        line = line[:-1].strip().split(",")
        if headers:
            if attribute_index == 0:
                pass
            elif attribute_index == 2:
                line[attribute_index] = float(line[attribute_index])
            else:
                line[attribute_index] = int(line[attribute_index])
        if not headers:
            headers = line
            if attribute[0].lower() == "all":
                is_all = True
            elif attribute[0] not in ['School', 'Age', 'Health', 'Failures']:
                print("Invalid Value")
                return []
            else:
                attribute_index = headers.index(attribute[0])
                print(headers[0], headers[1], headers[2], headers[3], headers[4], headers[5])
                del headers[attribute_index]
        elif line[attribute_index] == attribute[1] or is_all:
            stats = [str(line[0]), int(line[1]), float(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6]),
                     int(line[7]), int(line[8])]
            if not is_all:
                del stats[attribute_index]
            students += [dict(zip(headers, stats))]
    return students


# ==========================================#
# Place your add_average function after this line

def add_average(students: list[dict]) -> list[dict]:
    """
    Adds an entry to each dictionary containing the average grade of the student.

    Preconditions: N/A

    >>>add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}])
    [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_avg': 5.67}]
    """
    for i in students:
        i["G_avg"] = round((i["G1"] + i["G2"] + i["G3"]) / 3, 2)
    return students

# Do NOT include a main script in your submission

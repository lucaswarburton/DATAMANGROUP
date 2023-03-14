# ECOR 1042 Lab 3 - Individual submission for student_health_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Agri Tahami Nasab"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101259140"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-018"

#==========================================#
# Place your student_health_list function after this line



# Do NOT include a main script in your submission
def student_health_list(file_name : str, health: int) ->list[dict]:
    """Returns a list of dictionaries of the students who have the same health
    value thats inputed into the function 
    
    {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },
    {another element},
    …
    """
    studentinfo = open (file_name, 'r')
    students, keys =[], []
   
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
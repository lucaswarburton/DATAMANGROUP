# ECOR 1042 Lab 3 - Individual submission for student_failures_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Alexandre Radaelli"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101268587"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-018"

#==========================================#
# Place your student_failures_list function after this line

def student_failures_list(data:str, failure:int) -> list[dict] :
  """Returns a list of dictionaries composed of students in the data(Parameter 1) who have the same number f failures as Parameter 2.
  
  Preconditions: N/A
  
  >>> student_failures_list('student-mat.csv', 3)
  [{'School': 'GP', 'Age': 15, 'Study Time': 2.0, 'Health': 3, 'Abscences': 10, 'G1': 7, 'G2': 8, 'G3': 10}
  
  {'School': 'GP', 'Age': 17, 'Study Time': 1.0, 'Health': 5, 'Abscences': 16, 'G1': 6, 'G2': 5, 'G3': 5}
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
      
      students['School']     = str(lst[0])
      students['Age']        = int(lst[1])
      students['Study Time'] = float(lst[2])
      students['Failures']   = int(lst[3])
      students['Health']     = int(lst[4])
      students['Abscences']  = int(lst[5])
      students['G1']         = int(lst[6])
      students['G2']         = int(lst[7])
      students['G3']         = int(lst[8])
      
      jlst += [students]
  
  flst = []
  
  for i in jlst:
    if failure == int(i['Failures']):
      del i['Failures']
      flst.append(i)
      
  return flst

# Do NOT include a main script in your submission
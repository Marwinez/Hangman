# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']
subjects = set({})
subjects.update(Belov)
subjects.update(Smith)
subjects.update(Sarada)
print(len(subjects))

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'

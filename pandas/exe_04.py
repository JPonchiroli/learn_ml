import pandas as pd

students_dc = {'Name':['Jose', 'Maria', 'Robert', 'Alice'],
            'Grade':[7, 5, 4, 9],
            'Approved':['Yes', 'No', 'No', 'Yes']}

students_df = pd.DataFrame(students_dc)

print(students_df.head()) # Return the data of dataframe

print(students_df.shape) # Return number of lines and columns

print(students_df.describe()) # Overview of data
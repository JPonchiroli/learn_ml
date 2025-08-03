import pandas as pd

students_dc = {'Name':['Jose', 'Maria', 'Robert', 'Alice'],
            'Grade':[7, 5, 4, 9],
            'Approved':['Yes', 'No', 'No', 'Yes']}

students_df = pd.DataFrame(students_dc)

first_lines = students_df.loc[0:2]

approved_students_df = students_df.loc[students_df['Approved'] == 'Yes']
not_approved_students_df = students_df.loc[students_df['Approved'] != 'Yes']

print(approved_students_df)
print(not_approved_students_df)
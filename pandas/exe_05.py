import pandas as pd
import numpy as np

students_dc = {'Name':['Jose', 'Maria', 'Robert', 'Alice'],
            'Grade':[7, 5, 4, 9],
            'Approved':['Yes', 'No', 'No', 'Yes']}

students_df = pd.DataFrame(students_dc)

print(students_df['Name']) # Filter Columns

print(students_df.loc[[0, 2]]) # Filter Lines

print(students_df.loc[students_df['Grade'] >= 6])
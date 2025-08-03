import pandas as pd
import numpy as np

students = {'Name':['Jose', 'Maria', 'Robert', 'Alice'],
            'Grade':[7, 5, 4, 9],
            'Approved':['Yes', 'No', 'No', 'Yes']}

dataframe = pd.DataFrame(students)

_object1 = pd.Series([3, 6, 9, 12, 15]) # Create array with indices, only unidimensional

array = np.array([4, 8, 16, 24])
_object2 = pd.Series(array)
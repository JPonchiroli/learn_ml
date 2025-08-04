import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/joaop/projetos/learn_ml/files/athlete_events.csv')

data.boxplot(column = ['Age', 'Height', 'Weight'])
plt.show()
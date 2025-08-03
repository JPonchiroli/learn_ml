import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/joaop/projetos/learn_ml/pandas/files/athlete_events.csv')

athletes_df = pd.DataFrame(data)

male_athletes_df = athletes_df.loc[athletes_df['Sex'] == 'M']
female_athletes_df = athletes_df.loc[athletes_df['Sex'] == 'F']

male_athletes_df.hist(column = 'Weight', bins = 100)
female_athletes_df.hist(column = 'Weight', bins = 100)
plt.show() # Numbers columns only
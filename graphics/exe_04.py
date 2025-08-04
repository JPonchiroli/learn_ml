import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('C:/Users/joaop/projetos/learn_ml/files/athlete_events.csv')

athletes_df = pd.DataFrame(data)

male_athletes_df = athletes_df.loc[athletes_df['Sex'] == 'M']

male_athletes_height_df = male_athletes_df['Height']
male_athletes_weight_df = male_athletes_df['Weight']

plt.scatter(male_athletes_height_df, male_athletes_weight_df)
plt.show()
import pandas as pd
from sklearn.model_selection import train_test_split # evn necessary necessary sklearn-env\Scripts\activate
from sklearn.ensemble import ExtraTreesClassifier

data = pd.read_csv('C:/Users/joaop/projetos/learn_ml/files/wine_dataset.csv')

data['style'] = data['style'].replace('red', 0)
data['style'] = data['style'].replace('white', 1)

print(data.head())

y = data['style']
x = data.drop('style', axis = 1)

# Creating the data of train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

model = ExtraTreesClassifier()
model.fit(x_train, y_train)

result = model.score(x_test, y_test)
print('Accuracy:', result)

print(y_test[400:403])
print(x_test[400:403])

forecast = model.predict(x_test[400:403])
print(forecast)
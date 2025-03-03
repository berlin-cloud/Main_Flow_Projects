import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('student/student-mat.csv', sep=';')

print(" The head of the dataset is: \n", data.head())

print("\n\n The check of missing values : \n", data.isnull().sum())

print("\n\n the data type of column values:\n ", data.dtypes)

print("\n\n The Size of dataset: ", data.shape)

data = data.dropna()
print("\n\n Handling missing values: \n", data)

data = data.drop_duplicates()
print("\n\n Removing duplicate entries : \n", data)

print("\n\n The average score of math G3 is ", data['G3'].mean())

print('\n\n The number of students who scored more than 15 in their final grade G3 is ', data[data['G3'] > 15].shape[0])

print("\n\n The correlation between study time and G3 is ", data['studytime'].corr(data['G3']))

print("\n\n the gender that has a higher average final grade (G3) is \n", data.groupby('sex')['G3'].mean())

plt.figure(figsize = (9,9))


plt.subplot(2,2,1)
plt.hist(data['G3'], bins = 20, edgecolor = 'black', color = 'red')
plt.xlabel('G3 marks')
plt.ylabel('Frequency')
plt.grid(True)
plt.title('Histogram of G3')

plt.subplot(2,2,2)
plt.scatter(data['studytime'], data['G3'], color = "cyan", edgecolor = 'black')
plt.xlabel('studytime')
plt.ylabel('G3 marks')
plt.grid(True)
plt.title('Scatter plot of studytime and G3')

plt.subplot(2,2,3)
avg = data.groupby('sex')['G3'].mean()
plt.bar(avg.index, avg.values, color = 'lightgreen', edgecolor = 'black')
plt.xlabel('Gender')
plt.ylabel('G3 marks')
plt.grid(True)
plt.title('Bar chart comparing average scores of male and female students')

plt.tight_layout()
plt.show()
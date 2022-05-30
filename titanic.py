import pandas as pd
import numpy as np

data_csv = pd.read_csv('titanic.csv')
main_data = pd.DataFrame(data_csv)
main_data.fillna('NaN')
print(main_data)
main_data.columns.values.tolist()

a = data_csv[['Age', 'Sex']][0:5]
a['Relatives'] = data_csv['SibSp'] + data_csv['Parch']

data_csv[['Age', 'Sex']][440:450:2]

survived = data_csv['Survived'].sum()
survived_female = data_csv[data_csv['Sex'] == 'female']['Survived'].sum()
survived_male = survived - survived_female
print(f'Выжило мужчин: {survived_male}, женщин: {survived_female}, всего: {survived}')

data_csv.loc[data_csv['Pclass'] == 1,'Pclass'] = 'Элита'
data_csv.loc[data_csv['Pclass'] == 2,'Pclass'] = 'Средний класс'
data_csv.loc[data_csv['Pclass'] == 3,'Pclass'] = 'Работяга'
data_csv.loc[data_csv['Fare'] < 20, 'Fare_bin'] = 'Дешево'
data_csv.loc[data_csv['Fare'] >= 20, 'Fare_bin'] = 'Дорого'

data_csv[data_csv.isna()['Age']]
data_csv.dropna(subset=['Age', 'Sex'])



import matplotlib.pyplot as plt

x = sorted(set(i for i in main_data['Age'] if i > 0))
y_1 = [list(main_data['Age']).count(i) for i in x]

plt.figure(figsize=(20,5))
plt.xlabel('ages of people')
plt.ylabel('count of people')
plt.bar(x,y_1,width=0.5)



y_2 = [i for i in main_data['Age'].where(main_data['Survived'] > 0 ) if i > 0]

y_3 = [y_2.count(i) for i in x]

plt.figure(figsize=(20,5))
plt.bar(x,y_3,width=0.5);



import numpy as np
a = np.vstack([y_1,y_3])
y_4 = [round((a[1][i]/a[0][i])*100) for i in range(0,len(y_1)) ]

plt.figure(figsize=(20,5))
plt.bar(x,y_4,width=0.4);









data_1 = main_data[['Pclass','Sex']]
datam_1 = len(data_1[(data_1['Pclass'] == 1) & (data_1['Sex'] == 'male')])
datam_12 = len(data_1[data_1['Pclass'] == 1]) - datam_1

datam_2 = len(data_1[(data_1['Pclass'] == 2) & (data_1['Sex'] == 'male')])
datam_22 = len(data_1[data_1['Pclass'] == 2]) - datam_2

datam_3 = len(data_1[(data_1['Pclass'] == 3) & (data_1['Sex'] == 'male')])
datam_32 = len(data_1[data_1['Pclass'] == 3]) - datam_3

x_1 = [datam_1,datam_2,datam_3]
x_2 = [datam_12,datam_22,datam_32]
z = [1,2,3]
fig, ax = plt.subplots()

ax.bar([i + 0.2 for i in z], x_1, width = 0.4)
ax.bar([i - 0.2 for i in z], x_2, width = 0.4)

ax.set_facecolor('seashell')
fig.set_figwidth(12)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure
fig.set_facecolor('floralwhite')

plt.show()



vals = [len(main_data[main_data['Embarked']=='C']),len(main_data[main_data['Embarked']=='S']),len(main_data[main_data['Embarked']=='Q'])]
labels = [i for i in set(main_data['Embarked']) if i==i]
labels1 = [round(i/len(main_data['Embarked'])*100) for i in vals]
labels2 = [i + ' ' + str(j) + '%' for [i,j] in [[labels.pop(),labels1.pop()] for i in range(3)]]

plt.pie(vals,labels = labels2,radius=2);

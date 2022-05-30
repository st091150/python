from matplotlib import projections
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns
import pandas as pd
from dataclasses import make_dataclass

filename = 'anime.csv'
default_missing = pd._libs.parsers.STR_NA_VALUES
default_missing.add('-')
loaded_df = pd.read_csv(filename, thousands=',',na_values=default_missing)
df = loaded_df.copy()
s = pd.Series(df['Episodes'])
df['Episodes'] = pd.to_numeric(s, errors='coerce')

df.head(10)
df.dtypes
df.columns = [str.lower() for str in df.columns]

df.head(10)
df.describe(percentiles=[.25,.75,.9])

themes = [str(row).split(',') for row in df['theme']]
print(pd.DataFrame({'theme': [t for theme in themes for t in theme]}).theme.value_counts().sort_values())
geners = [str(row).split(',') for row in df['genre']]
print(pd.DataFrame({'genre': [t for gener in geners for t in gener]}).genre.value_counts().sort_values())
print(df.production.value_counts().sort_values())
print(df.source.value_counts().sort_values())

df.drop('airdate', inplace=True, axis=1)
df.dropna(how="any", inplace=True)
df.reset_index(drop=True, inplace=True)
s = pd.Series(df['episodes'], dtype="Int64")
df['episodes'] = pd.to_numeric(s)

def count(t):
  counts = []
  names = []
  for name,count in t.items():
      if len(counts)>0 and counts[-1] == count:
          names[len(counts) -1]+=', '+str(name)
      else:
          names.append(str(name))
          counts.append(count)
  return names, counts

  t= df.production.value_counts().sort_values()
names, counts = count(t)

print(f'Студия {names[-1]} выпустила {counts[-1]}, что является максимальным количеством аниме в датасете.')
plt.xticks(rotation=-90)
plt.bar(names,counts)

t= df.episodes.value_counts().sort_values()
names, counts = count(t)
print(f'Аниме с количесвом эпизодов {names[-1]} максимальное в датасете, и количество таких аниме {counts[-1]}')
plt.xticks(rotation=-90)
plt.bar(names,counts)

t= df.source.value_counts().sort_values()
names, counts = count(t)
print(f'Аниме с источником {names[-1]} максимальное в датасете, и количество таких аниме {counts[-1]}')
plt.xticks(rotation=-90)
plt.bar(names[-3:],counts[-3:])

t = pd.DataFrame({'index': [idx for idx,t in enumerate(themes) for t in range(len(t))],
                    'theme': [t for theme in themes for t in theme]}).theme.value_counts().sort_values()
names, counts = count(t)
print(f'Аниме с тема {names[-1]} максимальное в датасете, и количество таких аниме {counts[-1]}')
plt.xticks(rotation=-90)
plt.bar(names,counts)

date_df = loaded_df.copy()

date_df.dropna(how="any", inplace=True, subset = ['Airdate'])
t = pd.DataFrame({'airdate':[str(t).split(',')[1][1:] for t in date_df['Airdate']]}).airdate.value_counts().sort_values()
names, counts = count(t)
print(f'Аниме {names[-1]} года максимальное в датасете, и количество таких аниме {counts[-1]}')
plt.xticks(rotation=-90)
plt.bar(names,counts)


t = df.groupby('production').mean()['rating'].sort_values()
names, counts = count(t)
print(f'Аниме компаний {names[-3:]} лучше в датасете, и их средний рейтинг соотвественно {counts[-3:]}')
plt.xticks(rotation=-90)
plt.bar(names,counts)


t = df['rating'].astype(int).value_counts().sort_values()

names, counts = count(t)
print(f'Аниме c оценкой в промежутке [{names[-1]}-{int(names[-1])+1}) максимальное в датасете, и количество таких аниме {counts[-1]}')
plt.xticks(rotation=-90)
plt.bar(names,counts)


df_11 = df.copy()
df_11['rating'] = df_11['rating'].astype(int)
themes = [str(row).split(',') for row in df['theme']]
des = pd.DataFrame({'rating': [df_11['rating'][idx] for idx,t in enumerate(themes) for t in range(len(t))],
                   'theme': [t for theme in themes for t in theme]}).groupby('theme')['rating'].describe().sort_values('min', ascending=False)
des[des['count'] > 20]



v = df['voters']
r = df['rating']
plt.plot(v,r,'-')
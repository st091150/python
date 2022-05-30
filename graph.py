import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
normal_sample  = np.random.normal(loc = 0.0, scale = 1.0, size=10000)
random_sample =  np.random.random(size=10000)
gamma_sample = np.random.gamma(2,size=10000)

df = pd.DataFrame({'normal': normal_sample,
                   'random': random_sample,
                   'gamma': gamma_sample})


df.head()


plt.figure()
_ = plt.boxplot(df['normal'], whis ='range') #[0,100]

_ = plt.boxplot([df['normal'], df['random'], df['gamma']], whis ='range')


dff = pd.DataFrame(data=df, columns=["normal", "random", "gamma"] )
sns.boxplot(x =None, y= None, data=dff);


plt.figure()
plt.boxplot([df['normal'],df['random'], df['gamma']], whis = [0,100])
ax2=mpl_il.inset_axes(plt.gca(), width = '60%', height = '40%', loc=2)
ax2.hist(df['gamma'], bins =100)
ax2.margins(x=0.5)
ax2.yaxis.tick_right()
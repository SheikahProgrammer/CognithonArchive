import pandas as pd
import random
import numpy as np

# good_pressure	good_temp	good_vibe	good_flow	good_level	good_rpm

df = pd.read_csv('raw.csv')
# list form of all the columns

c1 = df['good_pressure'].tolist()
c2 = df['good_temp'].tolist()
c3 = df['good_vibe'].tolist()
c4 = df['good_flow'].tolist()
c5 = df['good_level'].tolist()
c6 = df['good_rpm'].tolist()

c1=np.random.choice(c1, 50000)
c2=np.random.choice(c2, 50000)
c3=np.random.choice(c3, 50000)
c4=np.random.choice(c4, 50000)
c5=np.random.choice(c5, 50000)
c6=np.random.choice(c6, 50000)

#save

df = pd.DataFrame({'good_pressure': c1, 'good_temp': c2, 'good_vibe': c3, 'good_flow': c4, 'good_level': c5, 'good_rpm': c6})
df.to_csv('good.csv', index=False)

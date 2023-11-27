import pandas as pd
import numpy as np
# read the data
df = pd.read_csv('raw.csv')
# List of all the columns
CList = df.columns.tolist()
print(CList)
# Function to randamly pic rows from a list of columns
def randam_rows(list, n):
    lll = []
    for i in range(n):
        boy = []
        for lol in list:
            boy.append(np.random.choice(lol))
        lll.append(boy)
    return lll
# A class that pairs two columns

class Pair:
    def __init__(self, col1, col2):
        self.good = col1.tolist()
        self.bad = col2.tolist()

class SixP:
    def __init__(self, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12):
        self.p1 = Pair(col1, col2)
        self.p2 = Pair(col3, col4)
        self.p3 = Pair(col5, col6)
        self.p4 = Pair(col7, col8)
        self.p5 = Pair(col9, col10)
        self.p6 = Pair(col11, col12)
    
    def signature(self,S):
        # S will be str of 0s and 1s
        # 0 means bad and 1 means good
        # S = '010101' for example

        # The following code will return a list of 6 lists

        lis = [] 
        for i in range(6):
            lis.append(eval(f"self.p{i+1}.{'bad' if S[i]=='0' else 'good'}"))
        return lis


# Create pairs of columns

pairs = []

pressure = Pair(df[CList[0]], df[CList[1]])
temp = Pair(df[CList[2]], df[CList[3]])
vibe = Pair(df[CList[4]], df[CList[5]])
oil_flow = Pair(df[CList[6]], df[CList[7]])
oil_level = Pair(df[CList[8]], df[CList[9]])
RPM = Pair(df[CList[10]], df[CList[11]])

# Create 6P

SSS = SixP(*[df[CList[i]] for i in range(12)])  


pp = []
for sign_No in range(63):
    sign = bin(sign_No)[2:]
    sign = '0'*(6-len(sign)) + sign
    print(sign)
    pp.extend(np.transpose(SSS.signature(sign)))

ppp = pd.DataFrame(pp)
print(ppp.shape)
print(ppp.sample(10))
ppp = ppp.sample(50000)
ppp.to_csv('bad.csv', index=False)
# print(pd.DataFrame(np.transpose(SSS.signature("010111"))).head(10))
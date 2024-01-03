#!/usr/bin/python3
#
# t1.py
#
# Generate Tables

import numpy as np
import pandas as pd

#y = np.arange(1, 6)
#x = np.arange(1, 6)
#df = pd.DataFrame(np.random.randint(2, size=(5,5)), columns=x, index=y, dtype=int)
#df.to_csv("table1.csv")

df = pd.DataFrame(
        np.random.randint(2, size=(5,5)),
        columns=np.arange(1,6),
        index=np.arange(1,6),
        dtype=int)
df.to_csv("table1.csv")

y2 = np.arange(1,11)
x2 = np.arange(1,11)
df2 = pd.DataFrame(np.random.randint(2, size=(10,10)), columns=x2, index=y2, dtype=int)
df2.to_csv("table2.csv")

y3 = np.arange(1,2)
x3 = np.arange(1,12)
df3 = pd.DataFrame(np.random.randint(2, size=(1,11)), columns=x3, index=y3, dtype=int)
df3.to_csv("table3.csv")

y4 = np.arange(1,12)
x4 = np.arange(1,2)
df4 = pd.DataFrame(np.random.randint(2, size=(11,1)), columns=x4, index=y4, dtype=int)
df4.to_csv("table4.csv")

y5 = np.arange(1,7)
x5 = np.arange(1,22)
df5 = pd.DataFrame(np.random.randint(2, size=(6,21)), columns=x5, index=y5, dtype=int)
df5.to_csv("table5.csv")

y6 = np.arange(1,11)
x6 = np.arange(1,11)
df6 = pd.DataFrame(np.zeros((10,10)), columns=x6, index=y6, dtype=int)
df6[5][3] = 1
df6.to_csv("table6.csv")

y7 = np.arange(1,12)
x7 = np.arange(1,12)
df7 = pd.DataFrame(np.zeros((11,11)), columns=x7, index=y7, dtype=int)
df7[6][6] = 1
df7.to_csv("example1.csv")

y8 = np.arange(1,12)
x8 = np.arange(1,12)
df8 = pd.DataFrame(np.zeros((11,11)), columns=x8, index=y8, dtype=int)
df8[2][6] = 1
df8.to_csv("example2.csv")

y9 = np.arange(1,12)
x9 = np.arange(1,12)
df9 = pd.DataFrame(np.zeros((11,11)), columns=x9, index=y9, dtype=int)
df9[4][8] = 1
df9[8][4] = 1
df9.to_csv("example3.csv")

y10 = np.arange(1,12)
x10 = np.arange(1,12)
df10 = pd.DataFrame(np.zeros((11,11)), columns=x10, index=y10, dtype=int)
df10[4][8] = 1
df10[6][7] = 1
df10.to_csv("example4.csv")



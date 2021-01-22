from itertools import combinations
import pandas as pd

path=""
df=pd.read_excel(path)


l=df["data"].tolist()
sum_searched=1000

for var in combinations(l, 10):
    if sum(var)==sum_searched:
        print(var)
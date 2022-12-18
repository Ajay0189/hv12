import pandas as pd
n=list(map(int,input().split()))
n_ser=pd.Series(n)
print(n_ser*n_ser)
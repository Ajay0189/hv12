import pandas as pd
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_series=pd.Series(a)
b_series=pd.Series(b)
print(a_series,b_series)
opr=input("please choose the operation:")
if opr=='*':
    print(a_series*b_series)
elif opr=='+':
    print(a_series+b_series)
elif opr=='-':
    print(a_series/b_series)
elif opr=='*':
    print(a_series/b_series)
else:
    print('choose the correct operator')
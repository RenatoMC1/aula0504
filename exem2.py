import pandas as pd

df = pd.DataFrame({
    'Col1': [1,2,3],
    'Col2': [4,5,6]
})

sum_col1 = df['Col1'].sum()
sum_col2 = df['Col2'].sum()

print("soma da coluna 1: ", sum_col1)
print("soma da coluna 2: ", sum_col2)
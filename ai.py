import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'./venv/heights.csv')
Q1 = round(df.height.quantile(0.25))
Q2 = round(df.height.quantile(0.5))
Q3 = round(df.height.quantile(0.75))
IQR = Q3-Q1
lower_bound = Q1-(1.5*IQR)
upper_bound = Q3+(1.5*IQR)
df[(df.height > lower_bound) | (df.height < upper_bound )]
df_without_outliners = df[(df.height > lower_bound) & (df.height < upper_bound )]
print(df_without_outliners)

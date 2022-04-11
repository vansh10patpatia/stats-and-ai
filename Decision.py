import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r'./CSV/salaries.csv');
print(df.head())
inputs = df.drop('salary_more_then_100k',axis='columns')
# target = df('salary_more_then_100k')

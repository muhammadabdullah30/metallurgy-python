import pandas as pd

#loading csv file

df = pd.read_csv('process_data.csv')

#what i have 

print('--- Dataset Overview ---')
print('Shape:', df.shape)
print('\nColumn Names:', df.columns.tolist())
print('\nData Types:')
print(df.dtypes)
print('\nFirst 5 rows')
print(df.head())
print('\nBasic Statistics')
print(df.describe())

print('\n--- Missing Values ---')
print(df.isnull().sum())

print('\n--- Suspicious Values ---')
df['recovery_rate'] = (df['output_mass']/df['input_mass'])*100
df['recovery_rate'] = df['recovery_rate'].round(1)

print(df[['heat_number', 'input_mass', 'output_mass', 'recovery_rate']])

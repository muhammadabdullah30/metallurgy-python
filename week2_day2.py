import pandas as pd

#loading data
df = pd.read_csv('process_data.csv')

#calculating recovery rate
df['recovery_rate'] = (df['output_mass']/df['input_mass'])*100
df['recovery_rate'] = df['recovery_rate'].round(1)

print('Rows before cleaning:', len(df))

#step 1 - Remove rows with missing input or output mass 
df = df.dropna(subset=['input_mass', 'output_mass'])
print('Rows after removing missing values:', len(df))

#step2 - remove physically impossible recovery rates
df = df[df['recovery_rate'] >= 50]
df = df[df['recovery_rate'] <= 100]
print('Rows after removing impossible values:', len(df))

#step 3 - flagginf low recovery heats for investigation
df['flag'] = 'Normal'
df.loc[df['recovery_rate'] < 80, 'flag'] = 'Investigate'

print('\n--- Clean Dataset ---')
print(df[['heat_number', 'scrap_grade', 'recovery_rate', 'flag']])

print('\n---Summary by Scrap Grade ---')
print(df.groupby('scrap_grade')['recovery_rate'].mean().round(1))

#save cleaned data to a new file
df.to_csv('process_data_clean.csv', index=False)
print('\nClean data saved to process_data_clean.csv')
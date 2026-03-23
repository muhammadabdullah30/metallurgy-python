import pandas as pd
import numpy as np

np.random.seed(42)
n = 100

#Generating input variables
heat_numbers = range(4501, 4501 + n)
scrap_grades = np.random.choice(['HMS1', 'HMS2', 'WEEE'], n, p=[0.4, 0.3, 0.3])
temperatures = np.random.randint(1420, 1490, n)
input_masses = np.random.randint(900, 1300, n)
fluxes = np.random.randint(35, 75, n)
operators = np.random.choice(['Ahmed', 'Tariq', 'Samir'], n)

#Generating recovery rates using metallurgical logic
recovery_rates = []
for i in range(n):
    if scrap_grades[i] == 'HMS1':
        base = 91
    elif scrap_grades[i] == 'HMS2':
        base = 89
    else:
        base = 80

    temp_effect = (temperatures[i] - 1450) * 0.05
    flux_effect = -abs(fluxes[i] - 45) * 0.05
    noise = np.random.normal(0, 1.5)

    recovery = base + temp_effect + flux_effect + noise
    recovery = round(min(max(recovery, 70), 98), 1)
    recovery_rates.append(recovery)

df = pd.DataFrame({
    'heat_number': heat_numbers,
    'scrap_grade': scrap_grades,
    'temperature': temperatures,
    'input_mass': input_masses,
    'flux': fluxes,
    'operator': operators,
    'recovery_rate': recovery_rates
})

print(df.head(10))
print('\nShape:', df.shape)
print('\nAverage recovery by grade:')
print(df.groupby('scrap_grade')['recovery_rate'].mean().round(1))

df.to_csv('process_data_100.csv', index=False)
print('\nDataset saved to process_data_100.csv')
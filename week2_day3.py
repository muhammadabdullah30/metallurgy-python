import pandas as pd 
import matplotlib.pyplot as plt 

#loading the clean data file
df = pd.read_csv('process_data_clean.csv')

#Chart 1: recovery rate per heat
plt.figure(figsize=(10,5))
plt.bar(df['heat_number'], df['recovery_rate'], color='steelblue')
plt.axhline(y=90, color='red', linestyle='--', label='Target 90%')
plt.xlabel('heat_number')
plt.ylabel('Recovery Rate (%)')
plt.title('Recovery Rate per Heat')
plt.legend()
plt.tight_layout ()
plt.savefig('chart1_recovery_per_heat.png')
plt.show()
print('Chart 1 saved')

#chart 2: average recovery by scrap grade
grade_avg = df.groupby('scrap_grade')['recovery_rate'].mean().round(1)

plt.figure(figsize=(7, 5))
plt.bar(grade_avg.index, grade_avg.values, color=['green', 'orange', 'red'])
plt.xlabel('Scrap Grade')
plt.ylabel('Average Recovery Rate (%)')
plt.title('Average Recovery by Scrap Grade')
plt.ylim(70, 100)
plt.tight_layout()
plt.savefig('chart2_recovery_by_grade.png')
plt.show()
print('Chart 2 saved')

#Chart 3: Temp vs Recovery rate
plt.figure(figsize=(8, 5))
plt.scatter(df['temperature'], df['recovery_rate'], 
            color='steelblue', s=80)
plt.xlabel('Temperature (°C)')
plt.ylabel('Recovery Rate (%)')
plt.title('Temperature vs Recovery Rate')
plt.tight_layout()
plt.savefig('chart3_temp_vs_recovery.png')
plt.show()
print('Chart 3 saved')
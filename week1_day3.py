# Week 1 Day 3 - Dictionaries

heat_4401 = {
    'heat_number': 4401,
    'metal_type': 'copper',
    'input_mass': 1000,
    'output_mass': 873,
    'temperature': 1450,
    'scrap_grade': 'HMS1',
    'flux_addition': 45
}

print('--- Heat Record ---')
print('Heat Number:', heat_4401['heat_number'])
print('Metal:', heat_4401['metal_type'])
print('Scrap Grade:', heat_4401['scrap_grade'])
print('Temperature:', heat_4401['temperature'])
print('Flux Addition:', heat_4401['flux_addition'], 'kg')


recovery = (heat_4401['output_mass']/heat_4401['input_mass'])*100
print(f'Recovery Rate: {round(recovery, 1)}%')


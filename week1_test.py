heats = [
    {
        'heat_number': 4501,
        'metal_type' : 'Copper',
        'input_mass' : 1000,
        'output_mass': 891,
        'temperature': 1450,
        'scrape_grade': 'HMS1',
        'flux': 40 
        },
    {
        'heat_number': 4502,
        'metal_type' : 'Copper',
        'input_mass' : 1200,
        'output_mass': 1080,
        'temperature': 1465,
        'scrape_grade': 'HMS2',
        'flux': 52 
        },
    {
        'heat_number': 4503,
        'metal_type' : 'Copper',
        'input_mass' : 950,
        'output_mass': 760,
        'temperature': 1430,
        'scrape_grade': 'WEEE',
        'flux': 38 
        },
    {
        'heat_number': 4504,
        'metal_type' : 'Copper',
        'input_mass' : 1100,
        'output_mass': 1012,
        'temperature': 1455,
        'scrape_grade': 'HMS1',
        'flux': 45
        },
    {
        'heat_number': 4505,
        'metal_type' : 'Copper',
        'input_mass' : 1080,
        'output_mass': 875,
        'temperature': 1440,
        'scrape_grade': 'WEEE',
        'flux': 60
        },

]


print('--- Daily Heat Report ---')
#loop for calculating and printing
for i in range(len(heats)):
    recovery = ((heats[i]['output_mass']/heats[i]['input_mass'])*100)
    recovery = round(recovery, 1)

    print(f'Heat Number:', heats[i]['heat_number'])
    print(f'Metal Type:', heats[i]['metal_type'])
    print(f'Scrap Grade:', heats[i]['scrape_grade'])
    print(f'Temperature:', heats[i]['temperature'],'C')
    print(f'Flux Added:', heats[i]['flux'],'kg')
    print(f'Recovery Rate: {recovery}%')

#checking status of the recovery rate
    if recovery >= 90:
        status = 'Excellent'
    elif recovery >= 80:
        status = 'Acceptable'
    else:
        status = 'Needs Review'

    print(f'Status: {status} \n')



#extra information
total_input_mass = sum(heat['input_mass'] for heat in heats)
total_output_mass = sum(heat['output_mass'] for heat in heats)

print('Total Input Mass:', total_input_mass, 'kg')
print('Total Output Mass:', total_output_mass, 'kg')   

average_recovery = sum((heat['output_mass']/heat['input_mass'])*100 for heat in heats) / len(heats)
average_recovery = round(average_recovery,1)
print(f'Average Recovery Rate: {average_recovery}%')
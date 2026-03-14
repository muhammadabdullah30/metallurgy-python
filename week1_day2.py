

heat_numbers = [4401, 4402, 4403, 4404, 4405]
input_masses = [1000, 1020, 950, 1100, 1050]
output_masses = [873, 1020, 800, 990, 924]

print('--- Daily heat recovery Report ---')

for i in range(len(heat_numbers)):
    recovery = (output_masses[i] / input_masses[i])*100
    recovery = round(recovery, 1)
    print(f"Heat {heat_numbers[i]}: Recovery = {recovery}%")

print('\n --- Status Report ---')

for i in range(len(heat_numbers)):
    recovery = (output_masses[i] / input_masses[i])*100
    recovery = round(recovery, 1)

    if recovery >= 90:
        status = 'Excellent'
    elif recovery >= 80:
        status = 'Acceptable'
    else:
        recovery = 'Needs Review'
    
    print(f'Heat {heat_numbers[i]}: Recovery = {recovery}% - {status}')
    
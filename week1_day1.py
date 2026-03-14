furnance_temperature = 1450.5
metal_type = 'copper'
recovery_rate = 87
process_active = True

print('--- Process Report ---')
print('Metal:', metal_type)
print('Furnace Temperature (C):', furnance_temperature)
print('Recovery Rate (%):', recovery_rate)
print('Process Active:', process_active)

scrap_input_mass = 1000
metal_output_mass = 873

calculated_recovery = (metal_output_mass/scrap_input_mass)*100
print('Calculated Recovery (%):', calculated_recovery)

loss = scrap_input_mass - metal_output_mass
print('Material Lost(kg): ', loss)

if calculated_recovery >= 90:
    print('Status: Excellent Recovery')

elif calculated_recovery >= 80:
    print('Status: Acceptable Recovery')

else:
    print('Status: Needs Process Review')
    
description = "This program converts mass concentration to molar concentration."
allowed_units = """The following units for mass concentration are allowed: 
g/L, mg/L, ug/L, ng/L, g/ml, mg/ml, ug/ml, ng/ml, g/ul, mg/ul, ug/ul, ng/ul
"""


print(description)
print(allowed_units)


coefficients = {'g/L': 1,
                'mg/L': 0.001,
                'ug/L': 0.000001,
                'ng/L': 0.000000001,
                'g/ml': 1000,
                'mg/ml': 1,
                'ug/ml': 0.001,
                'ng/ml': 0.000001,
                'g/ul': 1000000,
                'mg/ul': 1000,
                'ug/ul': 1,
                'ng/ul': 0.001}

# asking users to enter their mass concentration units and checking if the correct unit has been chosen
unit_MassConc_initial = input("Enter units for mass concentration, for example, g/L: ")

wrong_units_message = "Wrong units have been chosen."

while unit_MassConc_initial not in coefficients:
    print(wrong_units_message)
    print(allowed_units)
    unit_MassConc_initial = input("Enter units for mass concentration, for example, g/L: ")



# asking users to enter mass concentration and checking if a number was entered
wrong_value_message = "You need to enter a number (for example, 5, 130.6, 7.8...)."
mass_conc_initial = input("Enter the number corresponding to your mass concentration: ")

mass_conc_initial_float = None
while mass_conc_initial_float is None:
    try:
        mass_conc_initial_float = float(mass_conc_initial)

    except ValueError:
        print(wrong_value_message)
        mass_conc_initial = input("Enter the number corresponding to your mass concentration: ")



# asking users to enter molar mass in g/mol and checking if a number was entered
molar_mass = input("Enter the number corresponding to the molar mass in g/mol for your compound:")

molar_mass_float = None
while molar_mass_float is None:
    try:
        molar_mass_float = float(molar_mass)

    except ValueError:
        print(wrong_value_message)
        molar_mass = input("Enter the number corresponding to the molar mass in g/mol for your compound:")

# Converting the user's mass concentration units into g/L using coefficients and writing the resulting value into mass_conc_new:
mass_conc_new = mass_conc_initial_float * coefficients[unit_MassConc_initial]
molar_conc = mass_conc_new / molar_mass_float

result = 'The molar concentration is ' + str(molar_conc) + ' mol/L'
print(result)

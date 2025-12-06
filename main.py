import math
import sys

print("\nPlease select a moderator:")
print("1. Light Water (H2O) [High scattering, high uncertainty]")
print("2. Heavy Water (D2O) [Low absorption, medium uncertainty]")
print("3. Graphite (C)      [Stable slowing down, low uncertainty]")

choice = input("Your Selection (1/2/3): ")
moderators = {
    '1': {'name': 'Light Water (H2O)', 'xi': 0.920, 'A': 1},
    '2': {'name': 'Heavy Water (D2O)', 'xi': 0.509, 'A': 2},
    '3': {'name': 'Graphite (C)',    'xi': 0.158, 'A': 12}
}

if choice not in moderators:
    print("Error: Invalid Selection!")
    sys.exit()
selected_mod = moderators[choice]

try:
    e_initial_mev = float(input("\nEnter initial neutron energy (MeV) [e.g., 2]: "))
except ValueError:
    print("Error: Please enter a valid number.")
    sys.exit() 

e_initial_ev = e_initial_mev * 1_000_000 # MeV -> eV
e_thermal_ev = 0.025 # Target (eV)

if e_initial_ev <= e_thermal_ev:
    print("Error: Neutron energy cannot be lower than or equal to thermal energy!")
    sys.exit()

lethargy = math.log(e_initial_ev / e_thermal_ev)
avg_collisions = lethargy / selected_mod['xi']

variance = (2 / (3 * selected_mod['A'])) * avg_collisions
std_dev = math.sqrt(variance)

lower_limit = math.floor(avg_collisions - std_dev)
upper_limit = math.ceil(avg_collisions + std_dev)

print("\n" + "=" * 40)
print(f"MODERATOR: {selected_mod['name']}")
print(f"Energy Change: {e_initial_mev} MeV -> 0.025 eV")
print("-" * 40)
print(f"AVG. NUMBER OF COLLISIONS : {round(avg_collisions, 1)}")
print(f"STANDARD DEVIATION (Error): +/- {round(std_dev, 2)} collisions")
print("-" * 40)
print(f"ANALYSIS:")
print(f"Most neutrons will reach thermal energy levels")
print(f"between {lower_limit} and {upper_limit} collisions.")
print("=" * 40)

    

        
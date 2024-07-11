"""
Version: 1.0.0
Author: Minemetero
"""
import re

# Dictionary of elements with atomic number, atomic mass, and standard atomic weight
elements = {
    'H': {'atomic_number': 1, 'atomic_mass': 1.008},
    'He': {'atomic_number': 2, 'atomic_mass': 4.0026},
    'Li': {'atomic_number': 3, 'atomic_mass': 6.94},
    'Be': {'atomic_number': 4, 'atomic_mass': 9.0122},
    'B': {'atomic_number': 5, 'atomic_mass': 10.81},
    'C': {'atomic_number': 6, 'atomic_mass': 12.011},
    'N': {'atomic_number': 7, 'atomic_mass': 14.007},
    'O': {'atomic_number': 8, 'atomic_mass': 15.999},
    'F': {'atomic_number': 9, 'atomic_mass': 18.998},
    'Ne': {'atomic_number': 10, 'atomic_mass': 20.180},
    'Na': {'atomic_number': 11, 'atomic_mass': 22.990},
    'Mg': {'atomic_number': 12, 'atomic_mass': 24.305},
    'Al': {'atomic_number': 13, 'atomic_mass': 26.982},
    'Si': {'atomic_number': 14, 'atomic_mass': 28.085},
    'P': {'atomic_number': 15, 'atomic_mass': 30.974},
    'S': {'atomic_number': 16, 'atomic_mass': 32.06},
    'Cl': {'atomic_number': 17, 'atomic_mass': 35.45},
    'K': {'atomic_number': 19, 'atomic_mass': 39.098},
    'Ar': {'atomic_number': 18, 'atomic_mass': 39.948},
    'Ca': {'atomic_number': 20, 'atomic_mass': 40.078},
    'Sc': {'atomic_number': 21, 'atomic_mass': 44.956},
    'Ti': {'atomic_number': 22, 'atomic_mass': 47.867},
    'V': {'atomic_number': 23, 'atomic_mass': 50.942},
    'Cr': {'atomic_number': 24, 'atomic_mass': 51.996},
    'Mn': {'atomic_number': 25, 'atomic_mass': 54.938},
    'Fe': {'atomic_number': 26, 'atomic_mass': 55.845},
    'Ni': {'atomic_number': 28, 'atomic_mass': 58.693},
    'Co': {'atomic_number': 27, 'atomic_mass': 58.933},
    'Cu': {'atomic_number': 29, 'atomic_mass': 63.546},
    'Zn': {'atomic_number': 30, 'atomic_mass': 65.38},
    'Ga': {'atomic_number': 31, 'atomic_mass': 69.723},
    'Ge': {'atomic_number': 32, 'atomic_mass': 72.63},
    'As': {'atomic_number': 33, 'atomic_mass': 74.922},
    'Se': {'atomic_number': 34, 'atomic_mass': 78.971},
    'Br': {'atomic_number': 35, 'atomic_mass': 79.904},
    'Kr': {'atomic_number': 36, 'atomic_mass': 83.798},
    'Rb': {'atomic_number': 37, 'atomic_mass': 85.468},
    'Sr': {'atomic_number': 38, 'atomic_mass': 87.62},
    'Y': {'atomic_number': 39, 'atomic_mass': 88.906},
    'Zr': {'atomic_number': 40, 'atomic_mass': 91.224},
    'Nb': {'atomic_number': 41, 'atomic_mass': 92.906},
    'Mo': {'atomic_number': 42, 'atomic_mass': 95.95},
    'Tc': {'atomic_number': 43, 'atomic_mass': 98.0},
    'Ru': {'atomic_number': 44, 'atomic_mass': 101.07},
    'Rh': {'atomic_number': 45, 'atomic_mass': 102.91},
    'Pd': {'atomic_number': 46, 'atomic_mass': 106.42},
    'Ag': {'atomic_number': 47, 'atomic_mass': 107.87},
    'Cd': {'atomic_number': 48, 'atomic_mass': 112.41},
    'In': {'atomic_number': 49, 'atomic_mass': 114.82},
    'Sn': {'atomic_number': 50, 'atomic_mass': 118.71},
    'Sb': {'atomic_number': 51, 'atomic_mass': 121.76},
    'I': {'atomic_number': 53, 'atomic_mass': 126.90},
    'Te': {'atomic_number': 52, 'atomic_mass': 127.60},
    'Xe': {'atomic_number': 54, 'atomic_mass': 131.29},
    'Cs': {'atomic_number': 55, 'atomic_mass': 132.91},
    'Ba': {'atomic_number': 56, 'atomic_mass': 137.33},
    'La': {'atomic_number': 57, 'atomic_mass': 138.91},
    'Ce': {'atomic_number': 58, 'atomic_mass': 140.12},
    'Pr': {'atomic_number': 59, 'atomic_mass': 140.91},
    'Nd': {'atomic_number': 60, 'atomic_mass': 144.24},
    'Pm': {'atomic_number': 61, 'atomic_mass': 145.0},
    'Sm': {'atomic_number': 62, 'atomic_mass': 150.36},
    'Eu': {'atomic_number': 63, 'atomic_mass': 151.96},
    'Gd': {'atomic_number': 64, 'atomic_mass': 157.25},
    'Tb': {'atomic_number': 65, 'atomic_mass': 158.93},
    'Dy': {'atomic_number': 66, 'atomic_mass': 162.50},
    'Ho': {'atomic_number': 67, 'atomic_mass': 164.93},
    'Er': {'atomic_number': 68, 'atomic_mass': 167.26},
    'Tm': {'atomic_number': 69, 'atomic_mass': 168.93},
    'Yb': {'atomic_number': 70, 'atomic_mass': 173.05},
    'Lu': {'atomic_number': 71, 'atomic_mass': 174.97},
    'Hf': {'atomic_number': 72, 'atomic_mass': 178.49},
    'Ta': {'atomic_number': 73, 'atomic_mass': 180.95},
    'W': {'atomic_number': 74, 'atomic_mass': 183.84},
    'Re': {'atomic_number': 75, 'atomic_mass': 186.21},
    'Os': {'atomic_number': 76, 'atomic_mass': 190.23},
    'Ir': {'atomic_number': 77, 'atomic_mass': 192.22},
    'Pt': {'atomic_number': 78, 'atomic_mass': 195.08},
    'Au': {'atomic_number': 79, 'atomic_mass': 196.97},
    'Hg': {'atomic_number': 80, 'atomic_mass': 200.59},
    'Tl': {'atomic_number': 81, 'atomic_mass': 204.38},
    'Pb': {'atomic_number': 82, 'atomic_mass': 207.2},
    'Bi': {'atomic_number': 83, 'atomic_mass': 208.98},
    'Th': {'atomic_number': 90, 'atomic_mass': 232.04},
    'Pa': {'atomic_number': 91, 'atomic_mass': 231.04},
    'U': {'atomic_number': 92, 'atomic_mass': 238.03}
}

def parse_formula(formula):
    # Regex to match elements and their quantities
    pattern = r'([A-Z][a-z]?)(\d*)'
    parsed_formula = re.findall(pattern, formula)
    
    elements_dict = {}
    for element, quantity in parsed_formula:
        if quantity == '':
            quantity = 1
        else:
            quantity = int(quantity)
        if element in elements_dict:
            elements_dict[element] += quantity
        else:
            elements_dict[element] = quantity
    return elements_dict

def calculate_molar_mass(formula):
    elements_dict = parse_formula(formula)
    molar_mass = 0
    for element, quantity in elements_dict.items():
        molar_mass += elements[element]['atomic_mass'] * quantity
    return molar_mass

def calculate_subatomic_particles(formula):
    elements_dict = parse_formula(formula)
    protons = neutrons = electrons = 0
    for element, quantity in elements_dict.items():
        atomic_number = elements[element]['atomic_number']
        atomic_mass = elements[element]['atomic_mass']
        protons += atomic_number * quantity
        neutrons += (atomic_mass - atomic_number) * quantity
        electrons += atomic_number * quantity
    return protons, neutrons, electrons

def parse_reaction(reaction):
    reactants, products = reaction.split('->')
    reactants = reactants.split('+')
    products = products.split('+')
    return reactants, products

def parse_compound(compound):
    # Regex to extract stoichiometric coefficient and compound
    pattern = r'(\d*)\s*([A-Za-z0-9]+)'
    match = re.match(pattern, compound.strip())
    if match:
        coefficient = match.group(1)
        if coefficient == '':
            coefficient = 1
        else:
            coefficient = int(coefficient)
        formula = match.group(2)
        return coefficient, formula
    else:
        raise ValueError(f"Invalid compound format: {compound}")

def main():
    reaction = input("Enter a chemical reaction (e.g., 2 H2 + O2 -> 2 H2O): ")
    try:
        reactants, products = parse_reaction(reaction)
        
        print("Reactants:")
        for reactant in reactants:
            coefficient, formula = parse_compound(reactant)
            molar_mass = calculate_molar_mass(formula)
            total_mass = coefficient * molar_mass
            protons, neutrons, electrons = calculate_subatomic_particles(formula)
            total_protons = coefficient * protons
            total_neutrons = coefficient * neutrons
            total_electrons = coefficient * electrons
            print(f"{coefficient} {formula}:")
            print(f"  Molar Mass: {molar_mass:.2f} g/mol, Total: {total_mass:.2f} g/mol")
            print(f"  Protons: {total_protons}, Neutrons: {total_neutrons}, Electrons: {total_electrons}")
        
        print("Products:")
        for product in products:
            coefficient, formula = parse_compound(product)
            molar_mass = calculate_molar_mass(formula)
            total_mass = coefficient * molar_mass
            protons, neutrons, electrons = calculate_subatomic_particles(formula)
            total_protons = coefficient * protons
            total_neutrons = coefficient * neutrons
            total_electrons = coefficient * electrons
            print(f"{coefficient} {formula}:")
            print(f"  Molar Mass: {molar_mass:.2f} g/mol, Total: {total_mass:.2f} g/mol")
            print(f"  Protons: {total_protons}, Neutrons: {total_neutrons}, Electrons: {total_electrons}")
        
    except KeyError as e:
        print(f"Error: Element {e} not found in elements dictionary")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

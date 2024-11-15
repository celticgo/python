# Function to get weight in lbs and convert to kilograms
def get_weight_kg():
    weight_lbs = float(input("Enter your weight in pounds: "))
    weight_kg = weight_lbs * 0.453592
    return weight_kg

# Function to calculate protein needs for muscle building
def calculate_protein_needs(weight_kg):
    min_protein = weight_kg * 1.2  # minimum grams per kg
    max_protein = weight_kg * 1.7  # maximum grams per kg
    return min_protein, max_protein

# Main program
def main():
    weight_kg = get_weight_kg()
    min_protein, max_protein = calculate_protein_needs(weight_kg)
    print(f"Your weight in kilograms is: {weight_kg:.2f} kg")
    print(f"To build muscle, you need between {min_protein:.2f}g and {max_protein:.2f}g of protein per day.")

# Run the main function
if __name__ == "__main__":
    main()





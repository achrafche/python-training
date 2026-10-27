def main():
    weight = grams_to_kg(input("Weight in grams? "))
    rate = fils_to_bhd(input("Rate per kg in fils? "))
    cost = weight * rate
    print(f"Cost: {cost:.3f} BHD")


def grams_to_kg(g):
    """Return a weight typed in grams, converted to kilograms."""
    return float(g) / 1000


def fils_to_bhd(f):
    """Return an amount typed in fils, converted to Bahraini dinars."""
    return float(f) / 1000


main()
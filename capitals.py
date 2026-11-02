def main():
    countryc = {"bahrain": "Manama", "saudi arabia": "Riyadh", "uae": "Abu Dhabi", "kuwait": "Kuwait City",
                "oman": "Muscat", "qatar": "Doha"}
    capitals = input("Country: ").strip().lower()
    if capitals in countryc:
        print(f"Capital: {countryc[capitals]}")
    else:
        print("Unknown country")

main()
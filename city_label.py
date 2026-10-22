def main():
    entry = input("enter a city name: ")
    name = make_label(entry)
    print(name)


def make_label(entry):
    """Return the city cleaned and title-cased, preceded by 📦."""
    return f"📦 {entry.strip().title()}"


main()
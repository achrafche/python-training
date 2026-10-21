def main():
    enter_text = input("enter text: this format (city_year_reference): ")
    replacement = format_code(enter_text)
    print(replacement)


def format_code(text):
    """Return the shipment code with dashes, in uppercase."""
    return text.replace("_", "-").upper()


main()
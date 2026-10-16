"""Read one invoice line and print its total price."""


def main():
    entry = input("enter the invoice lien (item, quantity, unit_price) ? ")
    entry = entry.split(",")
    item = entry[0].strip().title()
    quantity = int(entry[1].strip())
    unit_price = float(entry[2].strip())
    total = line_total(quantity, unit_price)
    print(f"invoice line: {quantity} x {item}: {total} BHD")


def line_total(quantity, unit_price):
    """Return the total price for a quantity at a unit price."""
    total = quantity * unit_price
    return total


main()
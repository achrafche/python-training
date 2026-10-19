"""Read one invoice line and print its total price."""


def main():
    entry = input("Invoice line (item,quantity,unit_price): ")
    item, quantity, unit_price = parse_invoice_line(entry)
    total = line_total(quantity, unit_price)
    print(f"{quantity} x {item}: {total} BHD")


def parse_invoice_line(entry):
    """Return item, quantity and unit_price from an invoice line."""
    parts = entry.split(",")
    item = parts[0].strip().title()
    quantity = int(parts[1].strip())
    unit_price = float(parts[2].strip())
    return item, quantity, unit_price


def line_total(quantity, unit_price):
    """Return the total price for a quantity at a unit price."""
    total = quantity * unit_price
    return total


main()
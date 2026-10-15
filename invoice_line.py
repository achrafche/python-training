def main():
    entry = input("Invoice line (item,quantity,unit_price): ")
    parts = entry.split(",")
    item = parts[0].strip().title()
    quantity = int(parts[1].strip())
    unit_price = float(parts[2].strip())
    total_price = quantity * unit_price
    print(f"{quantity} x {item}: {total_price} BHD")


main()
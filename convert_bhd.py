def main():
    rate = {"usd": 0.4, "eur": 0.5, "sar": 0.1}
    entry = input("Amount: ").strip()
    amount, currency = entry.split()
    currency = currency.lower()
    if currency in rate:
        result = float(amount) * rate[currency]
        print(f"{result:.3f} BHD")

main()

def main():
    entry = {"water": 200, "bread": 350, "milk": 900}
    total = 0
    while True:
        item = input("Item: ").strip().lower()
        if item == "done":
            break
        if item in entry:
            total += entry[item]
    print(f"Total: {total} fils")

main()

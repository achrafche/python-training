while True:
    try:
        item = input("Item: ")
        print(f"Added: {item}")
    except EOFError:
        print()
        break
print("Finished")

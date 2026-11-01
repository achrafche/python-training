def main():
    entry = input("Enter text: ")
    print(swap_case(entry))


def swap_case(entry):
    """Return the text with uppercase and lowercase letters swapped."""
    result = ""
    for c in entry:
        if c.isupper():
            result += c.lower()
        elif c.islower():
            result += c.upper()
        else:
            result += c
    return result


main()
def main():
    name = input("Name: ")
    if is_ok(name):
        print("OK")
    else:
        print("Refused")


def is_ok(s):
    if len(s) < 3 or len(s) > 5:
        return False
    if s.isalpha() == False:
        return False
    return True


main()
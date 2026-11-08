def main():
    print(has_at("a@b"))
    print(has_at("abc"))


def has_at(s):
    for c in s:
        if c == "@":
            return True
    return False


main()
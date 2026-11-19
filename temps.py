"""
Temps (warm-up, 18 Nov 2026)

The program asks for a temperature.
If the user types something that is not a number, ignore it and ask again.
Keep asking until the user presses Ctrl-D.
At the end, print how many temperatures are below 0.

Test: -3, hello, 5, -0.5, 0, then Ctrl-D -> prints 2
"""


def main():
    count = 0
    while True:
        try:
            temps = float(input("enter temperature: "))
            if temps < 0:
                count += 1
        except ValueError:
            pass
        except EOFError:
            print()
            break
    print(count)


main()
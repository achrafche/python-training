"""
Parcels (exercise done together, 17 Nov 2026)

The program asks for the weight of a parcel in kg.
If the user types something that is not a number, ask again.
Keep asking until the user presses Ctrl-D.
At the end, print how many parcels weigh more than 20 kg.

Test: 12, abc, 25, 30, then Ctrl-D -> prints 2
"""


def main():
    count = 0
    while True:
        try:
            parcel_w = float(input("enter weight: "))
            if parcel_w > 20:
                count = count + 1
        except ValueError:
            pass
        except EOFError:
            print()
            break
    print(count)


main()
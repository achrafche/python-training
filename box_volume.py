def main():
    side = int(input("Cube side in cm: "))
    volume = cube_volume(side)
    print(volume)


def cube_volume(side):
    """Return the volume of a cube from the length of its side."""
    return side ** 3


main()
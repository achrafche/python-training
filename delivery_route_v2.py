def main():
    fuel = 60.0
    total_distance = 0
    deliveries = 0
    refused = 0

    while True:
        distance = int(input("Distance (km): "))

        if distance == 0:                       
            break

        if distance > 200:                      
            print("Refused: over 200 km")
            refused += 1
            continue

        needed = distance * 0.1                 
        if fuel < needed:                       
            print("Not enough fuel, back to depot")
            break

        fuel -= needed                          
        total_distance += distance
        deliveries += 1

        if fuel < 10:                           
            print("Warning: low fuel")

    print(f"Deliveries: {deliveries}")
    print(f"Distance: {total_distance} km")
    print(f"Fuel left: {fuel:.1f} L")
    print(f"Refused: {refused}")


main()
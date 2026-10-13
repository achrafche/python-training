fuel = 60
rejected_delivery = 0
accepted_delivery = 0
total_distance = 0
while True:
    distance_delivery = int(input("Enter the distance for the delivery in km ? "))
    fuel_needed = 0.1 * distance_delivery
    if distance_delivery == 0:
        print("finished")
        break
    elif distance_delivery > 200:
        rejected_delivery += 1  
        print("Delivery rejected due to distance exceeding 200 km.")
    elif fuel < fuel_needed:
        print("Not enough fuel, return to depot..")
        break
    else:
        accepted_delivery += 1
        total_distance += distance_delivery
        fuel = fuel - fuel_needed
        if fuel < 10:
            print("Warning: low fuel")
print(f"Deliveries:{accepted_delivery}")
print(f"Total distance covered: {total_distance} km.")
print(f"Remaining fuel: {fuel} liters.")
print(f"Refused: {rejected_delivery}")

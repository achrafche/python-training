"""
Delivery Route Simulator

Simulates a delivery driver's route with a limited fuel tank.
The driver starts with 60 liters and the truck uses 1 liter every 10 km.

Rules:
- Enter 0 to end the route.
- Deliveries over 200 km are refused.
- If there is not enough fuel for a delivery, the driver returns to the depot.
- A warning is shown when less than 10 liters remain after a delivery.

At the end, the program prints the number of deliveries, the total distance,
the remaining fuel and the number of refused deliveries.

Usage:
    python3 delivery_route.py
"""

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

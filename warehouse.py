shipments = [{"City": "Doha", "weight": 7},
{"City": "Dubai", "weight": 20},
{"City": "Manama", "weight": 10}, 
{"City": "Muscat", "weight": 18},]

total = 0 
heavy = 0
for shipment in shipments:
    print(f"{shipment['City']}: {shipment['weight']} kg")
    total = total + shipment["weight"]
    if shipment["weight"] > 15:
        heavy += 1 
print(f"Heavy: {heavy}")
print(f"Total: {total} kg")

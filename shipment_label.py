"""
Shipment Label Formatter

Turns a messy shipment entry typed as code,city,weight
into a clean label, for example: Shipment SHP-104 to Manama: 25 kg

Usage:
    python3 shipment_label.py
"""

received_info = input("what is the shipment information (code,destination,weight) ?")
received_info = received_info.split(",")
code = received_info[0].upper().strip()
destination = received_info[1].title().strip()
weight = received_info[2].strip()
print(f"Shipment {code} to {destination}: {weight} kg")
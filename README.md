# python-training

My Python training toward Harvard's CS50P and an AI Engineer role.

Each exercise is a small, self-contained program, written by hand (no AI code generation) and inspired by real business situations.

## Exercises

| File | Domain | Description |
| --- | --- | --- |
| `delivery_route.py` | Logistics | Simulates a delivery route: tracks fuel consumption, refuses deliveries over 200 km, warns on low fuel and stops when fuel runs out. |
| `shipment_label.py` | Logistics | Turns a messy shipment entry (code, city, weight) into a clean, formatted label. |
| `invoice_line.py` | Finance | Reads an invoice line (item, quantity, unit price), cleans it and prints the line total, using small functions that return values. |
| `shipment_code.py` | Logistics | Normalizes a shipment code typed as `bh_2026_0457` into the standard format `BH-2026-0457`, using chained string methods. |
   | `city_label.py` | Logistics | Cleans a city name typed by the user and returns it as a parcel label (`📦 Abu Dhabi`), through a function whose name and return value are imposed by the specification. |

## How to run

```bash
python3 delivery_route.py
```

## Skills practiced

- Variables, conditions (`if` / `elif` / `else`) and `while` loops
- User input and running totals
- Functions that receive values and return one or several values
- String methods (`.strip`, `.split`, `.replace`, `.upper`), slicing and number formatting
- Git and GitHub workflow
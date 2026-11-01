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
| `parcel_tag.py` | Logistics | Turns a parcel code typed by the user (`  bh-0457 `) into a clean tag (`#BH-0457`), built step by step from `main()` to the returned value. |
| `box_volume.py` | Logistics | Computes the volume of a cube-shaped box from its side (`25` → `15625` cm³), converting the input with `int()` and using the `**` operator. |
| `shipping_cost.py` | Logistics | Computes a parcel's shipping cost in Bahraini dinars from a weight in grams and a rate in fils, using two conversion functions called from `main()`. |
| `swap_case.py` | Text | Swaps uppercase and lowercase letters (`Hello` → `hELLO`) with a loop over each character and an `if` / `elif` / `else`. |

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
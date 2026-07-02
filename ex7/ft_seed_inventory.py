
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        text: str = f"{quantity} packets available"
    elif unit == "grams":
        text: str = f"{quantity} grams total"
    elif unit == "area":
        text: str = f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: {text}")
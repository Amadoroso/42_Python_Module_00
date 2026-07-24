
def ft_count_harvest_iterative() -> None:
    days_until: int = int(input("Days until harvest: "))
    for x in range(1, days_until + 1):
        print(f"Day {x}")
    print("Harvest time!")

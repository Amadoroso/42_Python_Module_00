
def ft_count_harvest_recursive() -> None:
    days_until: int = int(input("Days until harvest: "))
    ft_count_harvest_recursive_utils(days_until)
    print("Harvest time!")


def ft_count_harvest_recursive_utils(days_until) -> None:
    if days_until == 0:
        pass
    else:
        ft_count_harvest_recursive_utils(days_until - 1)
        print(f"Day {days_until}")

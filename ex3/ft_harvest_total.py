# O for é tipo um while com o iterador integrado
def ft_harvest_total():
    harvests: list = []
    for day in [1, 2, 3]:  # normalmente podia usar range()
        day_amount: int = int(input(f"Day {day} harvest: "))
        harvests.append(day_amount)
    print(f"Total harvest: {sum(harvests)}")

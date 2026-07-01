# O for é tipo um while com o iterador integrado
def ft_harvest_total():
    harvests: list = []
    for day in range(1, 4):  # neste caso range seria {1,2,3}
        day_amount: int = int(input(f"Day {day} harvest: "))
        harvests.append(day_amount)
    print(f"Total harvest: {sum(harvests)}")

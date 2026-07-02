
def ft_water_reminder():
    days_since: int = int(input("Days since last watering: "))
    if days_since > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

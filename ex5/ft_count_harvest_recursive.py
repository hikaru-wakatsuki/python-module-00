def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))

    def count(day):
        if day > harvest:
            print("Harvest time!")
            return
        else:
            print(f"Day {day}")
            count(day + 1)

    count(1)

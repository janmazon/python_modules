def ft_count_harvest_recursive():
    total_days = int(input("Days until harvest: "))

    def count(current_day):
        if current_day <= total_days:
            print("Day", current_day)
            count(current_day + 1)
        else:
            print("Harvest time!")
    count(1)

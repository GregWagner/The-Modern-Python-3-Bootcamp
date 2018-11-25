def return_day(day):
    if day > 7:
        return None
    days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 
            5: "Thursday", 6: "Friday", 7: "Saturday"}
    return days[day]

print(return_day(3))

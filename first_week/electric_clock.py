from sum import array_type_values
def get_time(number):
    if(type(number) not in array_type_values):
        return "Type error"
    count_hours = number // 60
    count_minutes = number % 60
    while(count_hours >= 24):
        count_hours -= 24
    return [count_hours, count_minutes]

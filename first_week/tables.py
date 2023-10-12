def get_tables(count_first_class, count_second_class, count_third_class):
    result = 0
    if count_first_class % 2 == 0:
        result += count_first_class // 2
    else:
        result += count_first_class // 2 + 1
    if count_second_class % 2 == 0:
        result += count_second_class // 2
    else:
        result += count_second_class // 2 + 1
    if count_third_class % 2 == 0:
        result += count_third_class // 2
    else:
        result += count_third_class // 2 + 1
    return result


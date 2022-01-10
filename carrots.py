def get_max_value(carrot_types: list, capacity: int) -> list:
    result = []
    for x in carrot_types:
        max_value = capacity // x["kg"]
        result.append(max_value)
    return result


if __name__ == "__main__":
    carrot_types = [{"kg": 5, "price": 100},
                   {"kg": 7, "price": 150},
                   {"kg": 3, "price": 70}]
    print(get_max_value(carrot_types, 36))

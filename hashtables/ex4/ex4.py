def has_negatives(a):
    numbers_dict = {}
    result = []

    for num in a:
        if numbers_dict.get(abs(num)):
            result.append(abs(num))
        else:
            numbers_dict[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

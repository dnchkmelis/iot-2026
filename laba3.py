def sum_two_smallest(positives: list):
    min1, min2, *_ = positives

    if min1 > min2:
        min1, min2 = min2, min1

    for item in positives[2:]:
        if item < min1:
            min1, min2 = item, min1
        elif item < min2:
            min2 = item

    return min1 + min2


raw_input = input("Введіть елементи масиву через пробіл: ")

A = []
for item in raw_input.split():
    A.append(float(item))

positives = [x for x in A if x > 0]
result = sum_two_smallest(positives)

print("Масив A:", A)
print("Результат:", result)



def pair_of_numbers(list1, list2):
    containing = []
    for i in list1:
        for j in list2:
            cont = i * j
            containing.append(cont)
    return containing


print(pair_of_numbers([1, 2, 4], [2, 3, 4]))

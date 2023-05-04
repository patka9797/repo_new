def pair_of_numbers(number_1,number_2):
    containing=[]
    for i in number_1:
        for j in number_2:
            cont=i*j
            containing.append(cont)
    return containing
print(pair_of_numbers([1,2,4],[2,3,4]))

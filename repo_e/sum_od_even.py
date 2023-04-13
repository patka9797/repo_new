# def sum_of_even(integer):
#     sum=0
#     for number in integer:
#         if number%2==0:
#             sum += number
#     return sum
# print(sum_of_even([1,10,4,3]))

def sum_of_even(integer):
    Even=[]
    for number in integer:
        if number%2==0:
            Even.append(number)
    return sum(Even)
        
    
print(sum_of_even([1,10,4,3]))

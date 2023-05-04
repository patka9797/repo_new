def capital(strings):
    Capital_str=[]
    for i, element in enumerate(strings):
        if  element==element.capitalize():
                Capital_str.append(element)
    return Capital_str
print(capital(['Krowa', 'swinia', 'Byk', 'Kun']))
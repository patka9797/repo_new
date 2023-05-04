colors=['black', 'brown', 'red', 'orange', 'yellow', 'green',
        'blue', 'violet', 'grey', 'white']

def color_value(color):
    return colors.index(color)

def label(colors):
    
    color_1, color_2, zero = [color_value(colors[i]) for i in range(3)]
    stufix = (10 * color_1 + color_2 ) * 10**zero

    if stufix <= 1000:
        return f'{stufix} ohms'
    
    elif stufix <= 1000000:
        return f'{stufix//1000} kiloohms'
    elif stufix <= 1000000000:
        return f'{stufix//1000000} megaohms'
    else:
        return f'{stufix//1000000000} gigaohms'   
    
    


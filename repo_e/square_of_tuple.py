def square_tuple(tuple):
    square = ()
    for number in tuple:
        square += (number**2,)
    return square


print(
    square_tuple(
        (
            1,
            3,
            4,
            6,
            7,
        )
    )
)

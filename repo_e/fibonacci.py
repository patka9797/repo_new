def fibonacci():
    numbers = int(input("How many numbers print?"))
    n1, n2 = 0, 1
    count = 0
    if numbers <= 0:
        print("Please enter a positive integer")
    elif numbers == 1:
        print(n1)
    else:
        print("Fibonacci sequence: ")
        while count < numbers:
            print(n1)
            next = n1 + n2
            n1 = n2
            n2 = next
            count += 1


print(fibonacci())

def factorial(n=3):
    i=1
    f=1
    while i < n:
        f += f * i
        i+=1
    print(f)
factorial(5)



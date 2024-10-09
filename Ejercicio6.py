def fibonacci(n):
    a, b = 0, 1
    if n ==1:
        print(a)
    else:
        print(a)
        print(b)

        for _ in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

n = int(input("Ingrese el número de términos: "))
fibonacci(n)

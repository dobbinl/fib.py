def fib(n): """set parameter, n. The following lines are the start of the sequence."""

    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(2, n): """Will loop until end of the range.The program will shift through the sequences."""
         c = a + b
         a = b
         b = c
         print(c)

fib(6)
def try_me(n):
    lisa = []
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            lisa.append("FizzBuzz")
        elif i % 3 == 0:
            lisa.append("Fizz")
        elif i % 5 == 0:
            lisa.append("Buzz")
        else:
            lisa.append(i)
    return lisa

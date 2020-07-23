def solution(M, F):
    generations = 0
    m, f = int(M), int(F)

    #could take fib approach, but edge case of 10^50 would take up too many resources
    while not (m == 1 and f == 1):
        if(m <= 0 or f <= 0):
            return "impossible"
        if(f == 1):
            return str(generations + m - 1)
        else:
            generations += int(m/f)
            m, f = f, m % f
    return str(generations)

print(solution("2", "4"))
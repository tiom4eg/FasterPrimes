primes = [2]


def find_all_primes(n):
    for numb in range(3, n + 1):
        max_div = int(numb ** 0.5)
        idx = 0
        flag = True
        while primes[idx] <= max_div:
            if numb % primes[idx] == 0:
                flag = False
                break
            idx += 1
        if flag:
            primes.append(numb)


n = int(input())
find_all_primes(n)
print(*primes)
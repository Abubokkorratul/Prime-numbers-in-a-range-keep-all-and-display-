low = int(input("Enter the lower bound (greater than 2): "))
high = int(input("Enter the upper bound (less than 500): "))
if low < 2 or high > 500 or low >= high:
    print("Error: Ensure the range is valid (2 < low < high < 500).")
else:
    primes = []
    for num in range(low, high + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print("Prime numbers in the range:", primes)

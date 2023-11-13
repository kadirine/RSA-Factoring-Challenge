import sys

def factorize(number):
    factors = []
    for i in range(2, number):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def main():
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        numbers = file.read().splitlines()
        for number in numbers:
            factor_pairs = factorize(int(number))
            for pair in factor_pairs:
                print(f"{number}={pair[0]}*{pair[1]}")

if __name__ == "__main__":
    main()

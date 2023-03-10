from matplotlib import pyplot as plt

from collections import Counter
from rich import print

from csv_parser import parse
import random

def main(argc: int, argv: list[str]) -> int:
    with open('data/rolls.csv') as f:
        csv: str = f.read()
        
    csv_lines: list[list] = parse(csv)
    head: list[str] = csv_lines.pop(0)

    data: list[dict[str, int]] = []

    mean: float = 0
    mode: int
    maximum: int = 0
    minimum: int = 0

    totals: list[int] = []

    for i in csv_lines:
        if not len(i) == 2:
            continue

        data.append({
            'big': i[0],
            'small': i[1],
            'total': (i[0] + i[1])
        })

        totals.append(i[0] + i[1])

    count = Counter(totals)

    mean = round(sum(totals) / len(totals), 2)
    mode = max(set(totals), key=totals.count)
    maximum = max(totals)
    minimum = min(totals)

    print(f'{len(data)} samples')
    print()
    print('  Big die  Small die  Total')
    for item in data:
        print(f'\t{item["big"]} \t {item["small"]} \t {item["total"]}\t')

    print()
    print(f'Mean(average): {mean}')
    print(f'Mode(most common): {mode}')
    print(f'Max: {maximum}')
    print(f'Min: {minimum}')

    random_nums: list[int] = [random.randrange(1, 7) + random.randrange(1, 7) for i in range(1000)]
    r_mean: float = round(sum(random_nums) / len(random_nums), 2)
    r_mode: int = max(set(random_nums), key=random_nums.count)
    r_max: int = max(random_nums)
    r_min: int = min(random_nums)

    print()
    print(f'Dice roll simul, ran 1000 simulations')
    print(f'Mean(average): {r_mean}')
    print(f'Mode(most common): {r_mode}')
    print(f'Max: {r_max}')
    print(f'Min: {r_min}')

    print()
    print('Count for each number')
    
    for i in range(2, 13):
        print(f'{i}: {count[i]}')

    plt.hist(totals, bins=[i for i in range(2, 13)])
    plt.show()
    plt.hist(random_nums, bins=[i for i in range(2, 13)])
    plt.show()

if __name__ == '__main__':
    import sys
    main(len(sys.argv), sys.argv)

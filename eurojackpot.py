from secrets import randbelow
from typing import List


def lotto(select: int, total: int) -> List[int]:
    available = list(range(1, total + 1))
    tip = []
    for _ in range(select):
        choice = randbelow(len(available))
        tip.append(available[choice])
        del available[choice]
    return sorted(tip)


print(f'Numbers: {lotto(5, 50)}\n'
      f'Euronumbers: {lotto(2, 10)}')

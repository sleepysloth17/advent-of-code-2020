from typing import List, Generator, Tuple
from itertools import islice
from math import prod

INPUT_FILE_NAME = "day-03-input.txt"


def get_input_list() -> Generator[str, None, None]:
    with open(INPUT_FILE_NAME) as input_file:
        for line in input_file:
            yield line.strip()


# 1 for tree, 0 for empty
def get_encountered(step: Tuple[int, int]) -> Generator[int, None, None]:
    input_list: List[str] = [i for i in get_input_list()]
    x: int
    y: int
    x, y = [0, 0]

    while y < len(input_list) - 1:
        y += step[1]
        line: str = input_list[y]
        x = (x + step[0]) % len(line)
        yield 1 if line[x] == "#" else 0


def multiply_trees(step_list: List[Tuple[int, int]]) -> int:
    return prod(sum(e for e in get_encountered(i)) for i in step_list)


if __name__ == "__main__":
    print("result 01: ", multiply_trees([(3, 1)]))
    print(
        "result 02: ", multiply_trees([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]),
    )

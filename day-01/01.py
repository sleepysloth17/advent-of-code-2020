from typing import List, Optional
from itertools import combinations
from functools import reduce

INPUT_FILE_NAME = "day-01-input.txt"
REQUIRED_SUM = 2020


def get_input_list() -> List[int]:
    with open(INPUT_FILE_NAME) as input_file:
        return_list: List[int] = [int(l) for l in input_file.readlines()]
        return_list.sort()
        return return_list


def search_sum_of_n(input: List[int], n: int) -> Optional[int]:
    for comb in combinations(input, n):
        if sum(comb) == REQUIRED_SUM:
            return reduce(lambda x, y: x * y, comb)

    return None


def main() -> None:
    input_list: List[int] = get_input_list()
    result_01: Optional[int] = search_sum_of_n(input_list, 2)
    result_02: Optional[int] = search_sum_of_n(input_list, 3)

    print("result 01: ", result_01)
    print("result 02: ", result_02)


if __name__ == "__main__":
    main()

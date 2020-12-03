from typing import List, Generator, Tuple, Callable

RuleRow = Tuple[Tuple[int, int], str, str]

INPUT_FILE_NAME: str = "day-02-input.txt"


def get_valid_input_list(
    condition: Callable[[RuleRow], bool]
) -> Generator[RuleRow, None, None]:
    with open(INPUT_FILE_NAME) as input_file:
        for line in input_file:
            split: List[str] = line.strip().split()
            char_range: Tuple[int, ...] = tuple(int(i) for i in split[0].split("-"))
            row: RuleRow = (
                (char_range[0], char_range[-1]),
                split[1][0],
                split[2],
            )
            if condition(row):
                yield row


def count_valid_with_condition(condition: Callable[[RuleRow], bool]) -> int:
    return len(list(get_valid_input_list(condition)))


def condition_01(entry: RuleRow) -> bool:
    return entry[0][0] <= entry[2].count(entry[1]) <= entry[0][-1]


def condition_02(entry: RuleRow) -> bool:
    return (entry[2][entry[0][0] - 1] == entry[1]) ^ (
        entry[2][entry[0][1] - 1] == entry[1]
    )


if __name__ == "__main__":
    print(
        "result 01: ", count_valid_with_condition(condition_01),
    )
    print(
        "result 02: ", count_valid_with_condition(condition_02),
    )

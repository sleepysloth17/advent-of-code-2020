from typing import Generator, Set, Callable, List
from functools import reduce

INPUT_FILE_NAME: str = "day-06-input.txt"


def get_input_sets(
    set_operation: Callable[[Set[str], Set[str]], Set[str]]
) -> Generator[Set[str], None, None]:
    with open(INPUT_FILE_NAME) as input_file:
        group: List[Set[str]] = []
        for line in input_file:
            new_entries: Set[str] = set(line.strip())
            if not len(new_entries):
                yield reduce(set_operation, group)
                group.clear()
            else:
                group.append(new_entries)
        yield reduce(set_operation, group)


def get_any_yes() -> int:
    return sum(len(i) for i in get_input_sets(lambda a, b: a.union(b)))


def get_all_yes() -> int:
    return sum(len(i) for i in get_input_sets(lambda a, b: a.intersection(b)))


if __name__ == "__main__":
    print("result 01: ", get_any_yes())
    print("result 02: ", get_all_yes())

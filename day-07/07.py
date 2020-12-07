from typing import Generator, Set, Callable, List, Dict, Tuple, Pattern
from re import compile, findall
import time

INPUT_FILE_NAME: str = "day-07-input.txt"

EXAMPLE_FILE_NAME: str = "day-07-example.txt"

CONTAINED_BAGS_PATTERN: Pattern = compile("(\\d+? .+?)+ bag")

CONTAINING_BAG_PATTERN: Pattern = compile("(.*?) bags contain ")

SEARCH_STRING: str = "shiny gold"


def get_input_entries() -> Generator[Tuple[str, Dict[str, int]], None, None]:
    with open(INPUT_FILE_NAME) as input_file:
        for line in input_file:
            containing_bag: str = findall(CONTAINING_BAG_PATTERN, line)[0]
            contained_bags: List[str] = findall(CONTAINED_BAGS_PATTERN, line)
            yield (containing_bag, dict(map(parse_bag_count, contained_bags)))


def parse_bag_count(prop: str) -> Tuple[str, int]:
    split: List[str] = prop.split(" ", 1)
    return (split[1], int(split[0]))


def construct_dict() -> Dict[str, Dict[str, int]]:
    return dict((entry[0], entry[1]) for entry in get_input_entries())


def contains_gold(
    rules: Dict[str, Dict[str, int]], calculated: Dict[str, bool], colour: str
) -> bool:
    if colour in calculated:
        return calculated[colour]

    contains: bool = (SEARCH_STRING in rules[colour]) or any(
        contains_gold(rules, calculated, child) for child in rules[colour]
    )

    calculated[colour] = contains

    return contains


def search_containing_bags(rules: Dict[str, Dict[str, int]]) -> int:
    calculated: Dict[str, bool] = {}

    for colour in rules:
        contains_gold(rules, calculated, colour)

    return sum(i for i in calculated.values())


def child_count(
    rules: Dict[str, Dict[str, int]], calculated: Dict[str, int], colour: str
) -> int:
    if colour in calculated:
        return calculated[colour]

    count: int = sum(
        rules[colour][child] * (child_count(rules, calculated, child) + 1)
        for child in rules[colour]
    )

    calculated[colour] = count

    return count


def search_gold_child_count(rules: Dict[str, Dict[str, int]]) -> int:
    return child_count(rules, {}, SEARCH_STRING)


if __name__ == "__main__":
    rules: Dict[str, Dict[str, int]] = construct_dict()
    print("result 01: ", search_containing_bags(rules))
    print("result 02: ", search_gold_child_count(rules))

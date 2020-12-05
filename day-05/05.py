from typing import Generator, Dict, Set, Optional

INPUT_FILE_NAME = "day-05-input.txt"

NUMBER_MAP: Dict[str, str] = {
    "F": "0",
    "B": "1",
    "L": "0",
    "R": "1",
}


def get_input_list() -> Generator[int, None, None]:
    with open(INPUT_FILE_NAME) as input_file:
        for line in input_file:
            yield get_seat_id(line.strip())


def get_seat_id(identifier: str) -> int:
    for item in NUMBER_MAP.items():
        identifier = identifier.replace(item[0], item[1])
    return int(identifier[:-3], 2) * 8 + int(identifier[-3:], 2)


def get_max_id() -> int:
    max_id: int = 0
    for seat_id in get_input_list():
        max_id = max(max_id, seat_id)
    return max_id


def find_my_seat() -> Optional[int]:
    ids: Set[int] = set(seat_id for seat_id in get_input_list())
    for seat_id in ids:
        # seat_id exists so is either mine + 1 or mine - 1
        # we can assume it's mine + 1 WLOG I think, just need to check mine doesn't exists and mine - 1 exists
        # note that mine would be seat_id - 1
        if seat_id - 1 not in ids and (seat_id - 2) in ids:
            return seat_id - 1
    return None


if __name__ == "__main__":
    print("result 01: ", get_max_id())
    print("result 02: ", find_my_seat())

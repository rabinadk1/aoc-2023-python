import sys
from typing import Sequence
MapItem = tuple[int, int, int]

MapperType = tuple[MapItem, ...]

def get_mappers(blocks: Sequence[str]):
    mappers_list: list[MapperType] = []
    for block in blocks:
        block_lines = block.splitlines()

        # Skip the description
        _, *block_lines = block_lines

        mapper: list[MapItem] = []

        for line in block_lines:
            dest, source, range_len = tuple(map(int, line.split(" ", 2)))
            mapper.append((source, source + range_len, dest))

        mapper_tuple = tuple(mapper)
        mappers_list.append(mapper_tuple)

    return tuple(mappers_list)

def get_lowest_location(almaniac: str):
    blocks = almaniac.split("\n\n")

    seed_block, *rest_blocks = blocks

    seeds = map(int, seed_block.split(":", 1)[1].strip().split(" "))

    mappers = get_mappers(rest_blocks)

    min_num = sys.maxsize
    for val in seeds:
        for mapper in mappers:
            for source_start, source_end, dest_start in mapper:
                if source_start <= val < source_end:
                    val = dest_start + val - source_start
                    break
        min_num = min(min_num, val)

    return min_num


if __name__ == "__main__":
    args_with_source_code = sys.argv

    if len(args_with_source_code) != 2:
        # For python solution.py
        print("Enter a input filename as the next argument.")
        sys.exit(1)

    filename = args_with_source_code[1]

    with open(filename) as f:
        inp = f.read()

    lowest_loc = get_lowest_location(inp)

    print("The lowest location is:", lowest_loc)

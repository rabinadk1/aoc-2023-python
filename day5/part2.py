from __future__ import annotations

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

    seeds = tuple(map(int, seed_block.split(":", 1)[1].strip().split(" ")))

    mappers = get_mappers(rest_blocks)

    min_num = sys.maxsize

    for seed_start, seed_range in zip(seeds[::2], seeds[1::2]):
        val_ranges = [(seed_start, seed_start + seed_range)]
        for mapper in mappers:
            mapped_val_ranges = []
            for source_start, source_end, dest_start in mapper:
                interim_val_ranges = []
                for start, end in val_ranges:
                    # Before overlap
                    before = (start, min(end, source_start))
                    before_start, before_end = before

                    # Send before overlap to interim for other mappings
                    if before_end > before_start:
                        interim_val_ranges.append(before)

                    # Send overlap directly to final range
                    inter = (max(start, source_start), min(end, source_end))
                    inter_start, inter_end = inter
                    if inter_end > inter_start:
                        offset = dest_start - source_start
                        mapped_val_ranges.append(
                            (inter_start + offset, inter_end + offset),
                        )

                    # After overlap
                    after = (max(start, source_end), end)
                    after_start, after_end = after
                    # Send before overlap to interim for other mappings
                    if after_end > after_start:
                        interim_val_ranges.append(after)
                val_ranges = interim_val_ranges
            val_ranges.extend(mapped_val_ranges)
        min_num = min(min_num, min(val_ranges)[0])

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

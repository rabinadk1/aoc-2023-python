import math
import sys


def get_metric(line: str):
    _pre, num_list = line.split(":", 1)
    return int("".join(n for n in num_list.split(" ") if n))


def get_total_beat_ways(race_sheet: str):
    giv_tim, giv_dist = tuple(map(get_metric, race_sheet.split("\n", 1)))

    # Time spent to press button = its speed
    # dist = t * (giv_tim - t)

    # For given dist, giv_dist = t * (giv_tim - t)
    # or, t*t - giv_tim * t + giv_dist = 0

    # here, a = 1, b = -giv_tim, c = giv_dist

    # t = (-b +- math.sqrt(b*b - 4*a*c))/2a
    # or, t = (giv_tim +- math.sqrt(giv_tim*giv_tim - 4*giv_dist)) / 2

    # Value needed to shift the result
    num_shift = 1e-8

    discr = math.sqrt(giv_tim * giv_tim - 4 * giv_dist)

    # lower value is ceil
    t1 = math.ceil((giv_tim - discr) / 2 + num_shift)

    # upper is floor
    t2 = math.floor((giv_tim + discr) / 2 - num_shift)

    num_beat = t2 - t1 + 1

    return num_beat


if __name__ == "__main__":
    args_with_source_code = sys.argv

    if len(args_with_source_code) != 2:
        # For python solution.py
        print("Enter a input filename as the next argument.")
        sys.exit(1)

    filename = args_with_source_code[1]

    with open(filename) as f:
        inp = f.read()

    num_beat = get_total_beat_ways(inp)

    print("The numebr of ways to beat is:", num_beat)

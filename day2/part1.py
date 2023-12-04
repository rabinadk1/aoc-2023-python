"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
"""

str_int_dict = dict[str, int]

def get_color_num_dict(conf: str):
    # rev is in this format: 3 blue, 4 red
    
    conf_dict: str_int_dict = {}
    
    # ["3", "blue"]
    for num_color in conf.split(","):
        # There could be space after comma so using left strip
        num, color = num_color.lstrip().split(" ", maxsplit=1)
        conf_dict[color] = int(num)
        
    return conf_dict

def get_sum_ids(game_inp: str, color_input_conf_dict: str_int_dict):
    sum_ids = 0
    inp_list = game_inp.splitlines()

    for line in inp_list:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game, revelations = line.split(":", maxsplit=1)

        # ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]
        for rev in revelations.split(";"):
            rev_dict = get_color_num_dict(rev)
            
            break_rev_loop = False
            for color, num in rev_dict.items():
                if num > color_input_conf_dict[color]:
                    # Break for one color
                    break_rev_loop = True
                    break
            
            # Break for one rev if broken for a color only
            if break_rev_loop:
                break
        else:
            _, game_id = game.rsplit(" ", maxsplit=1)
            sum_ids += int(game_id)
    
    return sum_ids

if __name__ == "__main__":
    import sys

    args_with_source_code = sys.argv

    if len(args_with_source_code) != 2:
        # For python solution.py
        print("Enter a input filename as the next argument.")
        exit(1)
    
    # 3 blue, 4 red
    inp_conf = input("Input configuration in this form: x color1, y color2:: ")

    try:
        inp_conf_dict = get_color_num_dict(inp_conf)
    except ValueError:
        print("\nPlease input in this form: 8 green, 6 blue, 20 red")
        exit(2)

    filename = args_with_source_code[1]

    with open(filename) as f:
        inp = f.read()

    total_sum = get_sum_ids(inp, inp_conf_dict)

    print("The total sum is:", total_sum)

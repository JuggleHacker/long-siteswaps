from utils import find_blocks, human_readable_locals

if __name__ == '__main__':
    why_not_four_two_start = [7, 8, 6, 2, 7] * 2  # 2 rounds so both jugglers get five throws
    why_not_blocks = find_blocks(why_not_four_two_start, 4, [2, 5, 6, 7, 8])
    for block in why_not_blocks:
        print(human_readable_locals(why_not_four_two_start + block))
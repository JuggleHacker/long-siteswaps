from utils import find_blocks, human_readable_locals

if __name__ == '__main__':
    why_not_four_two_start = [7, 8, 6, 2, 7] * 1  # 2 rounds so both jugglers get five throws
    block_length = 2
    valid_block_throws = [2, 5, 6, 7, 8]
    why_not_blocks = find_blocks(why_not_four_two_start, block_length, valid_block_throws)
    for block in why_not_blocks:
        print(f"Block: {block}")
        new_pattern = why_not_four_two_start + block
        print(f"New global: {new_pattern}")
        print(f"New locals: {human_readable_locals(new_pattern)}")
from utils import search_multiple_seeds, is_valid
from approvers import has_pass, no_dragon, no_repeated_pairs

if __name__ == "__main__":
    throws = [2, 4, 6, 7, 8, 9]
    filename = f"Patterns with throws {throws}.txt"
    depth = 15
    valid_pairs_of_throws = [[a, b] for a in throws for b in throws if is_valid([a, b])]
    patterns_found = search_multiple_seeds(valid_pairs_of_throws, throws, [has_pass, no_dragon, no_repeated_pairs], depth=depth)
    sorted_by_length = sorted(list(patterns_found), key=lambda x: len(x), reverse=True)
    with open(f"generate_patterns/{filename}", "w+") as f:
        f.writelines(f"{pattern}\n" for pattern in sorted_by_length)
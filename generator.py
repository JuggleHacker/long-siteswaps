from utils import search_multiple_seeds, human_readable_locals
from approvers import has_pass, no_dragon, no_repeated_pairs

def generate_patterns(throws, depth, filename):
    pairs_of_throws = [[a, b] for a in throws for b in throws]
    patterns_found = search_multiple_seeds(pairs_of_throws, throws, [has_pass, no_dragon, no_repeated_pairs],
                                           depth=depth)
    sorted_by_length = sorted(list(patterns_found), key=lambda x: len(x), reverse=True)
    with open(f"generated_patterns/{filename}", "w+") as f:
        f.writelines(f"{human_readable_locals(pattern)}\n" for pattern in sorted_by_length)

if __name__ == "__main__":
    # here I am using "singles" to means 6s and 7s. "Doubles" means 8s and 9s
    zips_singles_and_doubles = [2, 6, 7, 8, 9]
    zips_holds_singles_and_doubles = [2, 4, 6, 7, 8, 9]
    zips_zaps_singles_and_doubles = [2, 5, 6, 7, 8, 9]
    zips_holds_zaps_singles_and_doubles = [2, 4, 5, 6, 7, 8, 9]
    zaps_singles_and_doubles = [5, 6, 7, 8, 9]
    zaps_singles_doubles_and_trelfs = [5, 6, 7, 8, 9, 10]

    throws = zips_singles_and_doubles
    throws = zips_holds_zaps_singles_and_doubles
    filename = f"Patterns with throws {throws}.txt"
    depth = 15
    generate_patterns(throws, depth, filename)
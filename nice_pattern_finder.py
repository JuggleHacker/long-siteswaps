with open("generated_patterns/Period 19s with throws [2, 4, 5, 6, 7, 8, 9].txt") as f:
    lines = f.readlines()
    sorted_by_number_of_flips = sorted(lines, key=lambda pattern: pattern.count("4"))
    for pattern in sorted_by_number_of_flips[:10]:
        print(pattern, end="")
    print()
    for pattern in sorted_by_number_of_flips[-10:]:
        print(pattern, end="")
def is_valid(siteswap):
    landing_sites = set()
    for time, throw in enumerate(siteswap):
        if throw != "?":
            landing_site = (time + throw) % len(siteswap)
            if landing_site in landing_sites:
                return False
            else:
                landing_sites.add(landing_site)
    return True

def ways_to_complete(siteswap, throws, approvers=None):
    if not is_valid(siteswap):
        return
    if "?" not in siteswap:
        approved = (approvers is None) or all(approver(siteswap) for approver in approvers)
        if approved:
            yield siteswap
    else:
        first_unknown_throw = siteswap.index("?")
        for throw in throws:
            new_siteswap = siteswap[:first_unknown_throw] + [throw] + siteswap[first_unknown_throw+1:]
            yield from ways_to_complete(new_siteswap, throws, approvers)

def two_locals_to_global(local_one, local_two):
    global_siteswap = []
    for pair in zip(local_one, local_two):
        global_siteswap.extend(pair)
    return global_siteswap

def global_to_two_locals(siteswap):
    return siteswap[0::2], siteswap[1::2]

def extend_global_preserving_both_locals(siteswap, extra_throws):
    return siteswap + ["?"] * (2 * extra_throws)

def ways_to_extend(siteswap, throws, extra_throws, approver=None):
    yield from ways_to_complete(extend_global_preserving_both_locals(siteswap, extra_throws), throws, approver)


def is_siteswap_already_there(siteswap, pool):
    for i in range(len(siteswap)):
        return siteswap[i:] + siteswap[:i] in pool

def search(pattern, throws, approvers, depth):
    if depth == 0:
        yield pattern
    else:
        extended_siteswap = extend_global_preserving_both_locals(pattern, 2)
        ways = ways_to_complete(extended_siteswap, throws, approvers)
        next_patterns = []
        for options in ways:
            if not is_siteswap_already_there(options, next_patterns):
                next_patterns.append(options)
        if not next_patterns:
            if is_valid(pattern):
                yield pattern
        else:
            for next_pattern in next_patterns:
                yield from search(next_pattern, throws, approvers, depth - 1)

def search_multiple_seeds(patterns, throws, approvers, depth):
    for pattern in patterns:
        yield from search(pattern, throws, approvers, depth)


def human_readable_string(siteswap):
    throw_string = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "".join(throw_string[throw] for throw in siteswap)

def human_readable_locals(siteswap):
    locals = global_to_two_locals(siteswap)
    return " vs ".join(human_readable_string(local) for local in locals)

def state(siteswap):
    max_throw = max(siteswap)
    landing_sites = set()
    for i in range(1, max_throw+1):
        landing_site = -i + siteswap[-i % len(siteswap)]
        if landing_site >= 0:
            landing_sites.add(landing_site)
    siteswap_state = [0] * (max(landing_sites) + 1)
    for landing_site in landing_sites:
        siteswap_state[landing_site] = 1
    return siteswap_state

def find_blocks(siteswap, block_length, valid_block_throws):
    """
    A "block" is a series of throws which can be added to the end of a valid siteswap to give a longer valid siteswap.
    This function will find all blocks of length block_length consisting of valid_block_throws which can be used
    to extend the given siteswap.
    For example, if you are trying to extend 6 club why-not, starting from the 4-2 start:
    why_not_four_two_start = [7,8,6,2,7] * 2  # 2 rounds so both jugglers get five throws
    why_not_blocks = find_blocks(why_not_four_two_start(why_not_four_two_start, 4, [2, 6, 7, 8]))
    print(why_not_blocks)
    >> [[7, 7, 8, 2], [8, 6, 8, 2]]
    This means both the following are valid patterns:
    [7, 8, 6, 2, 7, 7, 8, 6, 2, 7, 7, 7, 8, 2]
    and
    [7, 8, 6, 2, 7, 7, 8, 6, 2, 7, 8, 6, 8, 2]
    """
    blocks_length_4 = [block[-4:] for block in ways_to_complete(siteswap + ['?'] * block_length, valid_block_throws)]
    return blocks_length_4

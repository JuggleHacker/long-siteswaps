from approvers import has_pass, no_dragon, no_repeated_pairs

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
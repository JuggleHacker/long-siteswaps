def has_pass(siteswap):
    for throw in siteswap:
        if throw % 2 == 1:
            return True
    return False

def no_dragon(siteswap):
    for time in range(len(siteswap)):
        if siteswap[time] == 9 and siteswap[(time+2)%len(siteswap)] == 5:
            return False
    return True

def no_repeated_pairs(siteswap):
    a_throws = siteswap[0::2]
    a_pairs = set(zip(a_throws, a_throws[1:]+[a_throws[0]]))
    if len(a_pairs) != len(a_throws):
        return False
    b_throws = siteswap[1::2]
    b_pairs = set(zip(b_throws, b_throws[1:] + [b_throws[0]]))
    if len(b_pairs) != len(b_throws):
        return False
    return True
from utils import state


def has_pass(siteswap):
    for throw in siteswap:
        if throw % 2 == 1:
            return True
    return False

def has_double(siteswap):
    for throw in siteswap:
        if throw == 9:
            return True
    return False

def has_heff(siteswap):
    for throw in siteswap:
        if throw == 8:
            return True
    return False

def has_throw(n):
    def to_return(siteswap):
        for throw in siteswap:
            if throw == n:
                return True
        return False
    return to_return


def has_zip(siteswap):
    for throw in siteswap:
        if throw == 2:
            return True
    return False

def has_7_objects(siteswap):
    return sum(siteswap) / len(siteswap) == 7

def has_6_objects(siteswap):
    return sum(siteswap) / len(siteswap) == 6

def has_n_objects(n):
    return lambda siteswap: sum(siteswap) / len(siteswap) == n

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

def is_ground_state(siteswap):
    return 0 not in state(siteswap)
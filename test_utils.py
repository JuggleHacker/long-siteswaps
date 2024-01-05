from utils import is_valid, ways_to_complete, two_locals_to_global, global_to_two_locals, extend_global_preserving_both_locals, ways_to_extend, search
from approvers import has_pass

def test_is_valid_with_valid():
    valids = [
        [5, 3, 4],
        [5, 6, "?"],
    ]
    for valid in valids:
        assert is_valid(valid)

def test_is_valid_with_invalid():
    assert not is_valid([5, 4, 4])

def test_ways_to_complete_one_missing():
    one_missing = [5, 6, "?"]
    throws = [4, 5, 6, 7]
    options = ways_to_complete(one_missing, throws)
    assert list(options) == [[5, 6, 4], [5, 6, 7]]

def test_ways_to_complete_with_approver():
    two_missing = ["?", "?", 6]
    throws = [5, 6, 7]
    options = ways_to_complete(two_missing, throws, [has_pass])
    assert list(options) == [[7, 5, 6]] # no [6, 6, 6]
def test_locals_to_global():
    local_one = [1, 2, 3]
    local_two = [4, 5, 6]
    assert two_locals_to_global(local_one, local_two) == [1, 4, 2, 5, 3, 6]

def test_global_to_two_locals():
    global_siteswap = [1, 2, 3, 4, 5, 6]
    assert global_to_two_locals(global_siteswap) == ([1, 3, 5], [2, 4, 6])

def test_extend_global():
    global_siteswap = [8, 6, 7, 7, 7, 7]
    assert extend_global_preserving_both_locals(global_siteswap, 2) == [8, 6, 7, 7, 7, 7, "?", "?", "?", "?"]

def test_ways_to_extend():
    siteswap = [8, 6]
    throws = [5, 6, 7, 8, 9]
    options = ways_to_extend(siteswap, throws, extra_throws=2)
    assert [8, 6, 7, 7, 7, 7] in options

def test_search_depth_0():
    assert list(search([8, 6], [4, 5, 6, 7, 8, 9], [has_pass], depth=0)) == [[8, 6]]

def test_search_depth_1():
    known_pattern = [[8, 6, 7, 7, 7, 7]]
    all_patterns = list(search([8, 6], [4, 5, 6, 7, 8, 9], [has_pass], depth=1))
    assert  all(pattern in all_patterns for pattern in known_pattern)
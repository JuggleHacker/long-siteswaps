from approvers import has_pass, no_dragon, no_repeated_pairs, is_ground_state

def test_has_pass():
    assert has_pass([6, 6, 6]) == False
    assert has_pass([7, 5, 6]) == True

def test_no_dragon():
    assert no_dragon([9, 7, 5]) == False
    assert no_dragon([7, 5, 9]) == False
    assert no_dragon([9, 5, 6]) == True

def test_no_repeated_pairs():
    assert no_repeated_pairs([8, 6, 7, 7, 7, 7])  # heff pass, pass pass, pass heff all different
    assert not no_repeated_pairs([8, 6, 7, 7, 7, 7, 7, 7])  # have two pass passes
    assert no_repeated_pairs([8, 6, 7, 7, 4, 4])

def test_is_ground_state():
    assert is_ground_state([7, 7, 7, 7, 2, 6])
    assert not is_ground_state([7, 7, 7, 2, 6, 7])  # state is [1, 1, 1, 1, 1, 0, 1]
from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_too_high_hint_says_lower():
    # Bug 1: hint message used to say "Go HIGHER" when guess was too high
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_hint_says_higher():
    # Bug 1: hint message used to say "Go LOWER" when guess was too low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_check_guess_both_ints():
    # Bug 2: secret was sometimes passed as a string, causing type mismatch
    # Both args should be ints and produce correct results
    outcome, _ = check_guess(50, 25)
    assert outcome == "Too High"
    outcome, _ = check_guess(25, 50)
    assert outcome == "Too Low"

def test_hard_mode_harder_than_normal():
    # Bug 3: Hard mode range was 1-50, easier than Normal's 1-100
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high

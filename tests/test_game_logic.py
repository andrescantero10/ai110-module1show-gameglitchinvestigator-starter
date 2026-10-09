from logic_utils import check_guess, get_range_for_difficulty, update_score, parse_guess

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

def test_win_on_first_attempt_score():
    # Bug 5: formula used (attempt_number + 1), giving 80 instead of 90
    score = update_score(0, "Win", 1)
    assert score == 90

def test_too_high_always_loses_points():
    # Bug 6: "Too High" on even attempts used to gain +5 instead of -5
    score = update_score(50, "Too High", 2)
    assert score == 45
    score = update_score(50, "Too High", 3)
    assert score == 45

# --- Edge-case tests ---

def test_negative_number_rejected():
    # Negative numbers are outside the valid range and should be rejected
    ok, value, err = parse_guess("-5", 1, 100)
    assert ok is False
    assert "Out of range" in err

def test_huge_number_rejected():
    # Numbers way above the range should be rejected
    ok, value, err = parse_guess("99999999", 1, 100)
    assert ok is False
    assert "Out of range" in err

def test_non_numeric_string_rejected():
    # Letters and words should be rejected as not a number
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert "not a number" in err

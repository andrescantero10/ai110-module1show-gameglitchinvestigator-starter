def get_range_for_difficulty(difficulty: str):
    # FIX: Hard mode was 1-50 (easier than Normal). Changed to 1-200. Claude Code proposed it, I reviewed the diff.
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    # FIX: flipped hint messages (was saying "Go HIGHER" when too high) and removed TypeError workaround for string comparison. Claude Code proposed it, I reviewed the diff.
    """Compare guess to secret and return (outcome, message)."""
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    # FIX: score formula used (attempt_number + 1) causing off-by-one, and "Too High" gained points on even attempts. Claude Code proposed it, I reviewed the diff.
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points
    if outcome == "Too High" or outcome == "Too Low":
        return current_score - 5
    return current_score

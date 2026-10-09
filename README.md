# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] The game is a number guessing game where you pick a difficulty, get a range, and try to guess the secret number within a limited number of attempts. You get hints after each guess and earn points based on how quickly you win.
- [x] Bugs found: backwards hint messages, type mismatch on even attempts, Hard mode easier than Normal, attempts starting at 1, score off-by-one, inconsistent scoring for wrong guesses, hardcoded range display.
- [x] Fixes: flipped hint messages, removed string conversion, changed Hard range to 1-200, started attempts at 0, fixed score formula, made wrong guesses always lose 5 points, used dynamic range in info bar, added range validation to parse_guess.

## 📸 Demo Walkthrough

1. Start the app on Normal difficulty. The page says "Guess a number between 1 and 100. Attempts left: 8." Open Developer Debug Info to see the secret number (let's say it's 73).
2. Guess 50 and click Submit. The hint says "Go HIGHER!" and your score drops by 5 to -5. Attempts left: 7.
3. Guess 80 and click Submit. The hint says "Go LOWER!" and your score drops to -10. Attempts left: 6.
4. Guess 70 and click Submit. The hint says "Go HIGHER!" Score: -15. Attempts left: 5.
5. Guess 73 and click Submit. Balloons appear and it says "You won! The secret was 73. Final score: 35." (You get 100 - 10*4 = 60 points for winning on attempt 4, added to -15.)
6. Click New Game to start over with a fresh secret number and score.

## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.12.4, pytest-9.1.1, pluggy-1.6.0
tests/test_game_logic.py::test_winning_guess PASSED                      [  8%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 16%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 25%]
tests/test_game_logic.py::test_too_high_hint_says_lower PASSED           [ 33%]
tests/test_game_logic.py::test_too_low_hint_says_higher PASSED           [ 41%]
tests/test_game_logic.py::test_check_guess_both_ints PASSED              [ 50%]
tests/test_game_logic.py::test_hard_mode_harder_than_normal PASSED       [ 58%]
tests/test_game_logic.py::test_win_on_first_attempt_score PASSED         [ 66%]
tests/test_game_logic.py::test_too_high_always_loses_points PASSED       [ 75%]
tests/test_game_logic.py::test_negative_number_rejected PASSED           [ 83%]
tests/test_game_logic.py::test_huge_number_rejected PASSED               [ 91%]
tests/test_game_logic.py::test_non_numeric_string_rejected PASSED        [100%]
============================== 12 passed in 0.01s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game looked like a normal number guessing game at first, but once I started playing it became clear something was really wrong. I guessed 300 on a 1-100 range and it told me to go higher, which made no sense. Then I tried 50, 75, 90, 100 and it kept saying go higher until suddenly at 100 it said go lower. The hints were completely backwards, and on top of that the game was switching between comparing numbers and comparing strings on every other guess, which made the hints unreliable even beyond being reversed. I also noticed the attempt counter started at 1 before I even guessed, so I was losing a turn right from the start.

**Bug Reproduction Log**

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|------------|-------------------|-----------------|------------------------|
| Guessed 300 (secret was 25, Normal mode) | Should say "Too High, go lower" | Said "Go HIGHER!" with an up arrow emoji | No console error |
| Guessed 50 on 2nd attempt (secret was 25) | Should say "Too High, go lower" | Compared int 50 to string "25", string comparison gave wrong result | No console error, but check_guess hit the TypeError except block |
| Loaded game on Normal, no guesses yet | Should say "Attempts left: 8" | Said "Attempts left: 7" because attempts starts at 1 instead of 0 | No console error |
| Switched to Hard mode | Range should be harder than Normal (e.g. 1-200) | Range was 1-50, which is actually easier than Normal's 1-100 | No console error |
| Won on attempt 1 | Should earn 90 points (100 - 10*1) | Earned 80 points because formula uses (attempt_number + 1) | No console error |
| Guessed too high on an even attempt | Should lose points (-5) | Gained 5 points instead because of an even/odd check in update_score | No console error |
| Playing on Easy mode | Info bar should say "between 1 and 20" | Said "between 1 and 100" because it's hardcoded | No console error |

---

## 2. How did you use AI as a teammate?

I used Claude Code for this project. One correct suggestion it made was that the hint messages in check_guess were backwards. It pointed to lines 37-40 where "Too High" returned "Go HIGHER!" and explained that the messages needed to be flipped. I verified this by playing the game after the fix and seeing that guessing above the secret now correctly says "Go LOWER."

One suggestion that was correct but felt like a big jump was when Claude Code proposed fixing Bugs 1 and 2 together in the same commit, moving check_guess to logic_utils.py while also removing the string conversion code. Both changes were right, but it was a lot to review at once. I checked every line of the diff before approving it and then played the game on both odd and even attempts to make sure it all worked.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by going back and playing the game myself, not just trusting the tests. After each fix I would restart the app and try the exact inputs that were broken before. For example, after fixing the hints I guessed a number above the secret and confirmed it now said "Go LOWER" instead of "Go HIGHER."

Claude Code also wrote pytest tests that targeted each specific bug, like checking that check_guess(60, 50) returns "Too High" with "LOWER" in the message. Running pytest after every change made sure I didn't break anything while fixing something else. Claude Code designed the tests and I reviewed them to make sure they were actually testing the right thing.

---

## 4. What did you learn about Streamlit and state?

I hadn't used Streamlit before this project. The main thing I learned is that every time you click a button, Streamlit reruns the entire script from top to bottom. Without session_state, everything would reset on every click, so the secret number would change, the score would go back to zero, and you could never finish a game. That's why the code uses checks like "if secret not in st.session_state" to only set values the first time. I also noticed that the submit button only works when you click it, not when you press enter, which is just how Streamlit works.

---

## 5. Looking ahead: your developer habits

The habit I want to reuse is testing the app manually by pushing it to its limits before looking at the code. I started by putting in numbers way outside the range like 300 and -5, and that immediately showed me things were broken. That approach of trying to break it first is something I'll keep doing.

Next time I work with AI on code, I would still review every diff carefully before applying it. The bugs in this project were all simple mistakes, and that taught me that AI-generated code can look fine at first glance but have small logic errors that only show up when you actually use it. You have to test it yourself.

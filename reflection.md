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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative number (-5) | "I noticed negative numbers don't get rejected" | test_negative_number_rejected: parse_guess("-5", 1, 100) should return ok=False with "Out of range" | Yes | The game range starts at 1, so negative numbers should not be accepted as valid guesses |
| Huge number (99999999) | "Find edge-case inputs that might still break the game" | test_huge_number_rejected: parse_guess("99999999", 1, 100) should return ok=False with "Out of range" | Yes | Numbers way above the range waste a turn and give misleading hints instead of telling the player to stay in bounds |
| Non-numeric string ("abc") | "Find edge-case inputs that might still break the game" | test_non_numeric_string_rejected: parse_guess("abc", 1, 100) should return ok=False with "not a number" | Yes | Letters and words should be caught before they reach the comparison logic |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->

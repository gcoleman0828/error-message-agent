A beginner-friendly agentic AI learning project that classifies pasted error messages and recommends the first troubleshooting step.

What This Project Does

Version 1 should be intentionally simple.

The user pastes an error message such as:

```bash

Permission denied (publickey).
fatal: Could not read from remote repository.

```

The agent returns:

```bash

Category: Git / SSH Authentication

Likely Cause:
Your Ubuntu VM does not have a valid SSH key configured for GitHub, or GitHub does not know about the public key from this VM.

First Command to Run:
ssh -T git@github.com

Expected Result:
A successful setup usually says that GitHub authenticated you, but shell access is not provided.

What To Do Next:
If authentication fails, check whether ~/.ssh contains a key pair and whether the public key has been added to GitHub.

```

```bash

The Simple Architecture

For version 1, think of the agent as five small parts:

User Error Message
        |
        v
[ Observe ]
Read the pasted error text
        |
        v
[ Classify ]
Decide what category the error belongs to
        |
        v
[ Route ]
Pick the right troubleshooting rule
        |
        v
[ Recommend ]
Return the first command/check
        |
        v
[ Next Action ]
Tell the user what to do based on the result

```

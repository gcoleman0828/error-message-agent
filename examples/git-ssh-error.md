# Example: Git / SSH Authentication Error

## Input

```text
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
Please make sure you have the correct access rights
and the repository exists.
```

## Expected Category
Git / SSH Authentication

## Expected Output

## Error Category
Git / SSH Authentication

## Likely Cause
The Ubuntu VM does not have a valid SSH key configured for GitHub, or the public key from this VM has not been added to the user's GitHub account.

## First Command or Check

```bash
ssh -T git@github.com
```

## Expected Result

If SSH is configured correctly, GitHub should return a message saying authentication was successful, but GitHub does not provide shell access.

## What To Do Next
If the SSH test fails, check whether this VM already has SSH keys

```bash
ls -la ~/.ssh
```

## Confidence
High



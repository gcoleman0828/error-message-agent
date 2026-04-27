"""
Error Message Classifier Agent

Version 1:
Recognizes these error types:

1. Git / SSH Authentication
2. Docker Permission Error
3. Python Dependency Error

Agent pattern:
observe -> classify -> route -> recommend
"""


def observe(error_message):
    """
    Normalize the pasted error message so it is easier to classify.
    """
    return error_message.lower()


def classify(observed_error):
    """
    Classify the error message into one known category.
    """

    if "permission denied (publickey)" in observed_error:
        return "Git / SSH Authentication"

    if "could not read from remote repository" in observed_error:
        return "Git / SSH Authentication"

    if "git@github.com" in observed_error:
        return "Git / SSH Authentication"

    if "docker.sock" in observed_error:
        return "Docker Permission Error"

    if "permission denied while trying to connect to the docker daemon socket" in observed_error:
        return "Docker Permission Error"

    if "/var/run/docker.sock" in observed_error:
        return "Docker Permission Error"

    if "modulenotfounderror" in observed_error:
        return "Python Dependency Error"

    if "no module named" in observed_error:
        return "Python Dependency Error"

    if "importerror" in observed_error:
        return "Python Dependency Error"

    return "Unknown"


def route(category):
    """
    Route the classified category to the correct troubleshooting rule.
    """

    if category == "Git / SSH Authentication":
        return {
            "category": "Git / SSH Authentication",
            "likely_cause": "The Ubuntu VM does not have a valid SSH key configured for GitHub, or the public key from this VM has not been added to the user's GitHub account.",
            "first_check": "ssh -T git@github.com",
            "expected_result": "If SSH is configured correctly, GitHub should return a message saying authentication was successful, but GitHub does not provide shell access.",
            "next_action": "If the SSH test fails, check whether this VM already has SSH keys with: ls -la ~/.ssh",
            "confidence": "High",
        }

    if category == "Docker Permission Error":
        return {
            "category": "Docker Permission Error",
            "likely_cause": "The current Ubuntu user does not have permission to use Docker without sudo. This usually means the user is not in the docker group, or the user was recently added to the group but has not started a new login session yet.",
            "first_check": "groups",
            "expected_result": "The output should include docker.",
            "next_action": "If docker is missing from the group list, run: sudo usermod -aG docker $USER. Then log out and log back in, or run: newgrp docker for a faster test. After that, test Docker again with: docker ps",
            "confidence": "High",
        }

    if category == "Python Dependency Error":
        return {
            "category": "Python Dependency Error",
            "likely_cause": "A required Python package is not installed in the active Python environment.",
            "first_check": "python -m pip list",
            "expected_result": "The installed Python packages should be listed. The missing package will probably not appear in the list.",
            "next_action": "If the missing package is not listed, install it in the correct Python environment. For example: python -m pip install package-name",
            "confidence": "High",
        }

    return {
        "category": "Unknown",
        "likely_cause": "The error message does not match a supported rule yet.",
        "first_check": "Review the full error message.",
        "expected_result": "You should identify words or phrases that can become match signals.",
        "next_action": "Add a new routing rule for this error type.",
        "confidence": "Low",
    }


def recommend(error_message):
    """
    Run the full agent workflow.
    """
    observed_error = observe(error_message)
    category = classify(observed_error)
    recommendation = route(category)
    return recommendation


def print_recommendation(result):
    """
    Print the final recommendation in a clean format.
    """
    print()
    print("## Error Category")
    print()
    print(result["category"])

    print()
    print("## Likely Cause")
    print()
    print(result["likely_cause"])

    print()
    print("## First Command or Check")
    print()
    print("```bash")
    print(result["first_check"])
    print("```")

    print()
    print("## Expected Result")
    print()
    print(result["expected_result"])

    print()
    print("## What To Do Next")
    print()
    print(result["next_action"])

    print()
    print("## Confidence")
    print()
    print(result["confidence"])


if __name__ == "__main__":
    print("Paste one error message and press Enter:")
    print()

    user_input = input("> ")

    result = recommend(user_input)
    print_recommendation(result)
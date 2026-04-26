"""
Error Message Classifier Agent

Version 1:
Recognizes one error type:
Git / SSH Authentication

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

    if "docker.sock" in observed_error:
        return "Docker Permission Error"

    if (
        "permission denied while trying to connect to the docker daemon socket"
        in observed_error
    ):
        return "Docker Permission Error"

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
            "likely_cause": "The current Ubuntu user may not be in the docker group, or the user was added to the group but has not logged out and back in yet.",
            "first_check": "groups",
            "expected_result": "The output should include docker.",
            "next_action": "If docker is missing, run: sudo usermod -aG docker $USER. Then log out and back in, or run: newgrp docker. After that, test with: docker ps",
            "confidence": "High",
        }

        # return to user when the error messae does not match any known category
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

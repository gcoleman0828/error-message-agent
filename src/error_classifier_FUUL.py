#!/usr/bin/env python3
"""
Error Message Classifier Agent

This script classifies technical error messages and provides troubleshooting guidance.
"""

import sys
import re
from typing import Dict, Tuple, Optional


class ErrorClassifier:
    """Classifies error messages and provides troubleshooting recommendations."""

    def __init__(self):
        self.categories = {
            'git_ssh': {
                'patterns': [
                    r'Permission denied \(publickey\)\.',
                    r'fatal: Could not read from remote repository',
                    r'git@github\.com: Permission denied',
                    r'Host key verification failed',
                    r'SSH key not found',
                    r'Authentication failed'
                ],
                'category': 'Git / SSH',
                'common_causes': [
                    'SSH key not configured or not added to ssh-agent',
                    'SSH key not added to GitHub account',
                    'Wrong SSH key or repository URL',
                    'SSH agent not running'
                ]
            },
            'docker': {
                'patterns': [
                    r'docker: Got permission denied',
                    r'Cannot connect to the Docker daemon',
                    r'docker daemon is not running',
                    r'docker: command not found',
                    r'Got permission denied while trying to connect',
                    r'docker.sock'
                ],
                'category': 'Docker',
                'common_causes': [
                    'User not in docker group',
                    'Docker daemon not running',
                    'Docker not installed',
                    'Permission issues with docker.sock'
                ]
            },
            'permissions': {
                'patterns': [
                    r'Permission denied',
                    r'Operation not permitted',
                    r'Access denied',
                    r'chmod',
                    r'chown',
                    r'sudo'
                ],
                'category': 'Linux permissions',
                'common_causes': [
                    'Insufficient file permissions',
                    'Running as wrong user',
                    'Directory ownership issues',
                    'Executable permissions missing'
                ]
            },
            'python_fastapi': {
                'patterns': [
                    r'ImportError',
                    r'ModuleNotFoundError',
                    r'fastapi',
                    r'uvicorn',
                    r'python.*not found',
                    r'pip install',
                    r'requirements\.txt'
                ],
                'category': 'Python / FastAPI',
                'common_causes': [
                    'Missing Python packages',
                    'Virtual environment not activated',
                    'Python path issues',
                    'FastAPI/Uvicorn not installed'
                ]
            },
            'network_port': {
                'patterns': [
                    r'port.*already in use',
                    r'bind.*address already in use',
                    r'connection refused',
                    r'network is unreachable',
                    r'port 80',
                    r'port 443',
                    r'localhost.*refused'
                ],
                'category': 'Network / port',
                'common_causes': [
                    'Port already in use by another process',
                    'Service not running',
                    'Firewall blocking connection',
                    'Wrong host/port configuration'
                ]
            }
        }

    def classify_error(self, error_message: str) -> Dict[str, str]:
        """
        Classify the error message and return troubleshooting information.

        Args:
            error_message: The error message to classify

        Returns:
            Dictionary with category, cause, command, expected_result, next_action
        """
        error_lower = error_message.lower()

        # Check each category for pattern matches
        for category_key, category_info in self.categories.items():
            for pattern in category_info['patterns']:
                if re.search(pattern, error_message, re.IGNORECASE):
                    return self._get_troubleshooting_info(category_key, category_info, error_message)

        # If no pattern matches, return unknown
        return {
            'category': 'Unknown',
            'likely_cause': 'Unable to determine from the provided error message',
            'first_command': 'Please provide more context or the full error message',
            'expected_result': 'N/A',
            'next_action': 'Share additional details about what you were trying to do'
        }

    def _get_troubleshooting_info(self, category_key: str, category_info: Dict, error_message: str) -> Dict[str, str]:
        """Get specific troubleshooting information for a matched category."""
        category = category_info['category']
        causes = category_info['common_causes']

        # Select the most likely cause (first one for simplicity)
        likely_cause = causes[0] if causes else 'Unknown cause'

        # Get appropriate first command based on category
        command_info = self._get_first_command(category_key, error_message)

        return {
            'category': category,
            'likely_cause': likely_cause,
            'first_command': command_info['command'],
            'expected_result': command_info['expected'],
            'next_action': command_info['next_action']
        }

    def _get_first_command(self, category_key: str, error_message: str) -> Dict[str, str]:
        """Determine the first safe command to run based on category."""
        commands = {
            'git_ssh': {
                'command': 'ssh -T git@github.com',
                'expected': 'Success message or authentication prompt',
                'next_action': 'If successful, try your git command again. If failed, check SSH key setup.'
            },
            'docker': {
                'command': 'docker --version',
                'expected': 'Docker version information',
                'next_action': 'If Docker is installed, check if daemon is running with "sudo systemctl status docker"'
            },
            'permissions': {
                'command': 'ls -la <problematic_file_or_directory>',
                'expected': 'File permissions and ownership information',
                'next_action': 'Check if you have read/write/execute permissions. Use chmod/chown if needed.'
            },
            'python_fastapi': {
                'command': 'python --version && pip list | grep -i fastapi',
                'expected': 'Python version and FastAPI in installed packages',
                'next_action': 'If FastAPI not installed, run "pip install fastapi uvicorn"'
            },
            'network_port': {
                'command': 'netstat -tlnp | grep <port_number>',
                'expected': 'Process using the port or no output if port is free',
                'next_action': 'If port is in use, identify the process and stop it, or use a different port'
            }
        }

        return commands.get(category_key, {
            'command': 'Please provide more details',
            'expected': 'N/A',
            'next_action': 'Share the full error message and context'
        })


def main():
    """Main function to run the error classifier."""
    print("Error Message Classifier Agent")
    print("=" * 40)
    print("Paste your error message below (press Ctrl+D when done):")
    print()

    try:
        # Read error message from stdin
        error_message = sys.stdin.read().strip()

        if not error_message:
            print("No error message provided.")
            return

        # Classify the error
        classifier = ErrorClassifier()
        result = classifier.classify_error(error_message)

        # Display results
        print("\nClassification Results:")
        print("-" * 20)
        print(f"Category: {result['category']}")
        print(f"Likely Cause: {result['likely_cause']}")
        print(f"First Command/Check: {result['first_command']}")
        print(f"Expected Result: {result['expected_result']}")
        print(f"Next Action: {result['next_action']}")

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
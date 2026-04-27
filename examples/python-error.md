# Example: Python Dependency Error

## Input

```text
ModuleNotFoundError: No module named 'fastapi'
```

## Expected Category

Python Dependency Error

## Expected Output

## Error Category

Python Dependency Error

## Likely Cause

A required Python package is not installed in the active Python environment.

## First Command or Check

```bash
python -m pip list
```

## Expected Result

The installed Python packages should be listed. The missing package will probably not appear in the list.

## What To Do Next

If the missing package is not listed, install it in the correct Python environment.

Example:

```bash
python -m pip install fastapi
```

## Confidence
High
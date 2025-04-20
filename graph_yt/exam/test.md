9. Run Python Code Inside Another Python Process
Problem: Given a string that contains a mixture of digits, letters, and special characters, your task is to find the first digit that appears after any special character (defined as any character other than a letter or digit). If no digit appears after a special character, return -1. You need to execute a Python script inside a separate process and retrieve its output. Write a Python program that runs another script (child.py) using subprocess.

You are given a string that may contain a mixture of letters, digits, and special characters. Your task is to find the first digit that appears after any special character (where a special character is anything not a letter or digit).

You need to:

- Write the logic in a script named child.py that accepts a string argument,
- Execute this logic by calling child.py from another script parent.py using the subprocess module,
- Return the output back to parent.py, which captures and prints the result. If no such digit exists, return -1.

child.py

Input: "a#4b3c"

Input: "abc!5def"

Input: "xy!z9"
Example Input: Run the child script from parent.py:

output = run_child_process("child.py")
Expected Output:

Input: a#4b3c → Output: 4
Input: abc!5def → Output: 5
Input: xy!z9 → Output: -1
Constraints:

Use the subprocess module.
Ensure that parent.py correctly captures and prints the output from child.py.
Time Estimate: 2 hours
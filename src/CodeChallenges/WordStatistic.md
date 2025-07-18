# Word Statistics Challenge

## Description

Create a program that processes a text input and calculates the following statistics:

1. The longest word in the text.
2. The most frequent word (case-insensitive).
3. The average word length.

## Requirements

- Accept a text input from the user.
- Ignore punctuation and special characters, processing only alphabetical words.
- Words are separated by spaces and punctuation.
- If there is a tie for the most frequent word, return any of the tied words.

## Example Input

```
Enter the text:
The quick brown fox jumps over the lazy dog. The fox is quick.
```

## Expected Output

```
The longest word is: jumps
The most frequent word is: the
The average word length is: 4.33
```

## Additional Notes

- Use Python data structures like `dict` or `list` as needed.
- Handle empty or invalid input gracefully with appropriate error messages.
- Ensure the average word length is displayed with two decimal precision.

## Submission

- Ensure the program is functional and well-commented.
- Test the program with multiple inputs, including edge cases.

## Stretch Goals

If you finish early, consider:

- Handling inputs in multiple languages (e.g., with accented characters).
- Adding unit tests for your solution using Python's `unittest` module.

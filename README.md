# generateParenthesis-leetcode
# Well-Formed Parentheses Combinations

This program generates all combinations of well-formed parentheses given a certain number of pairs of parentheses.

## Problem Description

Given an integer `n`, the program generates all combinations of well-formed parentheses containing `n` pairs of parentheses.

A combination of parentheses is considered well-formed if it meets the following conditions:
- It starts with an open parenthesis "(".
- It ends with a close parenthesis ")".
- For each open parenthesis, there is a corresponding close parenthesis that comes after it.

For example, when `n = 3`, the program should generate the following combinations:
- "((()))"
- "(()())"
- "(())()"
- "()(())"
- "()()()"

## Usage

The program is written in Python. Follow the steps below to use the code:

1. Make sure you have Python installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

2. Copy the code from the `solution.py` file in this repository.

3. Create a new Python file in your preferred editor.

4. Paste the code into the new Python file.

5. Instantiate the `Solution` class:

    ```python
    solution = Solution()
    ```

6. Call the `generateParenthesis` method on the `solution` object, passing the desired number of pairs of parentheses as an argument:

    ```python
    result = solution.generateParenthesis(3)
    ```

    Replace `3` with the desired number of pairs of parentheses.

7. The method will return a list of strings representing all combinations of well-formed parentheses. You can store the result in a variable (`result` in the example above) and use it as needed.

8. Optionally, you can print the result to see the generated combinations:

    ```python
    print(result)
    ```

9. Run the Python script, and the program will generate the well-formed parentheses combinations based on the provided input.

10. Experiment with different values of `n` to generate combinations for different numbers of pairs of parentheses.

## Contributing

If you have any improvements or suggestions for this program, feel free to contribute! You can submit a pull request with your changes, and they will be reviewed.

If you encounter any issues or have any questions, please create an issue in this repository.

## License

This program is released under the [MIT License](LICENSE).

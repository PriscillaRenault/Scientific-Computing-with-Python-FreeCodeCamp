def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists to store each line of the arranged problems
    first_line = []
    second_line = []
    dashes = []
    answers = []

    # Process each problem
    for problem in problems:
        # Split the problem into components
        parts = problem.split()
        
        # Check if the format is correct
        if len(parts) != 3:
            return "Error: Each problem should have exactly 3 parts."
        
        first_number = parts[0]
        operator = parts[1]
        second_number = parts[2]

        # Check if operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if numbers are valid
        if not (first_number.isdigit() and second_number.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check if numbers are too long
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate width of the problem
        width = max(len(first_number), len(second_number)) + 2
        
        # Format each line
        first_line.append(first_number.rjust(width))
        second_line.append(operator + second_number.rjust(width - 1))
        dashes.append('-' * width)

        # Calculate answer if required
        if show_answers:
            if operator == '+':
                answer = str(int(first_number) + int(second_number))
            else:
                answer = str(int(first_number) - int(second_number))
            answers.append(answer.rjust(width))

    # Combine all lines with proper spacing
    arranged_problems = '    '.join(first_line) + '\n' + \
                       '    '.join(second_line) + '\n' + \
                       '    '.join(dashes)
    
    # Add answers if required
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

# Test the function
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
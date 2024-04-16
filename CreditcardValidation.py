import sys

def valid_credit_card(number):
    original_number = number
    if(" " in original_number):
        return "Invalid"
    # Validating initial conditions starting with 4, 5, or 6 and is either 16 digits straight or grouped in 4s separated by hyphens
    if not (original_number.startswith(('4', '5', '6'))):
        return "Invalid"
    
    # Normalize by removing hyphens for digit and sequence checks
    normalized_number = original_number.replace("-", "")
    
    # Check the total digit count after removing hyphens
    if len(normalized_number) != 16 or not normalized_number.isdigit():
        return "Invalid"

    # Ensure correct formatting of hyphens if they are present
    if '-' in original_number:
        parts = original_number.split('-')
        if any(len(part) != 4 for part in parts):
            return "Invalid"
    
    # Check for sequences of four or more identical consecutive digits
    if has_four_consecutive_identical_digits(normalized_number):
        return "Invalid"

    return "Valid"

def has_four_consecutive_identical_digits(number):
    count = 1
    last_char = number[0]
    for char in number[1:]:
        if char == last_char:
            count += 1
            if count == 4:
                return True
        else:
            last_char = char
            count = 1
    return False

def main():
    input_data = sys.stdin.read().strip().split('\n')
    for test_case in input_data[1:]:  # Skip the first line as it's the count of test cases
        print(valid_credit_card(test_case))

if __name__ == "__main__":
    main()
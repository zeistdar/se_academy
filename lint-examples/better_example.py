"""
Code to add two numbers
"""
def add_two_numbers(first_number, second_number):
    """
    Params:
        first_number(int/float): The first number to add
        second_number(int/float): The second number to add
    Returns:
        result(int/float): The added result of two numbers 
    """
    result = first_number + second_number
    return result

if __name__ == "__main__":
    result_sum = add_two_numbers(3, 4)
    
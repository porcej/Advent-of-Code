def load_instructions(file_path):
    """
    Reads a file with two columns of numbers separated by spaces, stores each column in separate lists,
    and sorts them in ascending order.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        tuple: Two sorted lists, one for each column.
    """
    try:
        with open(file_path, 'r') as file:
            instructions = file.read()
        return instructions.strip()

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    instructions = load_instructions('input.txt')
    floor = 0
    for idx, instruction in enumerate(instructions):
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        if floor == -1:
            print(f'Santa entered the basement on instruction {idx+1}')

    print(f'Santa is on floor {floor}.')
def load_list_of_sizes(file_path):
    """
    Reads a file with two columns of numbers separated by spaces, stores each column in separate lists,
    and sorts them in ascending order.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        tuple: Two sorted lists, one for each column.
    """
    packages = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                l, w, h = line.split("x").strip()
                packages.append((l, w, h))
        return packages

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    total_paper = 0
    packages = load_list_of_sizes('input.txt')
    for l, w, h in packages:
        print(f'{l}x{w}x{h}')

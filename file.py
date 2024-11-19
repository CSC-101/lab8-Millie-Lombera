import sys
def main():
        # Check if the command-line argument (filename) is provided
    if len(sys.argv) != 2:
        print("Error: Please provide a filename as a command-line argument.")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                    # Strip any extra whitespace from the line
                line = line.strip()

                    # Attempt to split the line into two values
                parts = line.split()
                if len(parts) != 2:
                    print(f"Error on line {line_num}: Line does not contain exactly two values.")
                    continue

                try:
                        # Convert parts to floats and calculate their sum
                    num1 = float(parts[0])
                    num2 = float(parts[1])
                    print(f"Sum of line {line_num}: {num1 + num2}")
                except ValueError:
                    print(f"Error on line {line_num}: Unable to convert one or both values to float.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be opened.")
        sys.exit(1)

    if __name__ == "__main__":
        main()

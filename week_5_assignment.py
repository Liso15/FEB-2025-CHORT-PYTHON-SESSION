def read_and_modify_file(input_filename, output_filename):
    try:
        # Step 1: Open and read the input file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Step 2: Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Step 3: Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"File '{input_filename}' has been modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")
    
    # Define the output filename
    output_filename = "modified_" + input_filename

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
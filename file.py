def read_and_write_file():
    # Ask the user for the input and output filenames
    input_filename = input("Enter the input file name: ")
    output_filename = input("Enter the output file name: ")

    try:
        # Open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File content has been modified and saved to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read/write the file. Please check the file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_write_file()
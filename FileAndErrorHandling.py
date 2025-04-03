def modify_file():
    """Reads a file and writes a modified version to a new file with user-selected modifications."""
    input_filename = input("Enter the input filename: ").strip()

    try:
        # Open file with UTF-8 encoding to handle special characters
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()

        if not content:
            print("Warning: The file is empty. No modifications made.")
            return

        print("\nChoose a modification:")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Reverse text")
        print("4. Capitalize each word")

        # Capture the user's choice
        choice = input("Enter the number of your choice: ").strip()
        print(f"Debug: User entered choice: {choice}")  # Debugging line

        modifications = {
            '1': content.upper(),
            '2': content.lower(),
            '3': content[::-1],
            '4': content.title()
        }

        # Check if the choice is valid
        modified_content = modifications.get(choice)

        if modified_content is None:
            print("❌ Invalid choice! No modifications applied.")
            return

        # Get the output filename
        output_filename = input("Enter the output filename: ").strip()

        # Write the modified content to the output file with UTF-8 encoding
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_content)

        print(f"\n✅ Content successfully written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied. Cannot read '{input_filename}'.")
    except IOError as e:
        print(f"❌ Error: An I/O error occurred: {e}")
    except UnicodeDecodeError as e:
        print(f"❌ Error: Unable to decode the file. Check if the file contains special characters or use a different encoding. {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def read_and_handle_errors():
    """Reads a user-provided file and displays its contents, handling errors gracefully."""
    filename = input("Enter the filename to read (with path if needed): ").strip()

    try:
        with open(filename, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
            content = file.read()
            print("\n📄 File Content:")
            print(content)

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied. Cannot read '{filename}'.")
    except IOError as e:
        print(f"❌ Error: An I/O error occurred: {e}")
    except UnicodeDecodeError as e:
        print(f"❌ Error: Unable to decode the file. Check if the file contains special characters or use a different encoding. {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def toggle_read_modify():
    """Toggles between reading and modifying a file based on user input."""
    while True:
        print("\n🔄 What would you like to do?")
        print("1. Read a file")
        print("2. Modify a file")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            read_and_handle_errors()
        elif choice == '2':
            modify_file()
        elif choice == '3':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

# Uncomment to run the toggle function
toggle_read_modify()

# File Read & Write Challenge 🖋️

This project is a Python-based file read and write challenge that allows you to read, modify, and write content from one file to another. You can choose from several modification options such as converting text to uppercase, lowercase, reversing the text, or capitalizing each word.

## Features ✨
- Read a file and display its contents.
- Modify the contents of the file with user-selected transformations:
  - Convert text to UPPERCASE
  - Convert text to lowercase
  - Reverse the text
  - Capitalize each word
- Write the modified content to a new output file.
- Error handling for missing files, permission issues, or invalid modifications.

## Installation 🔧

1. Clone this repository:
    ```bash
    git clone https://github.com//KabeloMatlakala/Week-4-File-and-Error-Handling.git
    ```

2. Navigate to the project directory:
   ```bash  
   cd your-repository-name
   ```

3. Make sure you have Python installed. You can check this by running:
   ```bash
   python --version
   ```
    If Python is not installed, download and install it from python.org.

### Usage
#### Running the Program
To run the program, simply execute the script using Python:
  ```bash
  python FileAndErrorHandling.py
  ```
The program will ask you to:

1. Choose between reading or modifying a file:
  * Read a file: Displays the contents of the file.  
  * Modify a file: Allows you to choose a modification option, including:  
    - Convert text to uppercase  
    - Convert text to lowercase  
    - Reverse text
    - Capitalize each word
      
2. Provide the file path (with full path if necessary) for the input and output files.
   #### Example Flow
     ```
       🔄 What would you like to do?
        1. Read a file
        2. Modify a file
        3. Exit
        Enter your choice (1/2/3): 2
        
        Enter the input filename: C:\\Documents\\PLP\\python-week-4\\input.txt
        
        Choose a modification:
        1. Convert to UPPERCASE
        2. Convert to lowercase
        3. Reverse text
        4. Capitalize each word
        Enter the number of your choice: 1
        
        Enter the output filename: output.txt
        
        ✅ Content successfully written to 'output.txt'.
     ```

## Error Handling ⚠️
The program includes error handling to catch:
  * ***FileNotFoundError***: If the input file doesn't exist.
  * ***PermissionError***: If there are permission issues reading or writing the file.
  * ***IOError***: For general I/O problems.
  * ***UnicodeDecodeError***: If the file cannot be decoded (e.g., special characters).
  * ***Invalid Choice***: If an invalid modification option is chosen.


import os
import sys

def search_files(directory, filenames, case_sensitive):
    """
    Recursively search for multiple files in a given directory and its subdirectories.

    Parameters:
    directory (str): The path to the directory where the search will occur.
    filenames (list): A list of filenames to search for.
    case_sensitive (bool): Flag to indicate if the search should be case-sensitive.

    Returns:
    dict: A dictionary with filenames as keys and lists of full paths as values.
    """
    found_files = {filename: [] for filename in filenames}  # Initialize a dictionary to store found files
    try:
        # Walk through the directory tree
        for root, dirs, files in os.walk(directory):
            # Iterate over each file in the current directory
            for file in files:
                # Check each filename in the list
                for filename in filenames:
                    # Check for exact match if case-sensitive
                    if case_sensitive:
                        if file == filename:
                            found_files[filename].append(os.path.join(root, file))
                    else:
                        # Check for match ignoring case
                        if file.lower() == filename.lower():
                            found_files[filename].append(os.path.join(root, file))
    except Exception as e:
        print(f"An error occurred: {e}")

    return found_files

def main():
    """
    Main function to handle command-line arguments and initiate the file search.
    """
    # Check if the necessary arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python file_searcher.py <directory> <filename1> <filename2> ... [case_sensitive]")
        return

    # Extract command-line arguments
    directory_path = sys.argv[1]  # Directory to search in
    # Get the filenames from the command-line arguments
    file_names = sys.argv[2:-1] if len(sys.argv) > 3 else sys.argv[2:]  # All arguments except the first and last
    # Determine if the search should be case-sensitive
    case_sensitive = len(sys.argv) > 3 and sys.argv[-1].lower() == 'true'

    # Call the search_files function and store the result
    results = search_files(directory_path, file_names, case_sensitive)

    # Print the results of the search
    for filename, paths in results.items():
        if paths:
            print(f"File '{filename}' found at:")
            for path in paths:
                print(f" - {path}")
        else:
            print(f"File '{filename}' not found in directory '{directory_path}'.")

if __name__ == "__main__":
    # Execute the main function when the script is run directly
    main()

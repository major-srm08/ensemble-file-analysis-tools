import os
import sys

# Add the app directory to the Python module search path
sys.path.append(os.path.join(os.path.dirname(__file__), "app"))

from plugins.xlsx_plugin import analyze_xlsx  # Importing from the plugins folder

# Define the file path directly in the code
FILE_PATH = "sample.xlsx"

# Main execution function
def main():
    file_path = FILE_PATH

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return

    # Perform analysis using the xlsx plugin
    results = analyze_xlsx(file_path)

    # Print the results
    print("\nAnalysis Results:")
    print("------------------")
    for key, value in results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()



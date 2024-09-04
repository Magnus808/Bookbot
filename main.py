import logging
logging.basicConfig(level=logging.ERROR)

def read_file():
    while True:
        path_to_file = input("Enter the path to the file: ")
	try:
		with open(path_to_file) as f:
			return f.read()
	except FileNotFoundError:
    		print(f"Error: The file {path_to_file} does not exist.")
	except IOError:
    		print(f"Error: Could not read the file {path_to_file}.")
	except Exception as e:
    		print(f"An unexpected error occurred: {e}")
	
#Main execution
file_contents = read_file()
print("File read successfully.")
print(f"File size: {len(file_contents)} bytes")

if __name__ == "__main__":
    main()

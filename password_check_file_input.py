import os
from password_checker import check_password_validity
from circular_queue import CircularQueue

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def main():
    password_input_file = os.path.join("input_files", "passwords.txt")
    password_input = read_input_from_file(password_input_file)
    output = check_password_validity(password_input)
    print("Valid passwords:", output)

if __name__ == "__main__":
    main()

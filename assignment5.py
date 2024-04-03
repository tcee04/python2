def write_to_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("First line\n")
            file.write("Second line\n")
            file.write("Third line\n")
            print("File created and initial content written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while writing to file: {e}")
    finally:
        print("File write operation completed.")


def read_and_display():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of my_file.txt:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading file: {e}")
    finally:
        print("File read operation completed.")


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Fourth line\n")
            file.write("Fifth line\n")
            file.write("Sixth line\n")
            print("Additional content appended successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to file: {e}")
    finally:
        print("File append operation completed.")


if __name__ == "__main__":
    write_to_file()
    read_and_display()
    append_to_file()
    read_and_display()

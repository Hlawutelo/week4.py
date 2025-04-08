def read_and_write_file():
    filename = input("Enter filename: ")

    while True:
        print("\nOptions:")
        print("1. Read")
        print("2. Write")
        print("3. Exit")

        option = input("Choose option: ")

        try:
            if option == "1":
                with open(filename, 'r') as file:
                    print(file.read())
            elif option == "2":
                content = input("Enter content: ")
                with open(filename, 'w') as file:
                    file.write(content)
            elif option == "3":
                break
            else:
                print("Invalid option")
        except FileNotFoundError:
            print(f"File '{filename}' not found")
        except Exception as e:
            print(f"Error: {e}")

read_and_write_file()
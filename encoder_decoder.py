
def encode(password):
    password_encoded = ""
    for i in password:
        encoded_num = str((int(i) + 3) % 10)
        password_encoded += encoded_num
    return password_encoded


def decode(password_encoded):
    password = ""
    for i in password_encoded:
        decoded_num = str((int(i) - 3) % 10)
        password += decoded_num
    return password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option:"))
        if option == 1:
            password = input("Please enter a password to encode:")
            password_encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print("The encoded password is", password_encoded, "and the original password is", password, ".")
        elif option == 3:
            break


if __name__ == "__main__":
    main()


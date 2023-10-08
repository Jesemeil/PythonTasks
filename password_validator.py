def password_validator():
    while True:
        password = input("Enter a valid password: ")
        errors = []

        if len(password) < 8:
            errors.append("Password should have at least 8 characters: ")

        if not any(char.isdigit() for char in password):
            errors.append("Password should have at least one number")

        if not any(char.islower() for char in password):
            errors.append("Password should have at least a lowercase letter")

        if not any(char.isupper() for char in password):
            errors.append("Password should contain at least an uppercase letter ")

        if not errors:
            return password
        else:
            print("Invalid password. The following errors were found;")
            for error in errors:
                print(error)


valid_password = password_validator()
print("Valid password: ", valid_password)

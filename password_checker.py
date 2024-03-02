import re


def check_password_validity(passwords):
    valid_passwords = []
    passwords = passwords.split(',')

    for password in passwords:
        if 6 <= len(password) <= 12:
            if re.search("[a-z]", password) and re.search("[0-9]", password) and re.search("[A-Z]",
                                                                                           password) and re.search(
                    "[$#@]", password):
                valid_passwords.append(password)

    return ','.join(valid_passwords)


input_password = "asqwr1234@1,aF145#,2w3E*,2We3345"
# output = check_password_validity(input_password)
# print("Output =", output)

'''
Homework 5 Part 1 - coding
Maher Harkati
Problem 3 - Password Simulator
'''
import random
import string

class PasswordSimulator:
    def __init__(self):
        self.accepted_passwords = []
        self.rejected_passwords = []
        self.dictionary_list = ['password', 'admin', '123456', 'letmein', 'qwerty']
        self.common_passwords = set(self.dictionary_list)

    def generate_random_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def is_acceptable_password(self, password):
        has_special_symbols = any(char in string.punctuation for char in password)
        is_not_common_password = password.lower() not in self.common_passwords
        return has_special_symbols and is_not_common_password

    def simulate_password_creation(self, iterations=40):
        for _ in range(iterations):
            password = self.generate_random_password()
            if self.is_acceptable_password(password):
                print(f"Accepted Password: {password}")
                self.accepted_passwords.append(password)
            else:
                print(f"Rejected Password: {password}")
                self.rejected_passwords.append(password)

    def display_accepted_passwords(self):
        print("\nAccepted Passwords:")
        for password in self.accepted_passwords:
            print(password)

    def display_rejected_passwords(self):
        print("\nRejected Passwords:")
        for password in self.rejected_passwords:
            print(password)

    def display_common_passwords(self):
        print("\nCommon Passwords:")
        for password in self.common_passwords:
            print(password)

# Example Usage
password_simulator = PasswordSimulator()
password_simulator.simulate_password_creation()

password_simulator.display_accepted_passwords()
password_simulator.display_rejected_passwords()
password_simulator.display_common_passwords()

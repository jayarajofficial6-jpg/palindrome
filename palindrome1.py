# palindrome.py

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

test_string = "madam"  # default for Jenkins

if __name__ == "__main__":
    print(f"Checking: {test_string}")
    if is_palindrome(test_string):
        print("It is a palindrome.")
    else:
        print("It is NOT a palindrome.")
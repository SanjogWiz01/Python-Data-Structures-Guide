import sys

# paidrome.py
# Simple palindrome check for strings

def is_palindrome(s: str) -> bool:
    """
    Return True if s is a palindrome, ignoring case and non-alphanumeric characters.
    """
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":

    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        try:
            text = input("Enter string to check: ")
        except EOFError:
            text = ''

    result = is_palindrome(text)
    print("Palindrome" if result else "Not a palindrome")
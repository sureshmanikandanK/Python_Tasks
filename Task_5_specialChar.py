def speical_char(character):
    if   "a" <= character <= 'z' or "A" <= character <= 'Z' or "0" <= character <= '9':
        return f"{character} you enter character"
    else:
        return f"{character} you enter the special character"

def main():
    print(speical_char(input("Enter the character:")))

if __name__ == "__main__":
    main()
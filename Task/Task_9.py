def main():
    course = ['', 'Python', 'java', ',,', 'angul:ar', 'php']

    filter_list = list(filter(checkAlphabet, course))
    print('Filter List :', filter_list)

def checkAlphabet(check):
    if not check:
        return False
    
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    for checking in check:
        if checking in valid_chars:
            return True
    
    return False

if __name__ == '__main__':
    main()

def main():
    people = [
        {'name': 'shreya', 'age': 16},
        {'name': 'pratiksha', 'age': 33},
        {'name': 'prerna', 'age': 18}
    ]
    
    sorted_dict = sorted(people, key=lambda x: x['age'])
    
    print("Sorted by age:", sorted_dict)

if __name__ == "__main__":
    main()


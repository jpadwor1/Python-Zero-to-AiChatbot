# List to store diary entries
diary_entries = []

while True:
    # Display menu to user
    print("\nSimple Interactive Diary")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Delete Entry")
    print("4. Exit")
    
    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        entry = input("Type your diary entry: ")
        diary_entries.append(entry)
        print("Entry added successfully!")

    elif choice == "2":
        print("\nDiary Entries:")
        for i, entry in enumerate(diary_entries, 1):
            print(f"{i}. {entry}")

    elif choice == "3":
        entry_num = int(input("Enter the entry number to delete: "))
        if 0 < entry_num <= len(diary_entries):
            diary_entries.pop(entry_num - 1)
            print("Entry deleted successfully!")
        else:
            print("Invalid entry number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose a valid option.")

# To - do
todo_list = []

while True:
    print("============Enter your Task==================")
    print("1. Add Notes: ")
    print("2. View Notes: ")
    print("3. Delete Notes: ")
    print("4. Exit: ")

    user_input= input("\nChoose By Number you want to do task?: \n")

    if user_input == '1':
        user_note = input("Enter you task: \n")
        todo_list.append(user_note)
        print('Notes Added successfully By user! \n\n')

    
    elif user_input == '2':
        print('===========Your Notes:==================== \n')
        if not todo_list:
            print('No notes \n\n')
        else:
            for i, value in enumerate(todo_list, start=1):
                todo_list.sort()
                print (f"{i} {value}")
            print('\n\n')
                
    
    elif user_input == '3':
        print("\nYour Tasks: \n")
        for i, task in enumerate(todo_list, start=1):
            todo_list.sort()
            print(f"{i}. {task}")

        index = input("Enter index to delete note: \n")
        index_int = int(index)

        if 1 <= index_int <= len(todo_list):
            deleted = todo_list.pop(index_int - 1)
            print(f"Deleted task: {deleted}\n")    
    
    elif user_input == '4':
        print("Remind me later Byee! \n\n")
        break
    else:
        print('Choose valid number for you task \n\n')
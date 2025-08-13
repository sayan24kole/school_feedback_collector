i = int(input("Enter 1 to enter names and code, 2 to view names and code, 3 to delete all names"))
if i == 1 or i==2 or i==3:
    match i:
        case 1:
            tot_names = int(input("Enter total how many names/code you wanna enter"))
            with open('student_names.txt','a') as f:
                 for x in range(0,tot_names):
                     std_names = input(f'Enter student {x+1} name')
                     std_code = input(f'Enter student {x+1} code id')
                     f.write(f'{std_names},{std_code}\n')
        case 2:
            with open('student_names.txt','r') as f:
                print(f.read())
        case 3:
            with open('student_names.txt','w') as f:
                f.write("")
else:
    print("Use number between 1,2 and 3")
i = int(input("Enter 1 to enter names, 2 to view names, 3 to delete all names"))
if i == 1 or i==2 or i==3:
    match i:
        case 1:
            tot_names = int(input("Enter total how many names you wanna enter"))
            with open('teacher_names.txt','a') as f:
                for x in range(0,tot_names):
                    names = input("Enter names of teachers")
                    f.write(f"{names}\n")
                    k = open(f'{names}_teach.txt','x')
                    k.close()
        case 2:
            with open('teacher_names.txt','r') as f:
                print(f.read())
        case 3:
            with open('teacher_names.txt','w') as f:
                f.write("")
else:

    print("Use number between 1,2,3")

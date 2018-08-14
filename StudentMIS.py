print("1.enter record\n2.read record")
choice=input("choose the option")
with open("test1.txt",'a') as file:
    if choice=='1':
        name=input("enter the name:")
        address=input("enter the address:")
        save=input("do u wanna save?? enter y/n")
        if save=='y':
            file.write("student name: {}\nstudent address: {}\n".format(name,address))
        else:
            print("no info saved")




    elif choice=='2':
        with open("test1.txt",'r') as file:
            print(file.read())
            # print("name:",name)
            # print("address:",address)

    else:
        print("invalid entry")










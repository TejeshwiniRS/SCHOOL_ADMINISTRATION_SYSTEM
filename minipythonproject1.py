import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact No","Email-id"])
        writer.writerow(info_list)
selection=int(input("\nEnter 1 for adding student's info \nEnter 2 for deleting student's info: "))
if (selection == 1):
    x=True
    stu_num=1
    while(x):
        stu_info=input("Enter the information of the student #{} in the following format (Name Age Contact_no email_id) ".format(stu_num))
        stu_info_list=stu_info.split(' ')
        print("\nPlease check the entered info\nName: {}\nAge: {}\n Contact_no:     {}\n email_id: {}\n".format(stu_info_list[0],stu_info_list[1]    ,stu_info_list[2],stu_info_list[3]))
        choice_check=input("Is the entered info correct(yes/no): ")
        if choice_check == "yes":
            write_into_csv(stu_info_list)
            condition_check=input("Enter (yes/no) if you want to enter information     of another student: ")
            if condition_check == "yes":
                x=True
                stu_num=stu_num+1
            elif condition_check == "no":
                x=False
        elif choice_check == "no":
            print("\n Please re-enter the values\n")
elif (selection == 2): 
    lines = list()
    members= input("Please enter the student's name to be deleted.")
    with open('mycsv.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
        for field in row:
            if field == members:
                lines.remove(row)
    with open('mycsv.csv', 'w') as writeFile:
        writere = csv.writer(writeFile)
        writere.writerows(lines)
else:
    print("Enter a valid choice")
     

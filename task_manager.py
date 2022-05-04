#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime
from datetime import date 

#====Login Section====
# Promt user for their useername and password
# Create a count variable 
username_count = 0
username = input("Please Enter Your Username: ")
password = input("Please Enter Your Password: ")
username_list = " "
password_list = " "

# Open file and create a list
# Use try and except so that the indexes stay in range
# Count the iterations for the statistics  
with open("user.txt","r") as user_file:
    for lines in user_file:
        lines = lines.replace(",","") 
        lines = lines.split()
        try:
            username_list += lines[0]
            username_count += 1 
            password_list += lines[1]
        except:
            continue
user_count = username_count            
user_file.close()        

# Use if variable to validate username and password
# Use x and y as control variables to make sure both username and password are validated
x = 0
y = 0
while x == 0 or y == 0:
    if username in username_list:
        print("\nUsername found")
        x = 1
    elif username not in username_list:
        print("Username not found\n")
        username = input("Please Enter Your Username: ")  
    if password in password_list:
        print("Password found\n")
        y = 1
    elif password not in password_list:
        print("Password not found\n")
        password = input("Please Enter Your Password: ")
    else:
        print("Unknown error, Please try again.\n") 
        
# FUNCTIONS
def task_select():
    # Use this function to endit tasks  
    # Use task selector to select a task 
    # Open the file and copy all strings to a list
    # I used an if statment at the instruction of a mentor to get rid of all blank strings because my machine was printing lots of blank stings 
    task_selector = input("Please enter the task number that you would like to select or enter -1 to go back to main menu: ")
    with open("tasks.txt",'r+') as f:
        view_all = f.readlines()
        edit_list = []
        for line in view_all :
            line = line.strip()
            line = line.split(", ")
            if line == ['']:
                continue
            edit_list.append(line)

        # Use -1 to return to menu
        for line2 in edit_list:
            if task_selector == "-1":
               break
            
            # Validate task and username to ensure you don't end up with a duplicate task
            if task_selector == line2[2] and username == line2[1]:
                
            # Print selected task
                try:
                    print("""\n\nTask:\t\t\t{}\nAssigned To:\t\t{}\nTask No:\t\t{}\nDate Assigned:\t\t{}\nDue Date:\t\t{}\nTask Complete:\t\t{}\nTask Description:\n{}\n""".format(line2[0],line2[1],line2[2],line2[3],line2[4],line2[5],line2[6]))
                    # Only allow for editing on uncomplete tasks 
                    if line2[5] == "No":    
                        change = input("Would you like to edit the your task please enter yes or no: ").lower()
                    else:
                        break
                    
                    # If user indicates that they want to edit task let them select editing option from the menu
                    if change == "yes": 
                        task_edit = input("\nPlease enter the word to edit that section of the task: \n1\t\tMark the task as complete\n2\t\tEdit the due date and user in charge of the task\nEnter here: ")
                        
                        # If 1 is selected from menu change task to complete
                        if task_edit =="1":
                            line2[5] = line2[5].replace("No","Yes")
                        
                        # If 2 is selected from menu allow user to edit username and due date of the task
                        if task_edit == "2":
                            new_person = input("Please enter the username of the person you would like to complete this task: ")
                            new_date = input("Please enter a due-date in the format year\mm\dd for this task: ")
                            line2[1] = line2[1].replace(line2[1],new_person)
                            line2[4] = line2[4].replace(line2[4],new_date)
                except:
                    continue
        f.close()

    # Overwrite file with the edited version of the string 
    with open('tasks.txt','w') as f1:
        for line3 in edit_list:
            str_line = f"\n{line3[0]}, {line3[1]}, {line3[2]}, {line3[3]}, {line3[4]}, {line3[5]}, {line3[6]}"
            f1.write(str_line)
def view_all():
    # All commments for this code are found where this function is called.
    counts = 0
    with open("tasks.txt",'r') as view:
        for line in view :
            line = line.strip()
            line = line.split(", ")
            try:
                if len(line) > 1:
                    try:
                        print("""\n\nTask:\t\t\t{}\nAssigned To:\t\t{}\nTask No:\t\t{}\nDate Assigned:\t\t{}\nDue Date:\t\t{}\nTask Complete:\t\t{}\nTask Description:\n{}\n""".format(line[0],line[1],line[2],line[3],line[4],line[5],line[6]))         
                        counts += 1         
                    except:
                        continue
            except:
                print("There are no tasks currently")
    view.close()
def reg_user():
    # All commments for this code are found where this function is called.
            if username in "admin":
                
                with open("user.txt","a+") as userfile_add:
                    new_username = input("Please Enter New Users Username: ")
                    new_password = input("Please Enter New Users Password: ")
                    new_password_check = input("Please re-enter your password: ")
                    
                    with open("user.txt","r") as file:
                        for line in file:
                            line = line.strip()
                            line = line.split(", ")
                            try:
                                while new_username and new_password in line:
                                    print("\nUser already exists")
                                    new_username = input("Please Enter New Users Username: ")
                                    new_password = input("Please Enter New Users Password: ")
                                    new_password_check = input("Please re-enter your password: ")
                                    cont_var = 1
                                else:
                                    cont_var = 0
                            except:
                                continue
                    file.close()

                    if cont_var == 1:
                        print("Cannot log user that already exists\n")
                    elif new_password == new_password_check:
                         userfile_add.write("\n" + new_username + "," + " " + new_password)
                         return"\nNew user entered \n"
                    else:
                        print("\nPasswords are not the same, please try again.\n")
                userfile_add.close()
            else:
                return "You do not have administration permissions"           
def add_tasks():
    # All commments for this code are found where this function is called.
            task_user = input("Please enter the username of the person who needs to complete this task:  ")
            task_title = input("What is the name of this task: ")
            task_number = input("Please enter a task number in conjunction with the tasks on the view all menu: ")
            task_disc = input("Please describe the task: ")
            due_date = input("Please enter the due date in the format of year/mm/dd: ")
            current_date = input("What is todays date in the format of year/mm/dd: ")
            task_finished = "No"
            task_info = task_title + ", " + task_user + ", " + task_number + ", " + current_date + ", " + due_date + ", " + task_finished + ", " + task_disc + ", "

            with open("tasks.txt",'a+') as task_add:
              task_add.write("\n" + task_info)
              task_add.close()
              return """\n\nTask:\t\t\t{}\nAssigned To:\t\t{}\nTask No:\t\t{}\nDate Assigned:\t\t{}\nDue Date:\t\t{}\nTask Complete:\t\t{}\nTask Description:\n{}\n""".format(task_title,task_user,task_number,current_date,due_date,task_finished,task_disc)
def view_mine():
    # All commments for this code are found where this function is called.
    with open("tasks.txt",'r') as view_1:
        counts = 0
        for line in view_1 :
            line = line.strip()
            line = line.split(", ")
            try:
                if username in line:
                    try:
                        counts += 1
                        print("""\n\nTask:\t\t\t{}\nAssigned To:\t\t{}\nTask No:\t\t{}\nDate Assigned:\t\t{}\nDue Date:\t\t{}\nTask Complete:\t\t{}\nTask Description:\n{}\n""".format(line[0],line[1],line[2],line[3],line[4],line[5],line[6]))
                    except:
                        break
            except:
                print("There are no tasks for you") 
    task_select()
    
         

while True:
    #Presenting the menu to the user and display a seperate menu for admin
    if username in "admin":
        menu = input("""\nSelect one of the following Options below:
r -  Registering a user
a -  Adding a task
va - View all tasks
vm - view my task
e -  Exit
gr - Generate Reports
ds -  Display Statistics
\n\nEnter here: """).lower()
    else:
        menu = input("""\nSelect one of the following Options below:
r -  Registering a user
a -  Adding a task
va - View all tasks
vm - view my task
e -  Exit\n\nEnter here: """).lower()

    if menu == 'r':
        pass
        # Promt user for info about the new user that they are logging
        # Validate passwords to make sure they are correct 
        reg_user()
    
    elif menu == 'a':
        pass
        add_tasks()
        # Promt user for info about new task 
        # Write that task to the tasks,txt file 
        
    elif menu == 'va':
        pass
        # Print all the tasks that are logged
        # Use try and except so that the indexes stay in range
        # Create if statement to ensure that the strings have text 
        view_all()
    
    elif menu == 'vm':
        pass
        # Open tasks file and print all the tasks for a particular user 
        # Use try and except so that the indexes stay in range
        # if statement to print only the users tasks 
        view_mine()

    # Closing statement    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    # Use view all in order to iterate through tasks logged
    # Use user_counter variable from the top for user stats  
    elif menu == 'ds':
        count = 0
        with open("tasks.txt",'r+') as view_all_f:
            for line in view_all_f :
                line = line.strip()
                line = line.split(", ")
                if line == ['']:
                    continue
                try:
                    if len(line) > 0:
                        try:
                            count += 1
                        except:
                            continue
                except:
                    continue
        view_all_f.close()
        
        # Use a for loop to iterate through the completed tasks
        count_yes = 0
        with open("tasks.txt",'r+') as view_all_f1:
            for line in view_all_f1:
                line = line.strip()
                line = line.split(", ")
                if line == ['']:
                    continue
                try:
                    if len(line) > 0 and line[5] == "Yes":
                        try:
                            count_yes += 1
                        except:
                            continue
                except:
                    continue
        view_all_f1.close()

        # Subtract the completed tasks from the total task amounts in order to get the incomplete tasks
        incomplete_tasks = count - count_yes

        # Use datetime to find out what the current date is
        # Then loop through the tasks to find out if there are any overdue tasks 
        today = datetime.today().strftime('%Y/%m/%d')
        count_overdue = 0
        with open("tasks.txt",'r+') as view_all_f1:
            for line in view_all_f1:
                line = line.strip()
                line = line.split(", ")
                if line == ['']:
                    continue
                try:
                    if len(line) > 0 and line[5] == "No":
                        dates = line[4]
                        date_check = date(int(dates[0:4]),int(dates[5:7]),int(dates[8:10])).strftime('%Y/%m/%d')
                        if today > date_check:
                            count_overdue += 1 
                        else:
                            continue
                except:
                    continue
        view_all_f1.close()
        
        # Get the percentage of the incomplete tasks and overdue tasks
        incomplete_percent = (incomplete_tasks/count) * 100
        overdue_percent = (count_overdue/count) * 100
        
        # Wtite all the info to tasks_overview.txt
        with open("task_overview.txt","w+") as task_overviewfile:
            task_overviewfile.write("\n" + str(count) + ", " + str(count_yes) + ", " + str(incomplete_tasks) + ", " + str(count_overdue) + ", " + str(incomplete_percent) + ", " + str(overdue_percent) + ", ")
            task_overviewfile.close()

        # Print tasks from tasks_overview.txt
        with open("task_overview.txt","r") as task_overviewread:
            for line_string in task_overviewread:
                line_string = line_string.strip()
                line_string = line_string.split(", ")
                if line_string == '':
                    continue
                if len(line_string) > 1:
                    print('''
                    Total number of tasks currently logged: \t{}
                    Total number of completed tasks: \t\t{}
                    Total number of uncompleted tasks: \t\t{}
                    Total number of overdue tasks: \t\t{}
                    Percentage of tasks that are incomplete: \t{}
                    Percentage of tasks that are overdue: \t{}
                     '''.format(count,count_yes,incomplete_tasks,count_overdue,incomplete_percent,overdue_percent))   

    elif menu == "gr":
        # Used to generate admin reports

        # Used to get count of all the tasks logged
        count = 0
        with open("tasks.txt",'r+') as view_all_f:
            for line in view_all_f :
                line = line.strip()
                line = line.split(", ")
                if line == ['']:
                    continue
                try:
                    if len(line) > 0:
                        try:
                            count += 1
                        except:
                            continue
                except:
                    continue
        view_all_f.close()
        
        # Make a list and apppend all the tasks
        with open("tasks.txt",'r') as f:
            view_all = f.readlines()
            edit_list2 = []
            for linegr in view_all :
                linegr = linegr.strip()
                linegr = linegr.split(", ")
                if linegr == ['']:
                    continue
                edit_list2.append(linegr)
        f.close()
        
        # Make a list andappend the usernames
        with open("user.txt",'r') as f_user:
            view_all = f_user.readlines()
            edit_list3 = []
            for linegr1 in view_all :
                linegr1 = linegr1.strip()
                linegr1 = linegr1.split(", ")
                if linegr1 == ['']:
                    continue
                edit_list3.append(linegr1)
        
        
        # Use a for loop to  loop over the usernames and the tasks
        # Put the iteration variables between the two loops so that you get data for each username
        for user_line in edit_list3:
            print("\n{}".format(user_line[0]))
            user_line_user = user_line[0] 
            user_task_num = 0
            count_yes_user = 0
            count_no_user = 0
            user_count_overdue = 0
            for text_line in edit_list2:
                if user_line_user == text_line[1]:
                    
                    # Counting the amount of tasks per user
                    try:
                        if len(user_line_user) > 0:
                            try:
                                user_task_num += 1
                            except:
                                continue
                    except:
                        continue

                    # Percentage of the total amount of tasks assigned to that user
                    percent_of_tasks_for_user = (user_task_num/count) * 100

                    # Percentage of completed tasks for that user
                    try:
                        if len(text_line) > 0 and text_line[5] == "Yes":
                            try:
                                count_yes_user += 1
                            except:
                                continue
                    except:
                        continue
                    percent_of_completed_tasks = (count_yes_user/user_task_num) * 100

                    # Percentage of tasks that must still be completed
                    try:
                        if len(text_line) > 0 and text_line[5] == "No":
                            try:
                                count_no_user += 1
                            except:
                                continue
                    except:
                        continue

                    # Subtract the amount the user has not completed from their total tasks
                    # Get a percentage
                    percent_complete = user_task_num - count_no_user
                    percentage_of_incomplete_tasks = (percent_complete/user_task_num) * 100

                    # Tasks that are overdue
                    # Use datetime to find overdue tasks
                    today1 = datetime.today().strftime('%Y/%m/%d')
                    try:
                        if len(text_line) > 0 and text_line[5] == "No":
                            dates1 = text_line[4]
                            date_check1 = date(int(dates1[0:4]),int(dates1[5:7]),int(dates1[8:10])).strftime('%Y/%m/%d')
                        if today1 > date_check1:
                            user_count_overdue += 1 
                        else:
                            continue
                    except:
                        continue

                    

 
            # Print all the data for the admin to see
            print("The percent of tasks assigned to the user:   {}%".format(percent_of_tasks_for_user))
            print("The number of tasks each user has:           {}".format(user_task_num))
            print("The percent of tasks that are complete:      {}%".format(percent_of_completed_tasks))
            print("The percent of tasks that are incomplete:    {}%".format(percentage_of_incomplete_tasks))
            print("Tasks of the user that are overdue:          {}".format(user_count_overdue))

            # Write all that data to a file
            with open("user_overview.txt","a+") as user_over:
                user_over.write("The percent of tasks assigned to the user:   {}%\n".format(percent_of_tasks_for_user) +
                "The number of tasks each user has:           {}\n".format(user_task_num) +
                "The percent of tasks that are complete:      {}%\n".format(percent_of_completed_tasks) +
                "The percent of tasks that are incomplete:    {}%\n".format(percentage_of_incomplete_tasks) +
                "Tasks of the user that are overdue:          {}\n\n".format(user_count_overdue))
                



    else:
        print("You have made a wrong choice, Please Try again")

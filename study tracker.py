
#Study Tracker Project
print("Welcome To Study Tracker !!")

study_data = {}
while True:
    print("1.enter your study session")
    print("2.View Report")
    print("3.EXIT")

    choice=input("enter your choice between 1 to 3:")

    if choice == "1":
       subject = input("enter the subject:")
       hours = int(input("study hours:"))
       if subject in study_data:
           print("You already studied this subject,updating hours")
           study_data[subject]=study_data[subject] + hours
       else:
           study_data[subject] = hours 
       print("your study session recorded")

    elif choice == "2":
        print("your study report :")
        for subject in study_data:
            print(subject, ":" , study_data[subject] , "hours" )

    elif choice ==  "3":
        print("Thankyou for using study tracker")
        break

    else:
        print("invalid choice")
         
    

    

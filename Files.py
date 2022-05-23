more_files = 'Y'
print("This program will create a file as the name you want it with comma seperated information at the location specified.")
#while loop to create multiple files
while more_files == 'Y':
    #get desired information
    name = input("Enter your name  ")
    address = input("Enter your address  ")
    phone_number = input("Enter your phone number. ")
    file_path = input("Enter the File path to the file."  r" EG: C:\Users\john\university  ")
    file_name = input("Enter desired filename with extension.  EG: name.txt ")
    #open file as write to create the file and write the file contents as comma seperated.

    with open(file_path + "/" + file_name, 'w') as f:
        file_contents = name + ", " + address + ", " + phone_number
        f.write(file_contents)

#Reopen file as readable and print contents.
    with open(file_path + "/" + file_name, 'r+') as r:
        print("Youre file reads:")
        print(r.read())
    print("Would you like to create another file? y/n")
    more_files = input().upper()
    
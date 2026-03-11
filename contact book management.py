#contact boook
''' 
add contact
view contact
search contact
delete contact
edit  contact  
exit contact book '''


contact={}
def add_contact():
#loop for taking input to add contacts 
    while True:
        confirm=input("  do you want to add contact (yes/no) ")
        if confirm.isalpha():  #error handeling for name
            if confirm and confirm.lower()== 'yes':
                name=input(" Please Enter the good  name ")
                if name.isalpha():    
                    number=input("Please enter the number ")
                    if  number.isdigit():   # error handeling for number 
                        for num in contact:
                            if contact[num] == number:
                                print(" number already exist ")
                                return 
                        
                        contact[name]=number
                        print(" numbber added successfully ")
                    else:
                        print(" please input a integer value  ")
                else:
                    print(" enter the correct input ")
            else: 
                print("thanks to visit \n ")
                break
        else:
            print(" invalid input ! please enter a string")
print(contact) 

def  search_contact():  
        # taking input of name to search in contact list 
        name=input(" name of the person  to search the contact number ") .lower()
        if name.isalpha():    #error handleing for name 
            if name in contact :
                print("name found ")
                print(" the contact number is ", contact[name],'\n')
            else:
                print(" name not found ")
                
        else:
            print(" please enter string value ")

def view_contact():
    print(" please wait SHOWING CONTACTS  ")
    #loop for accessing name and number 
    for name,number in contact.items():
        print( name ,":" , number ,'\n')


def delete_contact():
    #taking name as input to delete contact
    name=input(" enter name to delete the contact number ")
    if name.isalpha(): # error handleing for name 
        if name in contact:
            print(" name found ")
            #deleteing contact 
            del contact[name]
            print("deleted successfully ")
        else:
            print("name not found")
        print( contact )
    else:
        print(" please enter string value ")

def edit_contact():
    #asking to edit name or number 
    what_to_edit=input(" what you want to edit (name/number)").lower()
    #for name 
    if what_to_edit == 'name':
        name=input("enter name to  edit ") # previous name stored in contact book 
        if name.isalpha():  #error handleing 
            if name in contact :
                new_name=input(" enter the new name   ")  # changing name from previous to new 
                if new_name.isalpha():  # error handeling for new name 
                    number= contact[name]
                    del contact[name]  #deleting old name to save new name 
                    contact[new_name]=number
                    print(" name edited successfully")
                else:
                    print(" invalid input")
            else:
                print(" name not found ")
        else:
            print(" please enter thee string value  ")
    # for number 
    elif what_to_edit=='number':
        name=input(" name to edit the nummber ") # name shose contact number  is to edited 
        if  name in contact:
                new_num=input(" enter the new num  ")
                if new_num.isdigit():
                    contact[name]=new_num  #saving new number 
                    print(" edited successfully")
                else:
                    print("please enter the integer value ")
        else:
            print(" name not found  ")

def  display():
    while True:
        print("=== wELL - COME === \n TO THE CONTACT BOOK ")
        try:
            task=int(input(" enter task to perform \n 0--> break \n 1--> add contact \n 2--> view contact \n 3-->search contact \n 4-->delete contact \n 5--> edit contact \n "))
            if task == 0:
                print (" thanks  to  use  CONTACT BOOK")
                break
            elif task and  task==1:
                add_contact()
            elif task and task == 2:
                view_contact()
            elif task and  task == 3:
                search_contact()
            elif task and  task== 4:
                delete_contact()
            elif task and  task== 5:
                edit_contact()
            else:
                print(" enter valid input ")
        except ValueError:
            print(" input value must be integer ")
display()

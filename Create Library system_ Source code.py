###
#imports
import random



#Class Books
class Books():
    #Constructor init
    def __init__(self):
        self.Title=""
        self.Author=""
        self.Author_First=""
        self.Author_Last=""
        self.Year=0
        self.Publisher=""
        self.ID=""
        self.Title_ID=""
        self.random_num=0
        self.restart_year=0
        self.List_values=[]
        self.Publish_date=date()    #Composition
        self.Number_copies=copies() #Composition


    #Methods
    #Title
    def set_Title (self):
        self.Title=input("Enter the name of the book: ").upper()

    def set_Author (self):
        self.Author_First=input("Enter Author's first name: ").upper()
        self.Author_Last=input("Enter Author's last name: ").upper()
        self.Author=self.Author_First+" "+self.Author_Last

    def set_year(self):
        #verify if the year is correct
        self.restart_year=0
        try:
            self.Year=int(input("Enter the Book's year: "))
        except:
            print("Inavlid year")
            self.restart_year=1
        #verify year
        self.restart_book()

    def set_publisher(self):
        self.Publisher=input("Enter the Book's publisher: ").upper()
        self.Publish_date.set_publish_date()
        #Loop date
        self.restart_book()

    def set_ID(self):
        self.random_num=str(random.randint(100,999))
        self.Title_ID= self.Title[:2]
        self.ID=self.random_num+"_"+self.Title_ID+"_"+self.Author_Last

    def get_Total_copies(self):
        self.Number_copies.set_total()
        #loop number of copies
        self.restart_book()
#modify
        self.Number_copies.set_lent()

    def get_list(self):
        self.List_values=[self.Title,self.Author,self.Year,self.ID,
                          self.Publisher,self.Publish_date.full_date,self.Number_copies.Total_copies,
                          self.Number_copies.Copies_availables]

    def get_book(self):
        print("Book's name: ",self.Title)
        print("Author: ",self.Author)
        print("Year: ", self.Year)
        print("ID: ",self.ID)
        print("Publisher: ",self.Publisher)
        self.Publish_date.get_publish_date()
        self.Number_copies.set_availables()
        self.Number_copies.get_copies()

    def restart_book(self):
        #loop date
        while self.Publish_date.restart==1:
            self.Publish_date.set_publish_date()

        #loop year
        while self.restart_year==1:
            self.set_year()

        #loop set total of copy
        while self.Number_copies.Restart_copy==1:
            self.Number_copies.set_total()
        

        
            
        
        
        
    
        
        
        
        

#Class publish date (Composition of Books)
class date():
    def __init__(self):
        self.day=0
        self.month=0
        self.year=0
        self.restart=0
        self.full_date=""
            

    def set_publish_date(self):
        self.restart=0
        print("Set publish date")
        #verify that date is correct
        try:    
            self.day=int(input("Enter Day in DD format: "))
            self.month=int(input("Enter Month in MM format: "))
            self.year=int(input("Enter Year in YYYY format: "))
            self.full_date="{0} / {1} / {2}".format(self.day,self.month,self.year)
        except:
            print("Inavlid date")
            self.restart=1

    def get_publish_date(self):
        #change to string all value
        print("Publish date: {0} / {1} / {2}".format(self.day,self.month,self.year))



        

#Class number of Book copies
class copies():
    def __init__(self):
        self.Total_copies=0
        self.Copies_availables=0
        self.Copies_lent=0
        self.Restart_copy=0

    def set_total(self):
        #verify nu,ber of copy
        self.Restart_copy=0
        try:
            self.Total_copies=int(input("Enter the number total of copies: "))
        except:
            print("Invalid number of copies")
            self.Restart_copy=1
        
#####verify this method
    def set_lent(self):
        self.Copies_lent=int(input("Enter number of loans: "))

    def set_availables(self):
        self.Copies_availables=self.Total_copies - self.Copies_lent

    def get_copies(self):
        print("Total of copies: ", self.Total_copies)
        print("Copies availables: ",self.Copies_availables)






#Class Book List
class BookList():
    Dict_title={}
    Search_book=""

    def __init__(self, other): #add aggregation with other 
        self.Dict_data={}
        self.Remove_book=""
        self.Status_remove=""
        self.book_saved=""
        self.book_found=0
        self.ListKey=["Book's name","Author","Year","ID","Publisher",
                      "Publish date","Total of copies","Copies availables"]
        self.List=other

    def get_data(self):
        self.List.get_list()
        self.Dict_data=dict(zip(self.ListKey,self.List.List_values))
        #print(self.Dict_data)           

    def get_data_title(self):
        self.Dict_title[self.Dict_data["Book's name"]]=self.Dict_data
        print(self.Dict_title)

    def get_book(self):
        self.Search_book=input("Enter title, author, publisher or date to find the book: ").upper()
        #search for the book in the dictionary list
        for p_id, p_info in self.Dict_title.items():
            
            for key in p_info:
                if self.Search_book==p_info[key]:
                    self.book_saved=p_id
                    self.book_found=1
                    print("Book found: ", p_id)
                    print(self.Dict_title[p_id])
            if self.book_found==0:
                print("Book no found")


    def remove_book(self):
        self.Remove_book=input("Enter the correct title: ").upper()
        self.Status_remove=self.Dict_title.pop(self.Remove_book, None)
        if self.Status_remove!=None:
            print(self.Remove_book, "is deleted")
        else:
            print(self.Remove_book, "was not found")
        print(self.Dict_title)

    def Total_List_Book(self):
        print("Total of books in Book list: ",len(self.Dict_title))











#class users (all users page)
class users():
    
    def __init__(self):
        self.username=""
        self.firstname=""
        self.surname=""
        self.email=""
        self.List_user_values=[]
        self.date_of_birth= user_date_of_birth()    #composition date of birth
        self.address=user_address()                 #composition address

    def set_user_name(self):
        self.username=input("Enter your user name: ").upper()

    def set_first_name(self):
        self.firstname=input("Enter your first name: ").upper()

    def set_surname(self):
        self.surname=input("Enter your surname: ").upper()

    def set_email(self):
        self.email=input("Enter your email address: ").upper()

    def set_user_info(self):
        print("Date of birth")
        self.date_of_birth.dof()
        #loop date of birth
        self.restart_user()
        print("Address information")
        self.address.set_house_num()
        #loop house number 
        self.restart_user()
        self.address.set_street_name()
        self.address.set_postcode()

    def new_first_name(self):
        self.firstname=input("Re-Enter first name: ").upper()

    def new_surname(self):
        self.surname=input("Re-Enter surname: ").upper()

    def new_email(self):
        self.email=input("Re-Enter email address: ").upper()

    def new_date_birth(self):
        print("Re-Ente Date of birth")
        self.date_of_birth.dof()

    def get_user_list(self):
        self.List_user_values=[self.username,self.firstname,self.surname,self.email,
                               self.date_of_birth.full_date,self.address.house_number,
                               self.address.street_name,self.address.postcode]
                               
        

    def get_user_info(self):
        print("User name: ", self.username)
        print("Full name: ", self.firstname+" "+self.surname)
        print("Emai address: ",self.email)
        self.date_of_birth.get_dof()
        self.address.get_address()
        

    def restart_user(self):
        #loop house number
        while self.address.restart_house_number==1:
            self.address.set_house_num()

        #loop date of birth
        while self.date_of_birth.restart_birth_date==1:
            self.date_of_birth.dof()
            
        
            
        

    

        

#user: class address
class user_address():
    
    def __init__(self):
        self.house_number=0
        self.street_name=""
        self.postcode=""
        self.restart_house_number=0

    def set_house_num(self):
        #verify house number
        self.restart_house_number=0
        try:
            self.house_number=int(input("Enter your house number: "))
        except:
            print("Invalid house number")
            self.restart_house_number=1

    def set_street_name(self):
        self.street_name=input("Enter your street name: ").upper()

    def set_postcode(self):
        self.postcode=input("Enter your postcode: ").upper()

    def get_address(self):
        print("House number: ",self.house_number)
        print("Street name: ",self.street_name)
        print("Postcode: ",self.postcode)



        

#user: class date of birth
class user_date_of_birth():

    def __init__(self):
        self.day=0
        self.month=0
        self.year=0
        self.full_date=""
        self.restart_birth_date=0
        
    #date of birth (dof)
    def dof(self):
        #verify date of birth
        self.restart_birth_date=0
        try:
            self.day=int(input("Enter Day in DD format: "))
            self.month=int(input("Enter Month in MM format: "))
            self.year=int(input("Enter Year in YYYY format: "))
            self.full_date="{0} / {1} / {2}".format(self.day,self.month,self.year)
        except:
            print("Invalid date of birth")
            self.restart_birth_date=1

    def get_dof (self):
        #change to string all value
        print("Date of birth: {0} / {1} / {2}".format(self.day,self.month,self.year))
        





#class list user
class ListUsers():
    Dict_username={}
    Search_user=""

    def __init__(self, other): #add aggregation with other
        self.Remove_user=""
        self.Dict_data_users={}
        self.Dict_loan_user={}
        self.user_found=0
        self.remove_user=""
        self.ready_to_remove=""
        self.count_remove=0
        self.removed_value=""
        self.remove_username=""
        self.count_user_remove=0
        self.Remove_user=""
        self.save_remove_key=[]
        self.ListKey_users=["User name","First name","Surname", "Emai address",
                      "Date of birth", "House number", "Street name",
                      "Postcode"]
        self.List_users=other

    #Add user to the list every time that the user is done
    def get_user_data(self):
        self.List_users.get_user_list()
        self.Dict_data_users=dict(zip(self.ListKey_users,self.List_users.List_user_values))
        #print(self.Dict_data_users)

        
    #Add user to the new dictionary
    def get_data_username(self):
        self.Dict_username[self.Dict_data_users["User name"]]=self.Dict_data_users
        print(self.Dict_username)

    def get_user(self):
        self.user_found=0
        if len(self.Dict_username)==0:
            print("No user name, empty list")
        else:
            self.Search_user=input("Enter your user name: ").upper()
            #search for the user name in the dictionary list
            for i in self.Dict_username.keys():
                if self.Search_user==i:
                    print(self.Dict_username[i])
                    self.Dict_loan_user=self.Dict_username[i]
                    self.user_found=1
            if self.user_found==0:
                print("User no found, try again ")
      #  return self.user_found()

    def get_user_to_remove(self):
        self.save_remove_key=[]
        self.remove_user=input("Enter the first name of the user to remove").upper()
        #search for the user first name
        for p_user, p_info_user in self.Dict_username.items():
            for user_key in p_info_user:
                if user_key=="First name" and self.remove_user==p_info_user[user_key]:
                    print("User found", p_user)
                    self.save_remove_key.append(p_user)
                    

    def get_number_user_remove(self):            
        #verify if a user was found to remove
        if len(self.save_remove_key)==0:
            print("User no found ")
            self.count_remove=1
        elif len(self.save_remove_key)==1:
            print("User to remove:", self.save_remove_key)
            self.count_remove=2            
        else:
            print("More than one user with the same first name, verify by user name")
            print(self.save_remove_key)
            self.count_remove=3
        return self.count_remove


    def remove_user_one_key(self):
        #verify the number of users and remove
        if self.count_remove==2:
            self.ready_to_remove=input("Do you want to remove user").upper()
            if self.ready_to_remove=="YES":
                self.removed_value=self.Dict_username.pop(self.save_remove_key[0], None)
                if self.removed_value!=None:
                    print("User has been removed from first name")
                    print(self.Dict_username)
                else:
                    print("No user has been removed from list from first name")
            else:
                print("No user has been removed from first name")

    def remove_user_more_key(self):
        #More than one user to remove
        if self.count_remove==3:
            self.ready_to_remove=input("Do you want to remove user").upper()
            if self.ready_to_remove=="YES":
                self.remove_username=input("Enter the username to remove from list: ").upper()
                for k in self.Dict_username.keys():
                    if self.remove_username==k:
                        self.count_user_remove=1

                self.remove_username_form_list()
            else:
                print("User no found, try again ")


    def remove_username_form_list(self):
        if self.count_user_remove==1:
            self.removed_value=self.Dict_username.pop(self.remove_username, None)
            if self.removed_value!=None:
                print("User has been removed from username")
                print(self.Dict_username)
            else:
                print("No user has been removed from list from username")
        else:
            print("User no found, verify, and try again")
        
        

                

    def remove_user_none(self):
        #None user to remove
        if self.count_remove==1:
            print("Try again")
                            
                

    def Total_List_User(self):
        print("Total of users: ", len(self.Dict_username))
        
        
    def get_user_from_List(self):
        if self.user_found==1:
            #Verify if they want to remove user
            while self.Remove_user!="YES":
                self.Remove_user=input("Do you want to remove user? ").upper()
                if self.Remove_user=="YES":
                    self.get_user_to_remove()
                    self.get_number_user_remove()
                    if self.count_remove==1:
                        self.remove_user_none()
                        self.Remove_user=""

                    elif self.count_remove==2:
                        self.remove_user_one_key()
                        self.Remove_user=""

                    elif self.count_remove==3:
                        self.remove_user_more_key()
                        self.Remove_user=""

                    else:
                        print("Try again, command no found")
                        self.Remove_user=""
                else:
                    break


    
#Class loan books
class loans():

    def __init__(self, other, user_other):
        self.user_to_borrow=""
        self.book_assign=""
        self.books_loans={}
        self.book_loan_user={}
        self.dict_count={}
        self.unassign_book=""
        self.Status_remove_book=""
        self.save_remove=""
        self.find_book=other
        self.find_user=user_other

        

    #find the book and return the name
    def set_book_borrow(self):
        self.find_book.get_book()
        print("check", self.find_book.book_saved)

    #find user
    def set_books_loans(self):
        self.find_user.get_user()
        if self.find_user.user_found==1:
            self.books_loans[self.find_book.book_saved]=self.find_book.book_saved
            print(self.books_loans)
            
    #new dictionary with loans
    def get_username_loans(self):
        print(self.find_user.Search_user)
        self.book_loan_user=dict(list(self.find_user.Dict_loan_user.items())+list(self.books_loans.items()))
        print(self.book_loan_user)
        print()


    def re_write_dictionary(self):
        if len(self.find_user.Dict_username)>0:
            self.find_user.Dict_username[self.book_loan_user["User name"]]=self.book_loan_user
            print(self.find_user.Dict_username)
        else:
            print("Empty List")
        


    def un_assign_book(self):
        self.unassign_book=input("Enter the correct title to return: ").upper()                  


    def remove_book_from_user(self):
        if len(self.find_user.Dict_username)>0:
            self.Status_remove_book=self.find_user.Dict_username[self.find_user.Search_user].pop(self.unassign_book, None)
            if self.Status_remove_book!=None:
                print(self.unassign_book, "is deleted from user")
            else:
                print(self.unassign_book, "was not found from user")
            print(self.find_user.Dict_username)
        else:
            print("Empty List")
        



    def count_loan_books(self):
        if len(self.find_user.Dict_username)>0 and self.find_user.user_found==1:
            self.dict_count=self.find_user.Dict_username.copy()
            del self.dict_count[self.find_user.Search_user]['User name']
            del self.dict_count[self.find_user.Search_user]['Postcode']
            del self.dict_count[self.find_user.Search_user]['Street name']
            del self.dict_count[self.find_user.Search_user]['Date of birth']
            del self.dict_count[self.find_user.Search_user]['First name']
            del self.dict_count[self.find_user.Search_user]['Surname']
            del self.dict_count[self.find_user.Search_user]['Emai address']
            del self.dict_count[self.find_user.Search_user]['House number']
            print("Verify loans of books")
            print(self.dict_count[self.find_user.Search_user])
            print("Loans by: ", self.find_user.Search_user, "=", len(self.dict_count[self.find_user.Search_user]))
        
        else:
            print("Empty List")
            



#All functions

def Books_1():
    #variables 1. Books
    stop=""

#make a loop
    while stop!="YES":
        
        #Call classes
        Lib_book.set_Title()
        Lib_book.set_Author()
        Lib_book.set_year()                           
        Lib_book.set_publisher()       
        Lib_book.set_ID()                            
        Lib_book.get_Total_copies()
        Lib_book.get_book()

        #call class as agregation
        #Book List
        ListB.get_data()
        ListB.get_data_title()

        #finish the loop
        stop=input("Do you want to stop adding? ").upper()





def Books_List_2():
    search=input("Do you want to search a book? ").upper()
    if search=="YES":
        ListB.get_book()


    remove_book=input("Do you want to remove a book? ").upper()
    if remove_book=="YES":
        ListB.remove_book()

    ListB.Total_List_Book()
    



def User_3():
    #variables 3. Users
    correct_user=""
    sign_in=""
    correct=""
    Start_sign_in=""
    
    
    #Get user data
    #Start the loop to sign in
    while Start_sign_in!="NO":                                                           
        sign_in=input("Do you want to sign in? ").upper()
        if sign_in=="YES":
            user_sign.set_user_name()
            user_sign.set_first_name()
            user_sign.set_surname()
            user_sign.set_email()
            user_sign.set_user_info()
            user_sign.get_user_info()
            #Loop edit user data
            while correct_user!="YES":
                print("check")
                #Edit users
                correct_user=input("Do you want to edit user? ").upper()
                if correct_user=="YES":
                    print("Please select the option to edit form 1 to 4")
                    correct=input("1 First name, 2 Surname, 3 email, 4 date of birth: ")
                    correct_user=""
                    if correct=="1":
                        user_sign.new_first_name()
                        continue
                    elif correct=="2":
                        user_sign.new_surname()
                        continue
                    elif correct=="3":
                        user_sign.new_email()
                        continue
                    elif correct=="4":
                        user_sign.new_date_birth()
                        continue
                    else:
                        print("Sellection no valid, try again")
                        continue
                elif correct_user=="NO":
                    break
                else:
                    print("Sellection no valid, try again")
                    continue
            
        
            #Print user sign in
            user_sign.get_user_info()
            #Add user into the list users    
            ListU.get_user_data()
            ListU.get_data_username()
        #Ask if someone else want to sign in
        Start_sign_in=input("Does someone else want to sign in? ").upper()








def UserList_4():
    #variables 4. User List
    log_in=""
    finish_log_in=""
    
    #Verify if the user name is in the list
    while finish_log_in!="YES":
        log_in=input("Do you want to log in? ").upper()
        if log_in=="YES":
            ListU.get_user()
            ListU.get_user_from_List()
        else:
            finish_log_in=input("Do you want to log out? ").upper()
        



    #Total of user in the list users
    ListU.Total_List_User()






def Loans_5():
    #variables 5. Loans
    stop_loan=""
    start_loan=""
    return_book=""
    #Get the book name from the list
    while stop_loan!="YES":
        start_loan=input("Do you want to borrow a book? ").upper()
        if start_loan=="YES":
            loan_book.set_book_borrow()
            #Get the user name
            loan_book.set_books_loans()
            loan_book.get_username_loans()
            loan_book.re_write_dictionary()
        elif start_loan=="NO":
            return_book=input("Do you want to return a book? ").upper()
            if return_book=="YES":
                loan_book.set_books_loans()
                loan_book.un_assign_book()
                loan_book.remove_book_from_user()
            
            else:
                stop_loan=input("Do you want to finish transaction? ").upper()
        else:
            stop_loan=input("Do you want to finish transaction? ").upper()
    #number of books loan
    loan_book.set_books_loans()
    loan_book.count_loan_books()













        
        
#variables for select option
Stop_selection=""
Option_selected=""

#call classes

Lib_book=Books()
ListB=BookList(Lib_book)
user_sign=users()
ListU=ListUsers(user_sign)
loan_book=loans(ListB,ListU)



#Select option
while Stop_selection!="YES":
    #verify correct option selection
    try:
        Option_selected=int(input("Select number of the option that you want to do, 1. Books, 2.BookList, 3. Users, 4.UserLists, 5. Loans "))
    except:
        print("Selection no valid, try again")
        print()
        continue
    
    #Select Books(1)
    if  Option_selected==1:
        Books_1()
       

    #Select Book List(2)
    elif Option_selected==2:
        Books_List_2()
        

    #Select User(3)
    if Option_selected==3:
        User_3()



    #Select User List(4)
    elif Option_selected==4:
        UserList_4()



    #Select Loan(5)
    elif Option_selected==5:
        Loans_5()



    elif Option_selected==0 or Option_selected>5:
        print("Number no valid")

    
    #Stop principal loop.
    Stop_selection=input("Do you want to stop monitoring? ").upper()
    

        
        
    
                          


















                             



   







        
    

    

    

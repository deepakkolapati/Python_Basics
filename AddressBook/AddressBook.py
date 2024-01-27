'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-27 11:25:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-27 11:25:30

@Title : AddressBook Problem
'''

from logger import get_logger

log = get_logger()


class Contact:
   def __init__(self,fname,lname, address,city, state, zip, phno,email):
        self.fname=fname
        self.lname=lname
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.phno=phno
        self.email=email

   def __repr__(self) -> str:
      return f'{self.fname}'
   
    
class AddressBook:

   def __init__(self, name):
        self.book_name = name
      #   self.contact_names=[]
        self.contacts={}
       

   def add_contact(self,contact):
        if contact.fname not in self.contacts:
          self.contacts[contact.fname]=contact
         #  self.contact_names.append(contact.fname)
      
        else:
            print("The Contact already exists")

   def add_contacts(self):
       
       while True:
            option=int(input("Enter 1 to add new contact, 2 to break: "))
            if option==1:
                fname=input("Enter the persons fname: ")
                lname=input("Enter the persons lname: ")
                address=input("Enter the persons address: ")
                city=input("Enter the persons city: ")
                state=input("Enter the persons state: ")
                zip=input("Enter the persons zip: ")
                phno=input("Enter the persons phno: ")
                email=input("Enter the persons email: ")
                contact=Contact(fname,lname,address,city,state,zip,phno,email)
                self.add_contact(contact)
            else:
               break
        
   def delete_contact(self,fname):
        if fname in self.contacts:
            self.contacts.pop(fname)
        else:
            print("The Contact doesn't exist")
    
   def get_contact(self,fname):
       if fname in self.contacts:
          contact=self.contacts[fname]
          print(f''' 
                     fname:{contact.fname}
                     lname:{contact.lname}
                     address:{contact.address}
                     city:{contact.city}
                     state:{contact.state}
                     zip:{contact.zip}
                     phno:{contact.phno}
                     email:{contact.email}
                
               ''')
         #  print(f'{contact.fname}\t')
       else:
          print("The Person doesn't exist")
    
   def edit_contact(self,fname):
        if fname in self.contacts:

            contact=self.contacts[fname]

            while True:
                edit=int(input("Enter 1 to change address, 2 to change city, 3 to change zip, 4 to change phno, 5 to change email: "))
                
                if edit ==1:
                  new_address=input("Enter the new address: ")
                  contact.address=new_address

                elif edit==2:
                  new_city=input("Enter the new city: ")
                  contact.city=new_city
                

                elif edit==3:
                  new_zip=input("Enter the new zip: ")
                  contact.zip=new_zip

                elif edit==4:
                  new_phno=input("Enter the new phno: ")
                  contact.phno=new_phno

                elif edit==5:
                  new_state=input("Enter the new state: ")
                  contact.state=new_state
                 

                else:
                   break

        else:
           print("The contact doesn't exist ")

   def contact_by_city_or_state(self, city_or_state):
      contacts = list(filter(lambda contact: city_or_state in [contact.city, contact.state], self.contacts.values()))
      print(contacts)


class MultiAddressBook:
    def __init__(self):
       self.books_dict={}


    def get_book(self, book_name):
       return self.books_dict.get(book_name)
    
    def add_addressbook(self,addressbook):
        if addressbook.book_name in self.books_dict:
          print("The Address Book already exists")
        else:
          self.books_dict[addressbook.book_name]=addressbook
        

    def delete_addressbook(self,name):
       if name in self.MultiAddressBook:
          del self.MultiAddressBook[name]

    def get_contacts_by_city_or_state(self, city_or_state):
      list(map(lambda book: book.contact_by_city_or_state(city_or_state), self.books_dict.values()))
         
      
def get_book_obj():
   book_name = input('Enter book name: ')
   book = books.get_book(book_name)
   if not book:
      book = AddressBook(book_name)
   return book
      
       


if __name__=="__main__":
   books =  MultiAddressBook()
   while True:
        
        choice = int(input("Enter 1 for add contacts, 2 for edit contact,3 for get contacts,4 for get contacts by cityorstate,5 for delete contacts: "))
        if choice == 1:
            book = get_book_obj()
            books.add_addressbook(book)
            book.add_contacts()

        elif choice==2:
           book = get_book_obj()
           name=input("Enter the name of the Person: ")
           book.edit_contact(name)
        elif choice==3:
           book = get_book_obj()
           name=input("Enter the name of the Person: ")
           book.get_contact(name)
         
        elif choice==4:
           city_or_state=input("Enter the city or state: ")
           books.get_contacts_by_city_or_state(city_or_state)
           
        elif choice==5:
           book = get_book_obj()
           name=input("Enter the name of the Person: ")
           book.delete_contact(name)
        else:
           break
   
   # dict1 = {'deepak': Contact('deepak', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd'),
   #          'joshi': Contact('joshi', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd'),
   #          'abhi:': Contact('abhi', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd')}
   
   # print(dict1.items())
   # sorted_dict = dict(sorted(dict1.items(), key=lambda x:x[1].fname))
      
   # print(sorted_dict)
     
    
        
                

                
                
                   


    

import pickle

class books(object):
    booksm=[]
    def __init__(self,name1,auth,cop):
        self.name=name1
        self.author=auth
        self.copies=cop
        self.isnam=[]
        j=self.name+".dat"
        file1=open(j,"wb")
        pickle.dump(self,file1)
        file1.close()
        books.booksm.append(self.name)
    def issbook(self,name2):
        self.isnam.append(name2)
        self.copies=self.copies-1
        j=self.name+".dat"
        file1=open(j,"wb")
        pickle.dump(self,file1)
        file1.close()
    def retbook(self,name3):
        self.isnam.remove(name3)
        self.copies=self.copies+1
        j=self.name+".dat"
        file1=open(j,"wb")
        pickle.dump(self,file1)
        file1.close()

class members(object):
    membersm=[]
    def __init__(self,name1):
        self.name=name1
        self.issue=""
        self.issd=0
        j=self.name+".dat"
        file1=open(j,"wb")
        pickle.dump(self,file1)
        file1.close()
        members.membersm.append(self.name)
    def issbook(self,name2):
        self.issue=name2
        self.issd=count
        j=self.name+".dat"
        file1=open(j,'wb')
        pickle.dump(self,file1)
        file1.close()
    def retbook(self):
        self.issue=""
        self.issd=0
        j=self.name+".dat"
        file1=open(j,"wb")
        pickle.dump(self,file1)
        file1.close()

def showbooks():
    print "BOOKS AVAILABLE RIGHT NOW"
    print
    print "NAME"," "*20,"AUTHOR"," "*20,"COPIES"
    print
    print
    

    for i in books.booksm:
         j=i+".dat"
         file1=open(j,"rb")
         book1=pickle.load(file1)
        
        
        
         if book1.copies!=0:
             a,b=26-len(book1.name),28-len(book1.author)
             print i,"_"*a,book1.author,"_"*b,book1.copies
            
            
         file1.close()

    print
    print
    print "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    print "BOOKS UNAVAILABLE RIGHT NOW"
    print
    print "NAME"," "*20,"AUTHOR"," "*20,"COPIES"
    print

    for i in books.booksm:
         j=i+".dat"
         file1=open(j,"rb")
         book1=pickle.load(file1)
        
        
        
         if book1.copies==0:
             a,b=26-len(book1.name),28-len(book1.author)
             print i,"_"*a,book1.author,"_"*b,book1.copies
         file1.close()


    return
    

def librcreator1():
    n1=int(raw_input("How many books would you like the library to have?"))
    print
    for i in range(0,n1):
        bn=raw_input("Please enter the name of the book")
        an=raw_input("Please enter the name of the author")
        cn=int(raw_input("How many copies of the book are to be stocked?"))
        print
        book1=books(an,bn,cn)
        
        

    n2=int(raw_input("How many initial members should the library have?"))
    print
    for i in range(0,n2):
        mn=raw_input("Please enter the name of member")
        print
        mem1=members(mn)

    books.booksm.sort()
    members.membersm.sort()
    return
    

def librcreator2():
    booksl=['Percy Jackson','Harry Potter','Tintin','The Cobra','GRK','Geronimo Stilton','Famous Five','Secret Seven','Changeling','Artemis Fowl']
    membersl=['hinata','oikawa','daichi','noya','kageyama','tanaka','sugawara','aone']
    booksd={'Percy Jackson':['Rick Riordan',4],'Harry Potter':['J.K. Rowling',4],'Tintin':['Herge',4],'The Cobra':['Frederick Forsyth',4],'GRK':['Joshua Doder',4],'Geronimo Stilton':['Geronimo Stilton',4],'Famous Five':['Enid Blyton',4],'Secret Seven':['Enid Blyton',4],'Changeling':['Steve Feasey',4],'Artemis Fowl':['Eoin Colfer',4]}
    for k in booksd:
        book1=books(k,booksd[k][0],booksd[k][1])
    for k in membersl:
        member1=members(k)
    books.booksm.sort()
    members.membersm.sort()
    return
    
        
        
        
        
        
print"HELLO!"
print
print"Welcome to the Otaku Library!"
print"This is a member based library. You need to be a member to participate."
print
print "The first step is to create a library"
print
print "You can choose to create a library of your own or you can continue with a pre-defined library"

choice1=raw_input("Enter 'a' to create your own library and enter anything else for a pre-defined library")

if choice1=="a":
    librcreator1()
else:
    librcreator2()

print "                                     Library has been created. Let's begin the real work                           "
print
count=0


print"Members of the Library are -"
print
for person in members.membersm:
    print person
    print
####??????????????????????????????????????????
while True:
    x='y'
    count=count+1 #time
    print'-----------------------------------------------------------------------------------------------------------------------------------------------------'
    print "DAY",count
    print
    #Position to insert code for time input
    while x=='y':
        name=raw_input("Hello! Please enter your name.")
        print
        for person1 in members.membersm:
            if name==person1:
                  print "Hello",name,",let me look through your status."
                  print
                  j=name+".dat"
                  file1=open(j,"rb")
                  person=pickle.load(file1)
                  file1.close()
                  
        
                  
                  if person.issue:

                       l=person.issue+".dat"
                       file2=open(l,"rb")
                       read=pickle.load(file2)
                       file2.close()
                      
                       print "You already have a book titled",person.issue,"written by",read.author,"issued",count-person.issd,"day(s) ago." #time
                       print

                       while True:
                          
                           print "Please select what you want to do by entering the number corresponding to the action."
                           print
                           print "1. Return book"
                           print "2. Check details of other books"
                           print "3. Exit"
                           print
                           choice=int(raw_input("Enter your choice-"))
                           print
                           if choice==1:
                               read.retbook(person.name)
                              
                               print "Your book has been returned."
                               print

                               if count - person.issd < 8:
                                   print "As the book was returned within the provided time period, no fine is to be paid."
                                   print
                               else:
                                   print "The book was not returned within provided time limit."
                                   print
                                   print "The fine to be paid is",(count - person.issd-7)*10,"$. Please pay the fine before proceeding."
                                   print
                               person.retbook()
                               break
                              
                           elif choice==2:
                               showbooks()
                           elif choice==3:
                               break
                           else:
                               print"Invalid choice! Try again."
                       print"If you want to perform any other activity, you will have to return later."
                      
                       print


                       print"Thank you for visiting.Please come again"
                      
                      
                       break
                    
                  else:
                      print "You don't have any issued book"
                      print

                      while True:
                          
                          print "Please select what you want to do by entering the number corresponding to the action."
                          print
                          print "1. Issue book"
                          print "2. Check details of other books"
                          print "3. Exit"
                          print
                          choice=int(raw_input("Enter your choice-"))
                          print

                          if choice==1:
                              print"HERE IS THE LIST OF BOOKS YOU CAN ISSUE"
                              for i in range(0,len(books.booksm)):
                                  l=books.booksm[i]+".dat"
                                  file2=open(l,"rb")
                                  read=pickle.load(file2)
                                  file2.close()
                                  if read.copies!=0:
                                      print i+1," ",books.booksm[i]
                                      print
                              
                              sele=int(raw_input("Enter the corresponding number to issue the book"))
                              print
                              sele=sele-1
                              j=books.booksm[sele]+".dat"
                              file1=open(j,"rb")
                              reader=pickle.load(file1)
                              file1.close()

                              reader.issbook(person.name)
                              person.issbook(reader.name)

                              print"Book successfully issued"
                              
                              
                              print"Thank you for visiting. As you have just issued a book, you will have to return again to perform any other activity"
                              print
                              print"Please return the book within 7 days to avoid a fine"
                              break
        
                          elif choice==2:
                              showbooks()
                          elif choice==3:
                              break
                          else:
                              print"Invalid choice! Try again." 
                              
                      print"If you want to perform any other activity, you will have to return later."
                      
                      print


                      print"Thank you for visiting.Please come again"
                      break      
                      
        else:
            print"Sorry! You are not a member."
            print
            ok=raw_input("Would you like to be a member? Press 'y' for yes and 'n' for no")
            print
            if ok=='y':
                name=raw_input("Please enter your name")
                print
                memb=members(name)
                members.membersm.sort()
                print"Congratulations! You are now a member of the Otaku Library"
                print
                print"As your information is still being processed, you cannot participate in any activities yet. Please come back later"
                print
        x=raw_input("Any other member ? Enter 'y' for yes and 'n' for no")
        print    

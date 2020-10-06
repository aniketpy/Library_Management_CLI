def display_books():

    f=open("books.txt","a+")
    a=f.seek(0)
    a=f.readlines()
    for i in range(len(a)):
        a[i]=a[i].strip("\n")

    print("\n")
    for j in a:
        j=j.title()
        print(j[0:len(j)-1:1])
    f.close()

def add_book():

    f=open("books.txt","a+")
    a=f.seek(0)
    a=f.readlines()
    for i in range(len(a)):
        a[i]=a[i].strip("\n")

    b=str(input("Enter the name of Book: "))
    b=b.lower()
    if b+"0" not in a and b+"1" not in a  :
        f.write(f"{b}1\n")
        print("Books added Succesfuly")
    else:
        print("Book is already present")
    f.close()

def allot_book():

    f=open("books.txt","a+")
    a=f.seek(0)
    a=f.readlines()
    for i in range(len(a)):
        a[i]=a[i].strip("\n")

    c=9999999999
    b=str(input("Enter the book you want:"))
    b=b.lower()
    for j,i in enumerate(a):
        if i[:len(i)-1]==b:c=j
    # print(c,a[c])
    if c!=9999999999:
        if a[c]==b+"0":
            print(f"Book is already taken")
            c=9999999999
        elif a[c]==b+"1":
            print(f"Book {b.title()} is Alloted")
            f.truncate(0)
            f.close()
            return a,c,b
    else:
        print(f"Book {b.title()} is not available")
    f.close()
    return a,c,b

def return_book():

    f=open("books.txt","a+")
    a=f.seek(0)
    a=f.readlines()
    for i in range(len(a)):
        a[i]=a[i].strip("\n")

    c=9999999999
    b=str(input("Enter the book you want to return:"))
    b=b.lower()
    for j,i in enumerate(a):
        if i[:len(i)-1]==b:c=j
    if c!=9999999999:
        if a[c]==f"{b}1":
            print(f"\nBook {b.title()} is already returned")
            c=9999999999
        elif a[c]==f"{b}0":
            print("\nYour book is returned sucessfully.\nThank You")
            f.truncate(0)
            f.close()
            return a,c,b
    else:
        print(f'\nBook "{b.title()}" is not available')
    f.close()
    return a,c,b

def re(a,c,b,value):
    g=open("books.txt","a+")
    for i in a:
        if i[:len(i)-1]==b:
            g.write(f"{b}{value}")
            g.write("\n")
        else:
            g.write(f"{i}")
            g.write("\n")
    g.close()
    
    

if __name__=="__main__":
    choice=0
    while(choice!=1):
        a=int(input("\n\nWelcome to Harry Library\n1.Display Books\n2.Add Books\n3.Allot Book\n4.Return Book\n5.Exit\n\t"))
        if a==1:
            display_books()
            print("\n")
        elif a==2:
            add_book()
        elif a==3:
            ad,c,b=allot_book()
            if c!=9999999999:
                re(ad,c,b,0)
        elif a==4:
            ad,c,b=return_book()
            if c!=9999999999:
                re(ad,c,b,1)
        elif a==5:break
        else:
            print("Enter correct options.")
        choice = int(input("\n\t\tPress 0 to Continue\n\t\t\t1 to Exit\n\t\t\t"))

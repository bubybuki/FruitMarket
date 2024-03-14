import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Frame, Label

current_username = ""

def connection():
    global conn, cursor
    conn = sqlite3.connect("fruitbase.db")
    cursor = conn.cursor()

def mainwindow():
    root = Tk()
    w = 1200
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.config(bg='#8E2727')
    root.title("Fruit Market")
    root.option_add('*font', "Helvetica 20 bold")
    root.rowconfigure((0, 3), weight=1)
    root.rowconfigure((1, 2), weight=1)
    root.columnconfigure((0, 3), weight=1)
    root.columnconfigure((1, 2), weight=1)
    return root

def loginlayout():
    global userentry, pwdentry

    loginframe = Frame(root, bg='#ffffff')
    loginframe.rowconfigure((0, 1, 2, 3), weight=1)
    loginframe.columnconfigure((0, 1), weight=1)
    loginframe.grid(row=0, column=0, columnspan=2, rowspan=4, sticky='news')
    Label(loginframe, text="Login", font="Helvetica 26 bold",
          compound=LEFT, bg='#ffffff', fg='#000').grid(row=0, columnspan=2)
    Label(loginframe, text="Username : ", bg='#ffffff',
          fg='#000', padx=20).grid(row=1, column=0, sticky='e')
    userentry = Entry(loginframe, bg='#E9E8E8', width=10)
    userentry.grid(row=1, column=1, sticky='w', padx=20)
    pwdentry = Entry(loginframe, bg='#E9E8E8', width=10, show='*')
    pwdentry.grid(row=2, column=1, sticky='w', padx=20)
    Label(loginframe, text="Password  : ", bg='#ffffff',
          fg='#000', padx=20).grid(row=2, column=0, sticky='e')
    Button(loginframe, image=btnLogin, width=270,border=0,activebackground="#ffffff", bg='#ffffff', command=lambda: loginclick(userentry.get(
    ), pwdentry.get())).grid(row=3, column=0,columnspan=2)

    # Right side

    rightframe = Frame(root, bg="#8E2727")
    rightframe.rowconfigure((0, 1,2,3), weight=1)
    rightframe.columnconfigure(0, weight=1)
    rightframe.grid(row=0, column=2, columnspan=2, sticky="news", rowspan=4)
    Label(rightframe,text="Welcome to our Fruit Market", bg='#8E2727',
          fg='#fff').grid(row=0, column=0,sticky='nw',padx=10)
    Label(rightframe,image=img1, bg='#8E2727',
          fg='#000').grid(row=0, column=0,rowspan=4)
    Label(rightframe,text="Don’t have an account?", bg='#8E2727',
          fg='#fff').grid(row=3, column=0,sticky='w',padx=90)
    Button(rightframe,text="Sign up",foreground="#A6A6A6",activebackground="#8E2727", cursor="hand2",border=0, bg='#8E2727',
          fg='#fff',command=lambda: [signuplayout()]).grid(row=3, column=0,sticky='e',padx=60)

def loginclick(username, password):
    global result
    global current_username
    if username == "" or password == "":
        messagebox.showwarning(
            "Admin : ", "Please enter a username or password")
        userentry.focus_force()
    else:
        sql = "select * from Login where Username=?;"
        cursor.execute(sql, [username])  # Change here to use the correct variable name
        result = cursor.fetchone()
        if result:
            sql = "select * from Login where Username=? and password=?;"
            cursor.execute(sql, [username, password])
            result = cursor.fetchone()
            if result:
                messagebox.showinfo("Admin : ", "Login Successfully.")
                current_username = username  #update current username
                homepage()
            else:
                messagebox.showwarning(
                    "Admin : ", "Incorrect Password \nPlease try again")
                pwdentry.selection_range(0, END)
                pwdentry.focus_force()
        else:
            messagebox.showwarning("Admin : ", "The username not found.")
            userentry.selection_range(0, END)
            userentry.focus_force()

def signuplayout():

    global leftframe, fnEntry, lnEntry, eaEntry, newUEntry, newpwdEntry, cfpwdEntry
    fnameinfo = StringVar()
    lnameinfo = StringVar()
    emailinfo = StringVar()
    newuserinfo = StringVar()
    newpwdinfo = StringVar()
    cfpwdinfo = StringVar()
    signupframe = Frame(root, bg="#fff")
    signupframe.rowconfigure(
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)
    signupframe.columnconfigure((0, 1), weight=1)
    signupframe.grid(row=0, column=0, columnspan=4,
                          sticky="news", rowspan=4)
    Label(signupframe, text="Sign up", font="Helvetica 35 bold",
          bg="#ffffff", fg="#000").grid(row=0, column=0, columnspan=2)
    for i in range(len(forsignup)):
        Label(signupframe, text=forsignup[i], bg="#ffffff", fg="#000", font="Helvetica 15 ").grid(
            row=i+1, column=0, sticky="e", padx=30)
    fnEntry = Entry(signupframe, bg='#E9E8E8', fg='#000',
                    width=30, textvariable=fnameinfo, font="Helvetica  15  ")
    fnEntry.grid(row=1, column=1, sticky="w")
    lnEntry = Entry(signupframe, bg='#E9E8E8', fg='#000',
                    width=30, textvariable=lnameinfo, font="Helvetica  15  ")
    lnEntry.grid(row=2, column=1, sticky="w")
    eaEntry = Entry(signupframe, bg='#E9E8E8', fg='#000',
                    width=30, textvariable=emailinfo, font="Helvetica  15  ")
    eaEntry.grid(row=3, column=1, sticky="w")
    newUEntry = Entry(signupframe, bg='#E9E8E8', fg='#000',
                      width=30, textvariable=newuserinfo, font="Helvetica  15  ")
    newUEntry.grid(row=4, column=1, sticky="w")
    newpwdEntry = Entry(signupframe, bg='#E9E8E8', fg='#000',
                        width=30, textvariable=newpwdinfo, font="Helvetica  15  ", show='*')
    newpwdEntry.grid(row=5, column=1, sticky="w")
    cfpwdEntry = Entry(signupframe, bg='#E9E8E8', fg='#000',
                       width=30, textvariable=cfpwdinfo, font="Helvetica  15  ", show='*')
    cfpwdEntry.grid(row=6, column=1, sticky="w")
    Button(signupframe, image=btnBacktoLogIn, border=0, bg="#ffffff", activebackground="#ffffff", command=loginlayout).grid(
        row=7, rowspan=2, column=0)
    Button(signupframe, image=btnCreateAcc, border=0, bg="#ffffff", activebackground="#ffffff", command=signupclick).grid(
        row=7, rowspan=2, column=1)

def signupclick():  # เสร็จแล้ว
    if fnEntry.get() == "":
        messagebox.showwarning("Admin: ", "Please enter a firstname")
        fnEntry.focus_force()
    elif lnEntry.get() == "":
        messagebox.showwarning("Admin : ", "Please enter a fullname")
        lnEntry.focus_force
    elif eaEntry.get() == "":
        messagebox.showwarning("Admin : ", "Please enter an Email")
        eaEntry.focus_force
    elif newUEntry.get() == "":
        messagebox.showwarning("Admin : ", "Please enter a username")
        newUEntry.focus_force
    elif newpwdEntry.get() == "":
        messagebox.showwarning("Admin : ", "Please enter a password")
        newpwdEntry.focus_force
    elif cfpwdEntry.get() == "":
        messagebox.showwarning("Admin : ", "Please enter a confirm password")
        cfpwdEntry.focus_force
    else:  # check a username is already exist???
        sql = "select * from Login where Username=?; "
        # execute sql query
        cursor.execute(sql, [newUEntry.get()])
        result = cursor.fetchone()  # fetch a result


        if result:
            messagebox.showerror(
                "Admin:", "The username is already exists\n Try again")
            newUEntry.selection_range(0, END)
            newUEntry.focus_force()
        else:
            if newpwdEntry.get() == cfpwdEntry.get():  # verify a new pwd and confirm pwd are equal
                # insert into statement
                sql = "INSERT INTO Login (Username, password, fname, lname, email) VALUES (?, ?, ?, ?, ?);"
                # execute sql query
                cursor.execute(sql, [newUEntry.get(), newpwdEntry.get(
                ), fnEntry.get(), lnEntry.get(), eaEntry.get()])
                conn.commit()
                messagebox.showinfo("Admin:", "Sign up Successfully")
            else:  # verify a new pwd and confirm pwd are not equal
                messagebox.showwarning(
                    "Admin: ", "Incorrect a confirm password\n Try again")
                cfpwdEntry.selection_range(0, END)
                cfpwdEntry.focus_force()

    fnEntry.delete(0, END)
    lnEntry.delete(0, END)
    eaEntry.delete(0, END)
    newUEntry.delete(0, END)
    newpwdEntry.delete(0, END)
    cfpwdEntry.delete(0, END)

def homepage():
    homeframe = Frame(root, bg="#fff")
    homeframe.rowconfigure(
        (0, 1,2,3), weight=1)
    homeframe.columnconfigure((0, 1,2,3,4), weight=1)
    homeframe.grid(row=0, column=0, columnspan=4,
                          sticky="news", rowspan=4)

    Label(homeframe,text="Product",bg="#fff").grid(row=0, column=0,columnspan=5)
    Button(homeframe,image=btnCart,border=0, bg="#ffffff", activebackground="#ffffff",command=cart).grid(row=0, column=3,columnspan=2,sticky='e',padx=20)
    Button(homeframe, image=imgorange, border=0, bg="#ffffff", activebackground="#ffffff",text="Orange", compound="top",command=orangepage).grid(
        row=1, column=1)
    Button(homeframe, image=imgbanana, border=0, bg="#ffffff", activebackground="#ffffff",text="Banana", compound="top",command=bananapage).grid(
        row=1, column=2)
    Button(homeframe, image=imgapple, border=0, bg="#ffffff", activebackground="#ffffff",text="Apple", compound="top",command=applepage).grid(
        row=1, column=3)
    Button(homeframe, image=imgwatermelon, border=0, bg="#ffffff", activebackground="#ffffff",text="Watermelon", compound="top",command=watermelonpage).grid(
        row=2, column=1)
    Button(homeframe, image=imggrape, border=0, bg="#ffffff", activebackground="#ffffff",text="Grape", compound="top",command=grapepage).grid(
        row=2, column=2)
    Button(homeframe, image=btnback, border=0, bg="#ffffff", activebackground="#ffffff",command=loginlayout).grid(
        row=3, column=0,columnspan=5)





def check_spinboxes(spinboxes, username, fruit_name):
    global sellers, sellerNames_list, fruitprice, fPriceResult

    try:
        spinbox_values = [int(spinbox.get()) for spinbox in spinboxes]
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid integer values in the Spinboxes.")
        return None

    # Count the number of Spinboxes with values greater than 0
    num_spinboxes_with_value = sum(1 for value in spinbox_values if value > 0)

    if num_spinboxes_with_value == 1:
        index_spinbox_with_value = spinbox_values.index(max(spinbox_values))  # Get the index of the Spinbox with the maximum value
        sellerName = sellers[index_spinbox_with_value]

        # Determine the table based on the selected fruit
        if fruit_name == 'banana':
            fruit_table = 'bananaPrice'
        elif fruit_name == 'grape':
            fruit_table = 'grapePrice'
        elif fruit_name == 'orange':
            fruit_table = 'orangePrice'
        elif fruit_name == 'apple':
            fruit_table = 'applePrice'
        elif fruit_name == 'watermelon':
            fruit_table = 'watermelonPrice'
        else:
            messagebox.showwarning("Invalid Fruit", "Selected fruit is not supported.")
            return None

        # Retrieve data from the appropriate table
        cursor.execute(f"SELECT {fruit_table} FROM sellerList WHERE sellerName = ?", (sellerName,))
        fruit_price = cursor.fetchone()[0]  # Assuming there's a single row for each seller in sellerList

        # Update the Login table and commit changes
        cursor.execute(f"UPDATE Login SET {fruit_name} = ? WHERE Username = ?", (sum(spinbox_values), username))
        conn.commit()

        # Calculate the total price and append it to fPriceResult
        total_price = fruit_price * sum(spinbox_values)
        fPriceResult.append(total_price)

        # Show information
        messagebox.showinfo("Information", f"Added {fruit_name} to cart. Seller: {sellerName}")
        sellerNames_list.append(fruit_name)
        sellerNames_list.append(sellerName)
        qtyL.append(sum(spinbox_values))
        fruitprice.append(fruit_price)  # Append the retrieved fruit price to the list
        print(sellerNames_list)
        print(fruitprice)
        print(qtyL)
        print(fPriceResult)

        return sellerName
    elif num_spinboxes_with_value > 1:
        # Show warning if more than one Spinbox has a value greater than 0
        messagebox.showwarning("Warning", "You can only add to one Spinbox at a time.")
        return None
    else:
        # Show warning if no Spinbox has a value greater than 0
        messagebox.showwarning("Warning", f"You must add a number to at least one {fruit_name} Spinbox")
        return None








#orange page
def orangepage():
    global current_username, first_orangespinbox, second_orangespinbox, third_orangespinbox, fourth_orangespinbox, orangespinboxes,sellers
    orangeframe = Frame(root, bg="#fff")
    orangeframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    orangeframe.columnconfigure((0, 1, 2, 3, 4), weight=1)
    orangeframe.grid(row=0, column=0, columnspan=4, sticky="news", rowspan=4)

    cursor.execute("UPDATE Login SET orange = NULL WHERE Username = ?", (current_username,))
    conn.commit()

    cursor.execute('SELECT sellername, Special, deliverTime, orangePrice,orange FROM sellerList')
    rows = cursor.fetchall()
    orangespinboxes = []  # List to store Spinbox widgets
    sellers = []  # List to store seller names

    for i in range(len(productlist)):
        Label(orangeframe, text=productlist[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=1, column=i, sticky="w", padx=30)

    for row_number, row_data in enumerate(rows):
        sellername, special, deliverTime, orangePrice, orange = row_data

        sellers.append(sellername)

        Label(orangeframe, text=sellername, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=0, sticky="w", padx=30)

        Label(orangeframe, text=special, bg="#ffffff", fg="#5DB63D", font="Helvetica 15").grid(
            row=row_number + 2, column=1, sticky="w", padx=30)

        Label(orangeframe, text=deliverTime, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=2, sticky="w", padx=30)

        # Display the orange amount as an integer
        Label(orangeframe, text=str(orangePrice), bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=3, sticky="w", padx=30)

        orangespinboxe = Spinbox(orangeframe, from_=0, to=orange, font="Helvetica 15", justify="center", width=10, increment=1)
        orangespinboxe.grid(row=row_number + 2, column=4, sticky="w")
        orangespinboxes.append(orangespinboxe)

    first_orangespinbox = orangespinboxes[0].get()
    second_orangespinbox = orangespinboxes[1].get()
    third_orangespinbox = orangespinboxes[2].get()
    fourth_orangespinbox = orangespinboxes[3].get()

    Button(orangeframe, image=btnback, bg="#fff", activebackground="#fff", border=0, command=homepage).grid(row=0, column=0, sticky='n', pady=20)
    Label(orangeframe, image=imgorange, bg="#fff", text="Orange", compound="bottom").grid(row=0, column=0, columnspan=5)
    Button(orangeframe, image=btnAddtoCart, bg="#fff", activebackground="#fff", border=0,
           command=lambda: check_spinboxes(orangespinboxes, current_username,"orange")).grid(row=0, column=4, sticky='n', pady=20)

#bnn page
def bananapage():
    global current_username,first_bananaspinbox , second_bananaspinbox , third_bananaspinbox , fourth_bananaspinbox,bananaspinboxes,sellers
    bananaframe = Frame(root, bg="#fff")
    bananaframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    bananaframe.columnconfigure((0, 1, 2, 3, 4), weight=1)
    bananaframe.grid(row=0, column=0, columnspan=4, sticky="news", rowspan=4)

    cursor.execute("UPDATE Login SET banana = NULL WHERE Username = ?", (current_username,))
    conn.commit()


    Button(bananaframe, image=btnback, bg="#fff", activebackground="#fff", border=0, command=homepage).grid(row=0, column=0, sticky='n', pady=20)
    Label(bananaframe, image=imgbanana, bg="#fff", text="Banana", compound="bottom").grid(row=0, column=0, columnspan=5)
    Button(bananaframe, image=btnAddtoCart, bg="#fff", activebackground="#fff", border=0,
           command=lambda: check_spinboxes(bananaspinboxes, current_username, "banana")).grid(row=0, column=4, sticky='n', pady=20)


    cursor.execute('SELECT sellername, Special, deliverTime, bananaPrice, banana FROM sellerList')
    rows = cursor.fetchall()
    bananaspinboxes = []  # List to store Spinbox widgets
    sellers = []

    for i in range(len(productlist)):
        Label(bananaframe, text=productlist[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=1, column=i, sticky="w", padx=30)

    for row_number, row_data in enumerate(rows):
        sellername, special, deliverTime, bananaPrice, banana = row_data

        sellers.append(sellername)

        Label(bananaframe, text=sellername, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=0, sticky="w", padx=30)

        Label(bananaframe, text=special, bg="#ffffff", fg="#5DB63D", font="Helvetica 15").grid(
            row=row_number + 2, column=1, sticky="w", padx=30)

        Label(bananaframe, text=deliverTime, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=2, sticky="w", padx=30)


        Label(bananaframe, text=str(bananaPrice), bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=3, sticky="w", padx=30)


        bananaspinbox = Spinbox(bananaframe, from_=0, to=banana, font="Helvetica 15", justify="center", width=10, increment=1)
        bananaspinbox.grid(row=row_number + 2, column=4,sticky="w")
        bananaspinboxes.append(bananaspinbox)

    # use later
    first_bananaspinbox = bananaspinboxes[0].get()
    second_bananaspinbox = bananaspinboxes[1].get()
    third_bananaspinbox = bananaspinboxes[2].get()
    fourth_bananaspinbox = bananaspinboxes[3].get()

#apple page
def applepage():
    global current_username, first_applespinbox, second_applespinbox, third_applespinbox, fourth_applespinbox, applespinboxes,sellers
    appleframe = Frame(root, bg="#fff")
    appleframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    appleframe.columnconfigure((0, 1, 2, 3, 4), weight=1)
    appleframe.grid(row=0, column=0, columnspan=4, sticky="news", rowspan=4)


    cursor.execute("UPDATE Login SET apple = NULL WHERE Username = ?", (current_username,))
    conn.commit()

    cursor.execute('SELECT sellername, Special, deliverTime, applePrice,apple FROM sellerList')
    rows = cursor.fetchall()
    applespinboxes = []  # List to store Spinbox widgets
    sellers = []  # List to store seller names

    for i in range(len(productlist)):
        Label(appleframe, text=productlist[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=1, column=i, sticky="w", padx=30)
        
    for row_number, row_data in enumerate(rows):
        sellername, special, deliverTime, applePrice, apple = row_data

        sellers.append(sellername)

        Label(appleframe, text=sellername, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=0, sticky="w", padx=30)

        Label(appleframe, text=special, bg="#ffffff", fg="#5DB63D", font="Helvetica 15").grid(
            row=row_number + 2, column=1, sticky="w", padx=30)

        Label(appleframe, text=deliverTime, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=2, sticky="w", padx=30)

        Label(appleframe, text=str(applePrice), bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=3, sticky="w", padx=30)

        applespinboxe = Spinbox(appleframe, from_=0, to=apple, font="Helvetica 15", justify="center", width=10, increment=1)
        applespinboxe.grid(row=row_number + 2, column=4, sticky="w")
        applespinboxes.append(applespinboxe)

    first_applespinbox = applespinboxes[0].get()
    second_applespinbox = applespinboxes[1].get()
    third_applespinbox = applespinboxes[2].get()
    fourth_applespinbox = applespinboxes[3].get()

    Button(appleframe, image=btnback, bg="#fff", activebackground="#fff", border=0, command=homepage).grid(row=0, column=0, sticky='n', pady=20)
    Label(appleframe, image=imgapple, bg="#fff", text="apple", compound="bottom").grid(row=0, column=0, columnspan=5)
    Button(appleframe, image=btnAddtoCart, bg="#fff", activebackground="#fff", border=0,
           command=lambda: check_spinboxes(applespinboxes, current_username,"apple")).grid(row=0, column=4, sticky='n', pady=20)
    
# watermelon page
def watermelonpage():
    global current_username, first_watermelonspinbox, second_watermelonspinbox, third_watermelonspinbox, fourth_watermelonspinbox, watermelonspinboxes,sellers
    watermelonframe = Frame(root, bg="#fff")
    watermelonframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    watermelonframe.columnconfigure((0, 1, 2, 3, 4), weight=1)
    watermelonframe.grid(row=0, column=0, columnspan=4, sticky="news", rowspan=4)

    cursor.execute("UPDATE Login SET watermelon = NULL WHERE Username = ?", (current_username,))
    conn.commit()

    cursor.execute('SELECT sellername, Special, deliverTime, watermelonPrice,watermelon FROM sellerList')
    rows = cursor.fetchall()
    watermelonspinboxes = []  # List to store Spinbox widgets
    sellers = []  # List to store seller names

    for i in range(len(productlist)):
        Label(watermelonframe, text=productlist[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=1, column=i, sticky="w", padx=30)
        
    for row_number, row_data in enumerate(rows):
        sellername, special, deliverTime, watermelonPrice, watermelon = row_data

        sellers.append(sellername)

        Label(watermelonframe, text=sellername, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=0, sticky="w", padx=30)

        Label(watermelonframe, text=special, bg="#ffffff", fg="#5DB63D", font="Helvetica 15").grid(
            row=row_number + 2, column=1, sticky="w", padx=30)

        Label(watermelonframe, text=deliverTime, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=2, sticky="w", padx=30)

        Label(watermelonframe, text=str(watermelonPrice), bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=3, sticky="w", padx=30)

        watermelonspinboxe = Spinbox(watermelonframe, from_=0, to=watermelon, font="Helvetica 15", justify="center", width=10, increment=1)
        watermelonspinboxe.grid(row=row_number + 2, column=4, sticky="w")
        watermelonspinboxes.append(watermelonspinboxe)

    first_watermelonspinbox = watermelonspinboxes[0].get()
    second_watermelonspinbox = watermelonspinboxes[1].get()
    third_watermelonspinbox = watermelonspinboxes[2].get()
    fourth_watermelonspinbox = watermelonspinboxes[3].get()

    Button(watermelonframe, image=btnback, bg="#fff", activebackground="#fff", border=0, command=homepage).grid(row=0, column=0, sticky='n', pady=20)
    Label(watermelonframe, image=imgwatermelon, bg="#fff", text="watermelon", compound="bottom").grid(row=0, column=0, columnspan=5)
    Button(watermelonframe, image=btnAddtoCart, bg="#fff", activebackground="#fff", border=0,
           command=lambda: check_spinboxes(watermelonspinboxes, current_username,"watermelon")).grid(row=0, column=4, sticky='n', pady=20)

# grape page
def grapepage():
    global current_username, first_grapespinbox, second_grapespinbox, third_grapespinbox, fourth_grapespinbox, grapespinboxes,sellers
    grapeframe = Frame(root, bg="#fff")
    grapeframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    grapeframe.columnconfigure((0, 1, 2, 3, 4), weight=1)
    grapeframe.grid(row=0, column=0, columnspan=4, sticky="news", rowspan=4)

    cursor.execute("UPDATE Login SET grape = NULL WHERE Username = ?", (current_username,))
    conn.commit()

    cursor.execute('SELECT sellername, Special, deliverTime, grapePrice,grape FROM sellerList')
    rows = cursor.fetchall()
    grapespinboxes = []  # List to store Spinbox widgets
    sellers = []  # List to store seller names

    for i in range(len(productlist)):
        Label(grapeframe, text=productlist[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=1, column=i, sticky="w", padx=30)
        
    for row_number, row_data in enumerate(rows):
        sellername, special, deliverTime, grapePrice, grape = row_data

        sellers.append(sellername)

        Label(grapeframe, text=sellername, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=0, sticky="w", padx=30)

        Label(grapeframe, text=special, bg="#ffffff", fg="#5DB63D", font="Helvetica 15").grid(
            row=row_number + 2, column=1, sticky="w", padx=30)

        Label(grapeframe, text=deliverTime, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=2, sticky="w", padx=30)

        Label(grapeframe, text=str(grapePrice), bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=row_number + 2, column=3, sticky="w", padx=30)

        grapespinboxe = Spinbox(grapeframe, from_=0, to=grape, font="Helvetica 15", justify="center", width=10, increment=1)
        grapespinboxe.grid(row=row_number + 2, column=4, sticky="w")
        grapespinboxes.append(grapespinboxe)

    first_grapespinbox = grapespinboxes[0].get()
    second_grapespinbox = grapespinboxes[1].get()
    third_grapespinbox = grapespinboxes[2].get()
    fourth_grapespinbox = grapespinboxes[3].get()

    Button(grapeframe, image=btnback, bg="#fff", activebackground="#fff", border=0, command=homepage).grid(row=0, column=0, sticky='n', pady=20)
    Label(grapeframe, image=imggrape, bg="#fff", text="grape", compound="bottom").grid(row=0, column=0, columnspan=5)
    Button(grapeframe, image=btnAddtoCart, bg="#fff", activebackground="#fff", border=0,
           command=lambda: check_spinboxes(grapespinboxes, current_username,"grape")).grid(row=0, column=4, sticky='n', pady=20)


def set_fruit_quantities_from_database():
    global current_username
    connection()
    query = f"SELECT COALESCE(orange, 0), COALESCE(banana, 0), COALESCE(apple, 0), COALESCE(watermelon, 0), COALESCE(grape, 0) FROM Login WHERE username = '{current_username}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        orangeQtt, bnnQtt, appleQtt, wmlQtt, grapeQtt = result
        fruitQttlist = [orangeQtt, bnnQtt, appleQtt, wmlQtt, grapeQtt]
        return fruitQttlist
    else:
        return [0, 0, 0, 0, 0]

def cart():
    global current_username 
    
    cartframe = Frame(root, bg="#fff")
    cartframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
    cartframe.columnconfigure((0, 1, 2, 3, 4), weight=1)
    cartframe.grid(row=0, column=0, columnspan=4, sticky="news", rowspan=4)
    Label(cartframe, text="Cart", bg="#fff").grid(row=0, column=0, columnspan=5)

    for i in range(len(cartlist)):
        Label(cartframe, text=cartlist[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=1, column=i + 2, sticky="w", padx=30)

    orangeQtt = 0
    bnnQtt = 0
    appleQtt = 0
    wmlQtt = 0
    grapeQtt = 0

    fruitQttlist = set_fruit_quantities_from_database()

    for i in range(len(fruitlist)):
        Label(cartframe, text=fruitlist[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=i + 2, column=2, sticky="w", padx=30)
        Label(cartframe, text=fruitQttlist[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=i + 2, column=3, sticky="w", padx=30)

    Button(cartframe, image=btnBackGrey, border=0, bg="#ffffff", activebackground="#ffffff", command=homepage).grid(
        row=8, column=0)
    
    
    Button(cartframe, image=btnRecipt, border=0, bg="#ffffff", activebackground="#ffffff",
           command=lambda: reciptpage()).grid(row=8, column=4)  
    
    

def reciptpage(): 

    reciptframe = Frame(root, bg="#fff")
    reciptframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15), weight=1)
    reciptframe.columnconfigure((0, 1, 2, 3, 4), weight=1)
    reciptframe.grid(row=0, column=0, columnspan=4, sticky="news", rowspan=4)
    Label(reciptframe, text="Payment Success!", bg="#fff").grid(row=0, column=0, columnspan=5)
    
    subtotal = sum(fPriceResult)
    vat = subtotal*0.07
    total = subtotal+vat

    for i in range(len(receiptlist)):
        Label(reciptframe, text=receiptlist[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=1, column=i+1, sticky="w", padx=30)

    #seller name
    for i in range(1, len(sellerNames_list), 2):
        Label(reciptframe, text="Seller name: "+sellerNames_list[i], bg="#ffffff", fg="#5DB63D", font="Helvetica 10").grid(row=i+2,
                                                                                                             column=2,
                                                                                                             sticky="nw",
                                                                                                             padx=30)

    #fruit name
    for i in range(0, len(sellerNames_list), 2):
        Label(reciptframe, text=sellerNames_list[i], bg="#ffffff", fg="#000", font="Helvetica 15").grid(row=i+2,
                                                                                                             column=2,
                                                                                                             sticky="w",
                                                                                                             padx=30)
            # Displaying Fruit Prices in the 3rd column
    for i, fruit_price in enumerate(fPriceResult):
        Label(reciptframe, text=fruit_price, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=2 * i + 2, column=3, sticky="w", padx=30
        )

    # Displaying Quantities in the 1st column
    for i, qty in enumerate(qtyL):
        Label(reciptframe, text=qty, bg="#ffffff", fg="#000", font="Helvetica 15").grid(
            row=2 * i + 2, column=1, sticky="w", padx=30
        )


            
    Label(reciptframe,text="Subtotal",bg="#ffffff", fg="#000", font="Helvetica 15").grid(row=12,
                                                                                                             column=2,
                                                                                                             sticky="w",
                                                                                                           padx=30)
    Label(reciptframe,text=subtotal,bg="#ffffff", fg="#000", font="Helvetica 15").grid(row=12,
                                                                                                             column=3,
                                                                                                             sticky="w",
                                                                                                             padx=30)
    Label(reciptframe,text="Vat 7%",bg="#ffffff", fg="#000", font="Helvetica 15").grid(row=13,
                                                                                                             column=2,
                                                                                                             sticky="w",
                                                                                                             padx=30)
    Label(reciptframe,text=vat,bg="#ffffff", fg="#000", font="Helvetica 15").grid(row=13,
                                                                                                             column=3,
                                                                                                             sticky="w",
                                                                                                             padx=30)
    Label(reciptframe,text="Total",bg="#ffffff", fg="#000", font="Helvetica 15 bold").grid(row=14,
                                                                                                             column=2,
                                                                                                             sticky="w",
                                                                                                             padx=30)
    Label(reciptframe,text=total,bg="#ffffff", fg="#000", font="Helvetica 15").grid(row=14,
                                                                                                             column=3,
                                                                                                             sticky="w",
                                                                                                             padx=30)


    Button(reciptframe,image=btnDone, border=0, bg="#ffffff", activebackground="#ffffff", command=lambda: (doneButton(),exit())).grid(row=15,column=0,columnspan=5)

def doneButton():
    cursor.execute("UPDATE Login SET orange = NULL,banana = NULL,apple = NULL,watermelon = NULL,grape = NULL WHERE Username = ?", (current_username,))
    conn.commit()


#
sellerNames_list = []
fruitprice = []
qtyL = []

#store the calculated  fruitprice and qtyL
fPriceResult = []

receiptlist = ["QTY",
                "Description",
                "Amount"]

fruitlist =["Orange",
            "Banana",
            "Apple",
            "Watermelon",
            "Grape"]

cartlist =["Name",
           "Quantity"]

productlist = ["seller name",
               "details",
               "deliverly time",
               "price/kg",
               "amount"]

forsignup = ["First Name : ",
             "last Name : ",
             "Email Address : ",
             "Username : ",
             "Password : ",
             "Confirm Password : "]
# Create Tkinter root window
root = mainwindow()

# Load image after creating the Tkinter root window
btnLogin = PhotoImage(file="img/btnLogin.png").subsample(2,2)
img1 = PhotoImage(file="img/fruitbasket.png").subsample(2,2)
btnCreateAcc = PhotoImage(file="img/btnCreateAccount.png").subsample(2,2)
btnBacktoLogIn = PhotoImage(file="img/btnBacktoLogIn.png").subsample(2,2)
imgorange = PhotoImage(file="img/orange.png")
imgbanana = PhotoImage(file="img/banana.png")
imgapple = PhotoImage(file="img/apple.png")
imgwatermelon = PhotoImage(file="img/watermelon.png")
imggrape = PhotoImage(file="img/grape.png")
btnback = PhotoImage(file="img/btnback.png")
btnAddtoCart = PhotoImage(file="img/btnAddtoCart.png")
btnCart = PhotoImage(file="img/btncart.png").subsample(2,2)
btnBackGrey = PhotoImage(file="img/btnBackgrey.png")
btnRecipt = PhotoImage(file="img/btnRecipt.png")
btnDone = PhotoImage(file="img/btnDone.png")

connection()
loginframe = Frame(root, bg='#739bb3')
loginlayout()

# conn.close()
root.mainloop()

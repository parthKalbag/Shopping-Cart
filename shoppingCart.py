from tkinter import *
import mysql.connector
import tkinter.messagebox as MessageBox
from mysql.connector import Error
from PIL import ImageTk, Image
from operator import itemgetter
import smtplib

from random import randint

def registerUser():
    # Submit for user
    def submit():
        u_name = user_name.get()
        passw = password.get()
        c_passw = confirm_password.get()
        f_name = first_name.get()
        l_name = last_name.get()
        
        gen = var.get()
        zipc = zipcode.get()
        que = queNumber.get()
        p_no = phone_no.get()
        em = email.get()
        answer = ans.get()

        if u_name == '' or passw == '' or c_passw == '' or f_name == '' or gen == '' or zipc == '' or p_no == '' or answer == '' or em == '':
            MessageBox.showinfo("Warning",
                                "All the fields marked with (*) are compulsory")
        if passw != c_passw:
            MessageBox.showinfo(
                'Warning', 'Password and confirm password does not match')

        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Parth@123",
                database="loginForPython"
            )
            c = conn.cursor()
            defaultIsLoggedInValue = 'F'
            
            # Insert the record into the table
            user_data = "insert into user_info values('"+u_name+"','"+passw+"','" + \
                f_name+"','"+l_name+"','"+gen+"','"+zipc+"','" + \
                em+"','"+que+"','"+answer+"','"+p_no+"','"+defaultIsLoggedInValue+"')"
            c.execute(user_data)
            # Commit Changes
            conn.commit()

            # Close the connection to the database
            conn.close()

        reset()
        showUserSubmitted = Toplevel()
        showUserSubmitted.geometry("300x300")
        showUserSubmitted.title("Submission")

        Label(showUserSubmitted, text="Registration Successfull").pack()

    def reset():
        user_name.delete(0, 'end')
        password.delete(0, 'end')
        confirm_password.delete(0, 'end')
        first_name.delete(0, 'end')
        last_name.delete(0, 'end')
        zipcode.delete(0, 'end')
        email.delete(0, 'end')
        phone_no.delete(0, 'end')
        ans.delete(0, 'end')
    
    register = Toplevel()
    register.title('Login System')
    register.geometry('500x500')

    var = StringVar(register)
    queNumber = StringVar(register)
    # Entries
    user_name = Entry(register, width=30)
    user_name.grid(row=0, column=1, padx=20)

    password = Entry(register, width=30, show="*")
    password.grid(row=1, column=1, padx=20)

    confirm_password = Entry(register, width=30, show="*")
    confirm_password.grid(row=2, column=1, padx=20)

    first_name = Entry(register, width=30)
    first_name.grid(row=3, column=1, padx=20)

    last_name = Entry(register, width=30)
    last_name.grid(row=4, column=1, padx=20)

    zipcode = Entry(register, width=30)
    zipcode.grid(row=9, column=1, padx=20)

    email = Entry(register, width=30)
    email.grid(row=10, column=1, padx=20)

    options = ('----None----', 'What was your favorite sport in high school?', "What is your pet's name?", "In what year was your father born?",
               "In what year was your mother born?", "In what country where you born?", "What is your favorite movie?", "What is your favorite sport?", "What is the name of your hometown?", "What was your favourite subject in school?")
    queNumber.set(options[0])
    drop = OptionMenu(register, queNumber, *options)
    drop.grid(row=11, column=1)
    ans = Entry(register, width=30)
    ans.grid(row=12, column=1, padx=20)

    phone_no = Entry(register, width=30)
    phone_no.grid(row=13, column=1, padx=20)

    # Labels
    Label(register, text="Username*").grid(row=0, column=0)
    Label(register, text="Password*").grid(row=1, column=0)
    Label(
        register, text="Confirm Password*").grid(row=2, column=0)
    Label(
        register, text="First Name*").grid(row=3, column=0)
    Label(register, text="Last Name").grid(row=4, column=0)

    Label(register, text='Gender*').grid(row=5, column=0)
    gender_of_male = Radiobutton(
        register, indicatoron=0, variable=var, text='Male', value='M')
    gender_of_male.grid(row=6, column=1, sticky="nsew")

    gender_female = Radiobutton(
        register, indicatoron=0, variable=var, text='Female', value='F')
    gender_female.grid(row=7, column=1, sticky="nsew")

    gender_trans = Radiobutton(
        register, indicatoron=0, variable=var, text='Other', value='T')
    gender_trans.grid(row=8, column=1, sticky="nsew")

    Label(register, text="Pincode*").grid(row=9, column=0)
    Label(register, text="Email*").grid(row=10, column=0)
    Label(
        register, text="Security question*").grid(row=11, column=0)
    Label(register, text="Answer*").grid(row=12, column=0)
    Label(register, text="Phone No*").grid(row=13, column=0)
    Label(
        register, text="All fields marked with (*) are compulsory").place(x=40, y=400)
    # Create Submit Button
    submit_btn = Button(register, text="Register",
                        command=submit)
    submit_btn.place(x=100, y=350)

    reset_btn = Button(register, text="Reset", command=reset)
    reset_btn.place(x=300, y=350)

    # Execute the register GUI
    register.mainloop()


def login_user():
    def checkUsernamePassword():
        def logout_command():
            logOut = Toplevel()
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Parth@123",
                database="loginForPython"
            )
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM user_info")
            myresult = mycursor.fetchall()
            logInDetail = 'F'
            mycursor.execute(
                "UPDATE user_info set isLoggedIn = ('"+logInDetail+"') where user_name=('"+username+"')")
            conn.commit()

            Label(logOut, text="You have successfully logged out").pack()
            logOut.mainloop()

        def product_category():
            loginUser.destroy()
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="Parth@123",
                    database="loginForPython"
                )

            c = conn.cursor()
            c.execute("SELECT * FROM products")
            allRecords = c.fetchall()

            productNames = list(map(itemgetter(1), allRecords))
            productInfo = list(map(itemgetter(2), allRecords))
            productPrice = list(map(itemgetter(3), allRecords))
            productImages = list(map(itemgetter(4), allRecords))
            productCategories = list(map(itemgetter(5), allRecords))
            
            def allCategory(row, x, y, categoryList, category):
                n=2
                cartBtnPath = "/home/dell/Desktop/VSCode/Python_proj/Images/CartIcon.ppm"       
                path = productImages[category]
                image = Image.open(path)
                [imageSizeWidth, imageSizeHeight] = [45, 75]
                same = True
                newImageSizeWidth = int(imageSizeWidth*n)
                if same:
                    newImageSizeHeight = int(imageSizeHeight*n) 
                else:
                    newImageSizeHeight = int(imageSizeHeight/n) 

                image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image)
                imgCanvas = Label(categoryList, image=img)
                imgCanvas.image = img
                imgCanvas.grid(row=row, column=0, padx=10, pady=10)
                
                cartBtnImg1 = Image.open(cartBtnPath)
                cartBtnImg1 = cartBtnImg1.resize((20, 20), Image.ANTIALIAS)

                cartBtnImg = ImageTk.PhotoImage(cartBtnImg1)
                Label(categoryList, text=productNames[category], font="Times 16").grid(row=row, column=1, padx=10, pady=10)
                my_btn = Button(categoryList, text="Add to Cart", font="Times 14", image=cartBtnImg, compound=LEFT)
                my_btn.image = cartBtnImg
                my_btn.grid(row=row, column=2, padx=10, pady=10)        
            
            def mobileCategory():
                mobilesList = Toplevel()
                mobilesList.geometry("700x700")
                mobilesList.title("Mobiles")

                Label(mobilesList, text="MOBILES LIST", font="Times 20").grid(row=0, column=1)
                row=0
                x=0
                y=0
                
                for category in range(len(productCategories)):
                    if productCategories[category] == 6666:
                        allCategory(row, x, y, mobilesList, category)
                        row+=1
                        x+=50
                        y+=50
                        

                mobilesList.mainloop()

            def fashionCategory():
                pass

            def homeCategory():
                pass

            def toysCategory():
                pass

            productCategory = Toplevel()
            productCategory.title("Product Category")
            productCategory.geometry("500x300")
            menubar = Menubutton(
                productCategory, text="---", relief=FLAT, justify=LEFT)
            menubar.place(x=0, y=0)
            menubar.menu = Menu(menubar)
            menubar["menu"] = menubar.menu
            menubar.menu.add_checkbutton(label=username)
            menubar.menu.add_checkbutton(
                label="Logout", command=logout_command)
            menubar.pack()

            mobiles = Button(productCategory, text="Mobiles",
                             command=mobileCategory)
            mobiles.place(x=50, y=50)

            fashion = Button(productCategory, text="Fashion",
                             command=fashionCategory)
            fashion.place(x=130, y=50)

            home = Button(productCategory, text="Home", command=homeCategory)
            home.place(x=210, y=50)

            toys = Button(productCategory, text="Toys", command=toysCategory)
            toys.place(x=290, y=50)

            productCategory.mainloop()

        username = username_entry.get()
        password = password_entry.get()
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Parth@123",
                database="loginForPython"
            )
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM user_info")

            myresult = mycursor.fetchall()
            username_list = list(map(itemgetter(0), myresult))
            password_list = list(map(itemgetter(1), myresult))
            isLoggedIn_list = list(map(itemgetter(10), myresult))
            if username in username_list:
                index_of_username = username_list.index(username)

                if password in password_list[index_of_username]:
                    logInDetail = isLoggedIn_list[index_of_username]
                    logInDetail = 'T'
                    username = username_entry.get()
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="Parth@123",
                        database="loginForPython"
                    )
                    mycursor = conn.cursor()
                    mycursor.execute("SELECT * FROM user_info")

                    myresult = mycursor.fetchall()
                    
                    mycursor.execute(
                        "UPDATE user_info set isLoggedIn = ('"+logInDetail+"') where user_name=('"+username+"')")
                    conn.commit()
                    product_category()

                else:
                    MessageBox.showinfo("Incorrect password",
                                        "Password entered by the user is incorrect")
            else:
                MessageBox.showinfo(
                    "Warning!", "Given username does not exist")
        except Error as e:
            print('MySQL connection is not established', e)
        finally:
            conn.close()

    def forgotPassword():
        def sendOTP():
            username = username_entry.get()
            email = email_id_entry.get()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()                
            server.login("10bparth@gmail.com", "*********")
            otpValue = str(randint(1000, 9999))
            msg = "{}".format(otpValue)
            conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="Parth@123",
                        database="loginForPython"
                    )
            mycursor = conn.cursor(buffered=True)
            mycursor.execute("SELECT * FROM user_info")
            sql= "UPDATE user_info SET otp=('"+otpValue+"') WHERE user_name=('"+username+"')"
            try:
                mycursor.execute(sql)
                conn.commit()
            except Exception as e:
                conn.rollback()
            finally:    
                server.sendmail("10bparth@gmail.com", email, msg)
                server.quit()
                conn.close()
        
        def update():
            username = username_entry.get()
            email = email_id_entry.get()
            newPassword = new_password_entry.get()
            confirmNewPassword = confirm_password_entry.get()
            otp = otp_entry.get()
            answer = ans.get()
            if newPassword != confirmNewPassword:
                MessageBox.showinfo("Warning!",
                                    "New password and confirm new password does not match")
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="Parth@123",
                        database="loginForPython"
                    )
                    mycursor = conn.cursor()
                    mycursor.execute("SELECT * FROM user_info")

                    myresult = mycursor.fetchall()
                    username_list = list(map(itemgetter(0), myresult))
                    email_id_list = list(map(itemgetter(6), myresult))
                    answers_list = list(map(itemgetter(8), myresult))
                    otp_list = list(map(itemgetter(11), myresult))

                    if username in username_list:
                        index_of_username = username_list.index(username)
                        if email in email_id_list[index_of_username]:
                            if otp in otp_list[index_of_username]:
                                if answer in answers_list[index_of_username]:
                                    sql = "UPDATE user_info SET password=('" + \
                                        newPassword + \
                                        "') WHERE user_name=('"+username+"')"
                                    try:
                                        mycursor.execute(sql)
                                        conn.commit()
                                    except Error as e:
                                        MessageBox.showinfo(
                                            "Error", "Error while connecting with database")
                                        conn.rollback()
                                else:
                                    MessageBox.showinfo(
                                        "Warning!", "Answer entered is incorrect")
                            else:
                                MessageBox.showinfo(
                                        "Warning!", "OTP entered is incorrect")
                                reset_forgot()
                        else:
                            MessageBox.showinfo("Incorrect email",
                                                "Email id entered by the user is incorrect")
                    else:
                        MessageBox.showinfo(
                            "Warning!", "Given username does not exist")
                except Error as e:
                    print("Error while connecting to database", e)
                finally:
                    conn.close()
            reset_forgot()

        def reset_forgot():
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            new_password_entry.delete(0, 'end')
            confirm_password_entry.delete(0, 'end')
            ans.delete(0, 'end')
            
        queNumber = StringVar()
        passwordForget = Toplevel()
        passwordForget.title("Forgot Password")
        passwordForget.geometry("300x650")
        Label(passwordForget, text="Username*").pack()
        username_entry = Entry(passwordForget, width=20)
        username_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Email ID*").pack()
        email_id_entry = Entry(passwordForget, width=20)
        email_id_entry.pack()

        Label(passwordForget, text="").pack()
        otp_btn = Button(passwordForget, text='Send OTP', command=sendOTP)
        otp_btn.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="OTP*").pack()
        otp_entry = Entry(passwordForget, width=20, show='*')
        otp_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="New Password*").pack()
        new_password_entry = Entry(passwordForget, width=20, show='*')
        new_password_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Confirm Password*").pack()
        confirm_password_entry = Entry(passwordForget, width=20, show='*')
        confirm_password_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Security Question*").pack()

        options = ('----None----', 'What was your favorite sport in high school?', "What is your pet's name?", "In what year was your father born?",
                   "In what year was your mother born?", "In what country where you born?", "What is your favorite movie?", "What is your favorite sport?", "What is the name of your hometown?", "What was your favourite subject in school?")
        queNumber.set(options[0])
        drop = OptionMenu(passwordForget, queNumber, *options)
        drop.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Answer*").pack()
        ans = Entry(passwordForget, width=30)
        ans.pack()

        Label(passwordForget, text="").pack()
        update_btn = Button(passwordForget, text='Update', command=update)
        update_btn.pack()

        Label(passwordForget, text="").pack()
        reset_btn = Button(passwordForget, text="Reset", command=reset_forgot)
        reset_btn.pack()

    def reset():
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

    loginUser = Toplevel()
    loginUser.title("Login")
    loginUser.geometry("300x300")

    Label(loginUser, text="Please enter login details").pack()
    Label(loginUser, text="").pack()

    username_label = Label(loginUser, text="Username*").pack()
    username_entry = Entry(loginUser, width=20)
    username_entry.pack()

    Label(loginUser, text="").pack()
    password_label = Label(loginUser, text="Password*").pack()
    password_entry = Entry(loginUser, width=20, show='*')
    password_entry.pack()

    Label(loginUser, text="").pack()
    login_button = Button(loginUser, text="Login", width=10,
                          height=1, command=checkUsernamePassword)
    login_button.pack()
    Label(loginUser, text="").pack()
    forgot_password = Button(
        loginUser, text="Forgot Password", width=15, height=1, command=forgotPassword)
    forgot_password.pack()
    Label(loginUser, text="").pack()

    reset_everything = Button(loginUser, text="Reset",
                              width=10, height=1, command=reset)
    reset_everything.pack()
    loginUser.mainloop()


def login_admin():
    def checkUsernamePassword():
        def logout_command():
            logOut = Toplevel()
            
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Parth@123",
                database="loginForPython"
            )
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM admin_info")
            myresult = mycursor.fetchall()
            
            logInDetail = 'F'
            mycursor.execute(
                "UPDATE admin_info set isLoggedIn = ('"+logInDetail+"') where admin_id=('"+username+"')")
            conn.commit()

            Label(logOut, text="You have successfully logged out").pack()
            logOut.mainloop()
        
        username = username_entry.get()
        password = password_entry.get()
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Parth@123",
                database="loginForPython"
            )
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM admin_info")

            myresult = mycursor.fetchall()
            username_list = list(map(itemgetter(0), myresult))
            password_list = list(map(itemgetter(1), myresult))
            isLoggedIn_list = list(map(itemgetter(6), myresult))
            if username in username_list:
                index_of_username = username_list.index(username)

                if password in password_list[index_of_username]:
                    logInDetail = isLoggedIn_list[index_of_username]
                    logInDetail = 'T'
                    username = username_entry.get()
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="Parth@123",
                        database="loginForPython"
                    )
                    mycursor = conn.cursor()
                    mycursor.execute("SELECT * FROM admin_info")

                    myresult = mycursor.fetchall()
                    
                    mycursor.execute(
                        "UPDATE admin_info set isLoggedIn = ('"+logInDetail+"') where admin_id=('"+username+"')")
                    conn.commit()
                    

                else:
                    MessageBox.showinfo("Incorrect password",
                                        "Password entered by the user is incorrect")
            else:
                MessageBox.showinfo(
                    "Warning!", "Given username does not exist")
        except Error as e:
            print('MySQL connection is not established', e)
        finally:
            conn.close()

    def forgotPassword():
        def sendOTP():
            username = username_entry.get()
            email = email_id_entry.get()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()                
            server.login("10bparth@gmail.com", "*********")
            otpValue = str(randint(1000, 9999))
            msg = "{}".format(otpValue)
            conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="Parth@123",
                        database="loginForPython"
                    )
            mycursor = conn.cursor(buffered=True)
            mycursor.execute("SELECT * FROM admin_info")
            sql= "UPDATE admin_info SET otp=('"+otpValue+"') WHERE admin_id=('"+username+"')"
            try:
                mycursor.execute(sql)
                conn.commit()
            except Exception as e:
                conn.rollback()
            finally:    
                server.sendmail("10bparth@gmail.com", email, msg)
                server.quit()
                conn.close()
        
        def update():
            username = username_entry.get()
            emailId = email_id_entry.get()
            newPassword = new_password_entry.get()
            confirmNewPassword = confirm_password_entry.get()
            otpValue = otp_entry.get()

            if newPassword != confirmNewPassword:
                MessageBox.showinfo("Warning!",
                                    "New password and confirm new password does not match")
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="Parth@123",
                        database="loginForPython"
                    )
                    mycursor = conn.cursor()
                    mycursor.execute("SELECT * FROM admin_info")

                    myresult = mycursor.fetchall()
                    username_list = list(map(itemgetter(0), myresult))
                    otp_list = list(map(itemgetter(8), myresult))
                    email_id_list = list(map(itemgetter(7), myresult))

                    if username in username_list:
                        index_of_username = username_list.index(username)
                        if emailId in email_id_list[index_of_username]:
                            if otpValue in otp_list[index_of_username]:
                                sql = "UPDATE admin_info SET password=('" + \
                                        newPassword + \
                                        "') WHERE admin_id=('"+username+"')"
                                try:
                                    mycursor.execute(sql)
                                    conn.commit()
                                except Error as e:
                                    MessageBox.showinfo(
                                            "Error", "Error while connecting with database")
                                    conn.rollback()
                            else:
                                MessageBox.showinfo("Incorrect OTP", "OTP entered by the user is incorrect")
                        else:
                            MessageBox.showinfo("Incorrect email",
                                                "Email ID entered by the user is incorrect")
                    else:
                        MessageBox.showinfo(
                            "Warning!", "Given username does not exist")
                except Error as e:
                    print("Error while connecting to database", e)
                finally:
                    conn.close()
            reset_forgot()

        def reset_forgot():
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            new_password_entry.delete(0, 'end')
            confirm_password_entry.delete(0, 'end')
            
            
        queNumber = StringVar()
        passwordForget = Toplevel()
        passwordForget.geometry("300x450")
        Label(passwordForget, text="Username*").pack()
        username_entry = Entry(passwordForget, width=20)
        username_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Email ID*").pack()
        email_id_entry = Entry(passwordForget, width=20)
        email_id_entry.pack()

        Label(passwordForget, text="").pack()
        otp_btn = Button(passwordForget, text='Send OTP', command=sendOTP)
        otp_btn.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="OTP*").pack()
        otp_entry = Entry(passwordForget, width=20, show='*')
        otp_entry.pack()

        Label(loginAdmin, text="").pack()
        Label(passwordForget, text="New Password*").pack()
        new_password_entry = Entry(passwordForget, width=20, show='*')
        new_password_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Confirm Password*").pack()
        confirm_password_entry = Entry(passwordForget, width=20, show='*')
        confirm_password_entry.pack()

        Label(passwordForget, text="").pack()
        update_btn = Button(passwordForget, text='Update', command=update)
        update_btn.pack()

        Label(passwordForget, text="").pack()
        reset_btn = Button(passwordForget, text="Reset", command=reset_forgot)
        reset_btn.pack()

    def reset():
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

    loginAdmin = Toplevel()
    loginAdmin.title("Login")
    loginAdmin.geometry("300x300")

    Label(loginAdmin, text="Please enter login details").pack()
    Label(loginAdmin, text="").pack()

    username_label = Label(loginAdmin, text="Username*").pack()
    username_entry = Entry(loginAdmin, width=20)
    username_entry.pack()

    Label(loginAdmin, text="").pack()
    password_label = Label(loginAdmin, text="Password*").pack()
    password_entry = Entry(loginAdmin, width=20, show='*')
    password_entry.pack()

    Label(loginAdmin, text="").pack()
    login_button = Button(loginAdmin, text="Login", width=10,
                          height=1, command=checkUsernamePassword)
    login_button.pack()
    
    Label(loginAdmin, text="").pack()
    forgot_password = Button(
        loginAdmin, text="Forgot Password", width=15, height=1, command=forgotPassword)
    forgot_password.pack()
    Label(loginAdmin, text="").pack()

    reset_everything = Button(loginAdmin, text="Reset",
                              width=10, height=1, command=reset)
    reset_everything.pack()
    loginAdmin.mainloop()

def main_screen():
    main = Tk()
    main.geometry("500x400")
    main.title("Main Screen")
    login_for_admin = Button(main, text="Login as admin", command=login_admin)
    login_for_admin.place(x=20, y=20, height=40, width=200)

    login_for_user = Button(main, text="Login as user", command=login_user)
    login_for_user.place(x=240, y=20, height=40, width=200)

    register_for_user = Button(
        main, text="Register as user", command=registerUser)
    register_for_user.place(x=120, y=120, width=200, height=40)

    main.mainloop()


if __name__ == "__main__":
    main_screen()
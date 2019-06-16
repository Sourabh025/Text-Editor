import pymysql

import tkinter


try:
    # Open database connection
    db = pymysql.connect("localhost", "root", "Admin@123", "mydb")
    print("connected to database")
    cursor = db.cursor()
except Exception as e:
    print("error in database", e)


def show_entry_fields():
    sql = "SELECT * FROM user WHERE user_name ='"+e1.get()+"' AND password='"+e2.get()+"'"
    print(sql)
    cursor.execute(sql)
    myresult = cursor.fetchall()
    if len(myresult)>0:
        print("login successful")
        success()

    else:
        print("login failed")
        screen_exit=tkinter.Toplevel(login)
        screen_exit.geometry('300x100')
        screen_exit.title("Eror")
        tkinter.Label(screen_exit, text="Eror please try again").grid(padx=60, pady=40)


login = tkinter.Tk()
login.title('LOGIN')
login.geometry('300x150+0+100')

b=tkinter.Label(login, text="username").grid(row=5, column=4)
c=tkinter.Label(login, text="password").grid(row=6, column=4)





e1 = tkinter.Entry(login)
e2 = tkinter.Entry(login)

e1.grid(row=5, column=6)
e2.grid(row=6, column=6)

tkinter.Button(login, text="Login", command=show_entry_fields, width=20, bg='blue').grid(row=7, column=6, pady=5)
tkinter.Button(login, text="Exit", command=login.destroy).grid(row=8, column=6, padx=5)




def body(screen):
    newscreen=tkinter.Toplevel(screen)
    newscreen.title("Body")
    newscreen.geometry("500x300")

    k="SELECT body FROM Post WHERE '1'=Post_id"
    cursor.execute(k)
    result= cursor.fetchall()
    w=tkinter.Label(newscreen, text=result, bg='orange').grid(padx=220, pady=100)
    print(result)


def userid(screen):

    newscreen=tkinter.Toplevel(screen)
    newscreen.title("userid")
    newscreen.geometry("500x300")

    n = "SELECT user_id FROM Post WHERE '1'=Post_id"
    cursor.execute(n)
    result=cursor.fetchall()
    w= tkinter.Label(newscreen, text=result, bg='orange').grid(padx=200, pady=100)
    print(result)

def comment(screen):
    newscreen=tkinter.Toplevel(screen)
    newscreen.title("comment")
    newscreen.geometry("500x300")


    m="SELECT comment FROM Post WHERE '1'=post_id"
    cursor.execute(m)
    result=cursor.fetchall()
    print(result)

    w=tkinter.Label(newscreen, text=result, bg='orange').grid(padx=220, pady=100)



def success():

    screen = tkinter.Toplevel(login)
    screen.geometry('1300x800')
    screen.title("Wellcome")
    #tkinter.Label(screen, text="You are successfully login").grid(padx=50, pady=50)
    x=tkinter.Button(screen, text="body", width=30, bg='blue', command=lambda: body(screen)).grid(row=1, column=4, pady=50, padx=70)
    z=tkinter.Button(screen, text="userid", width=30, bg='blue', command=lambda: userid(screen)).grid(row=1, column=5, pady = 50, padx=70)
    y=tkinter.Button(screen, text="comment", width=30, bg='blue', command=lambda: comment(screen)).grid(row=1, column=6, pady = 50, padx=70)

login.mainloop()

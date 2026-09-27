from tkinter import *
from tkinter import messagebox
import ast
import subprocess
import concurrent.futures

def open_deadlift_app():
    subprocess.run(["python", "deadlift.py"])

def open_deadlift_app_async():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(open_deadlift_app)

def open_squats_app():
    subprocess.run(["python", "squats.py"])

def open_squats_app_async():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(open_squats_app)

def signin():
    username = user.get()
    password = code.get()

    file = open('Datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:
        # Destroy the login window
        root.destroy()
        # Open the Deadlift app
        open_squats_app_async()
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

def signup_command():
    def signup():
        username = user.get()
        password = code.get()
        conform_password = conform_code.get()

        if password == conform_password:
            try:
                file = open('Datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate
                file.close()

                file = open('Datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Signup', 'Successfully sign up')
                window.destroy()

            except Exception as e:
                print(e)
                messagebox.showerror('Error', 'Failed to sign up')
        else:
            messagebox.showerror('Invalid', "Both passwords must match")

    def sign():
        window.destroy()

    window = Toplevel(root)
    window.title("Signup")
    window.geometry('925x500+300+200')
    window.configure(bg='white')
    window.resizable(True, True)

    img = PhotoImage(file='logi.png')
    Label(window, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg='black')
    frame.place(x=1000, y=50)

    heading = Label(frame, text='Sign up', fg='blue', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=120, y=5)

    code = Entry(frame, width=25, fg='black', border=2, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=25, y=150)
    code.insert(0, 'Password')

    user = Entry(frame, width=25, fg='black', border=2, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=25, y=83)
    user.insert(0, 'Username')

    conform_code = Entry(frame, width=25, fg='black', border=2, bg='white', font=('Microsoft Yahei UI Light', 11))
    conform_code.place(x=25, y=220)
    conform_code.insert(0, 'Confirm Password')

    Button(frame, width=39, pady=7, text='Sign up', bg='White', fg='blue', border=0, command=signup).place(x=35, y=280)
    Label(frame, text='I have an account', fg='black', bg='red', font=('Microsoft Yahei UI Light', 9)).place(x=90, y=340)

    signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='blue', command=sign)
    signin.place(x=200, y=340)

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='Orange')
root.resizable(True, True)

img = PhotoImage(file='logi.png')
Label(root, image=img, bg='white').place(x=50, y=85)

frame = Frame(root, width=500, height=500, bg='red')
frame.place(x=800, y=80)

heading = Label(frame, text='Sign in', fg='Yellow', bg='white', font=('Microsoft YaHei UI light', 23, 'bold'))
heading.place(x=200, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11))
user.place(x=10, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=207, height=2, bg='black').place(x=10, y=105)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        user.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11))
code.place(x=10, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=207, height=2, bg='black').place(x=10, y=175)

Button(frame, width=67, pady=7, text='Sign in', bg='blue', fg='white', border=0, command=signin).place(x=10, y=204)
Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=155, y=270)

Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='blue', command=signup_command).place(x=300, y=270)

root.mainloop()
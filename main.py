from tkinter import *
from tkinter import messagebox
import random
#import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers= [random.choice(numbers) for number in range(nr_numbers)]

    password_list = password_symbols + password_letters + password_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)

    pass_word.insert(0, password)

    #pyperclip.copy(password)
    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = web_name.get()
    mail = email_input.get()
    mot_de_pass = pass_word.get()

    if len(web) == 0 or len(mail) == 0 or len(mot_de_pass) == 0:
        messagebox.showinfo(title='Wrong input!', message="Don't leave any field empty!")
    elif len(mot_de_pass) < 8:
        messagebox.showinfo(title='Password', message='Password should be at least 8 characters')
    else:
        is_ok = messagebox.askokcancel(title=web, message=f'These are the entered details:\nWebsite: {web}'
                                                          f' \nEmail: {mail} \nPassword: {mot_de_pass}')
        if is_ok:
            with open('data.txt', mode='a') as login:
                login.write(f'\n{web} | {mail} | {mot_de_pass}')
                web_name.delete(0, END)
                pass_word.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
#window.minsize(width=600, height=500)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_pic = PhotoImage(file='logo.png')
canvas.create_image(100, 100 , image= lock_pic)
canvas.grid(column=1, row=0)

website = Label(text='Website:', font=('Ariel', 10, 'normal'))
website.grid(column=0, row=1)

web_name = Entry(width=39)
web_name.grid(column=1, row=1, columnspan=2)
web_name.focus()

email = Label(text='Email/Username:', font=('Ariel', 10, 'normal'))
email.grid(column=0, row=2)

email_input = Entry(width=39)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'sysavaneusman1@gmail.com')


password = Label(text='Password:', font=('Ariel', 10, 'normal'))
password.grid(column=0, row=3)

pass_word = Entry(width=21)
pass_word.grid(column=1, row=3)

gen_pass_button = Button(text='Generate Password', command=gen_password)
gen_pass_button.grid(column=2, row=3)


add_pass = Button(text='Add', width=34, command=save)
add_pass.grid(column=1, row=4, columnspan=2)



window.mainloop()

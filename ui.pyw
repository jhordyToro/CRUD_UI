
from tkinter import *
from main import *


# raiz=Tk()

# mi_nombre = StringVar()

# miframe = Frame(raiz, width=650, height=350)
# miframe.pack()

# def text(row,colum):
#     cuadrado_text = Entry(miframe)
#     cuadrado_text.grid(row=row, column=colum, padx=10, pady=10)

# def description(row,colum, name):
#     nombreLabel = Label(miframe, text=name)
#     nombreLabel.grid(row=row, column=colum, padx=10, pady=10)


# def run():
#     mi_nombre.set()

# bottom = Button(raiz, text='enviar', command=run)
# bottom.pack()

# nombreLabel = Label(miframe, text='nombre:')
# nombreLabel.grid(row=0, column=0, padx=10, pady=10)

# cuadrado_text = Entry(miframe, textvariable=mi_nombre)
# cuadrado_text.grid(row=0, column=1, padx=10, pady=10)


# description(1,0,'email')
# text(1,1)

# description(2,0,'address')
# text(2,1)



# raiz.mainloop()

raiz=Tk()
Status = False
miframe = Frame(raiz, width=650, height=350)
miframe.pack()

#-----------------------Save User-----------------------------------------------
def save():
    user = {
        'first_name': name_text.get(),
        'last_name': last_name_user_text.get(),
        'age': int(age_user_text.get()),
        'email': email_user_text.get(),
    }

    main = User()
    main.create_user(user)
    name_text.delete(0,"end")
    last_name_user_text.delete(0,"end")
    age_user_text.delete(0,"end")
    email_user_text.delete(0,"end")

# ------------------------Create-User---------------------------------------------

name_user = Label(miframe, text='<----------Create User--------------->')
name_user.grid(row=0, column=0, padx=10, pady=30, columnspan=2)


name_user = Label(miframe, text='First name:')
name_user.grid(row=1, column=0, padx=0, pady=0)
name_text = Entry(miframe)
name_text.grid(row=1, column=1, padx=0, pady=0)

last_name_user = Label(miframe, text='Last name:')
last_name_user.grid(row=2, column=0, padx=0, pady=0)
last_name_user_text = Entry(miframe)
last_name_user_text.grid(row=2, column=1, padx=0, pady=0)

age_user = Label(miframe, text='age User:')
age_user.grid(row=3, column=0, padx=0, pady=0)
age_user_text = Entry(miframe)
age_user_text.grid(row=3, column=1, padx=0, pady=0)

email_user = Label(miframe, text='Email:')
email_user.grid(row=4, column=0, padx=0, pady=0)
email_user_text = Entry(miframe)
email_user_text.grid(row=4, column=1, padx=0, pady=0)

bottom = Button(miframe, text='Save', command=save)
bottom.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

#-------------------------Upload User Funtion---------------------------------->

def upload():
    id = int(upload_name_text_id.get())
    user = {
        'first_name': upload_name_text.get(),
        'last_name': upload_last_name_user_text.get(),
        'age': int(upload_age_user_text.get()),
        'email': upload_email_user_text.get(),
    }

    main = User()
    main.upload_user(user,id)

    upload_name_text.delete(0,"end")
    upload_last_name_user_text.delete(0,"end")
    upload_age_user_text.delete(0,"end")
    upload_email_user_text.delete(0,"end")

#--------------------------Upload User--------------------------------->

upload_name_user_title = Label(miframe, text='<----------Upload User--------------->')
upload_name_user_title.grid(row=6, column=0, padx=0, pady=30, columnspan=2)

upload_name_user_id = Label(miframe, text='¿what is the id of the user you want to update?:')
upload_name_user_id.grid(row=7, column=0, padx=0, pady=0)
upload_name_text_id = Entry(miframe)
upload_name_text_id.grid(row=7, column=1, padx=0, pady=0)

upload_name_user = Label(miframe, text='¿what is the new first name?:')
upload_name_user.grid(row=8, column=0, padx=0, pady=0)
upload_name_text = Entry(miframe)
upload_name_text.grid(row=8, column=1, padx=0, pady=0)

upload_last_name_user = Label(miframe, text='¿what is the new last name?:')
upload_last_name_user.grid(row=9, column=0, padx=0, pady=0)
upload_last_name_user_text = Entry(miframe)
upload_last_name_user_text.grid(row=9, column=1, padx=0, pady=0)

upload_age_user = Label(miframe, text='¿what is the new age?:')
upload_age_user.grid(row=10, column=0, padx=0, pady=0)
upload_age_user_text = Entry(miframe)
upload_age_user_text.grid(row=10, column=1, padx=0, pady=0)

upload_email_user = Label(miframe, text='¿what is the new email?')
upload_email_user.grid(row=11, column=0, padx=0, pady=0)
upload_email_user_text = Entry(miframe)
upload_email_user_text.grid(row=11, column=1, padx=0, pady=0)

upload_bottom = Button(miframe, text='Upload', command=upload)
upload_bottom.grid(row=12, column=1, padx=10, pady=10, columnspan=2)

#-----------------------------Delete_funtion------------------->

def delete():
    id = int(delete_name_text.get())
    main = User()
    main.delete_user(id)

    delete_name_text.delete(0,'end')

#-----------------------------Delete_user-------------------->

delete_name_user = Label(miframe, text='<----------Delete User--------------->')
delete_name_user.grid(row=13, column=0, padx=10, pady=30, columnspan=2)

delete_name_user = Label(miframe, text='¿what is the id of the user you want to delete?:')
delete_name_user.grid(row=14, column=0, padx=0, pady=0)
delete_name_text = Entry(miframe)
delete_name_text.grid(row=14, column=1, padx=0, pady=0)

delete_bottom = Button(miframe, text='Delete', command=delete)
delete_bottom.grid(row=15, column=1, padx=10, pady=10, columnspan=2)


#------------------------------View Users-------------------------->

# def view():
#     main = CreateUser()
#     result = main.show_user()
#     for i in range(len(result)):
#         for resul in result:
#             result = dict(result)
#             view_name_label = Label(view_name_text, text=result['first_name'])    
#             view_name_label.grid(row=0,column=0,padx=10,pady=10)


def view2(): 
    main = User()
    result = main.show_user()

    view_name_label = Label(view_name_text, text=result)    
    view_name_label.grid(row=0,column=0,padx=10,pady=10)

def view():
    
    Status = True
    return Status


#-------------------------------View Users------------------------->

view_name_user = Label(miframe, text='<----------View User--------------->')
view_name_user.grid(row=0, column=8, padx=10, pady=30, columnspan=2)

view_name_user = Label(miframe, text='press to te buttom :')
view_name_user.grid(row=2, column=8, padx=0, pady=0)
view_name_text = Text(miframe, width=40, height=10)
view_name_text.grid(row=2, column=9, padx=0, pady=0, rowspan=4)

scroll = Scrollbar(miframe, command=view_name_text.yview)
scroll.grid(row=2, column=10, sticky="nsew")

view_name_text.config(yscrollcommand=scroll.set)

view_name_label = Label(view_name_text, text='you can go to the users.json file and see the result since it is not visible in the graphical interface, sorry :(')    
view_name_label.grid(row=3,column=10,padx=10,pady=10)


view_bottom = Button(miframe, text='see anyway', command=view2)
view_bottom.grid(row=6, column=9, padx=10, pady=10, columnspan=2)


raiz.mainloop()
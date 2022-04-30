from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
# sign in widow


root = Tk()
root.title("Sign in")

root.geometry("500x350+400+170")

root.configure(bg = "#334846")
root.resizable(width = False,height = False)

frame = Frame(root,padx = 136, pady = 103,bg = "#34495e",bd = 3,relief = "raised")
frame.pack(expand = True,pady = 5)

#img = Image.open("/home/wael/Downloads/University-Logo.png")
#resize = img.resize((200,80))
#new_img = ImageTk.PhotoImage(resize)

main_pic = Image.open("/home/wael/Downloads/main-ph.jpg")
new_img = ImageTk.PhotoImage(main_pic)

label_img = Label(frame,image = new_img,bg = "#34495e")
label_img.place(x = 65 , y = -90)


label1 = Label(frame,text = "user name",bg = "#34495e",fg = "white",padx = 30,font = ("Microsoft Yahei UI Light",11,'bold'))
label1.grid(row = 0 ,column = 0,pady = 3)

e1 = Entry(frame,borderwidth = 3)
e1.grid(row = 1,column = 0,ipadx = 30)

label2 = Label(frame,text = "password",bg = "#34495e",fg = "white",padx = 30,font = ("Microsoft Yahei UI Light",11,"bold"))
label2.grid(row = 2 ,column = 0,pady = 3)

e2 = Entry(frame,borderwidth = 3)
e2.grid(row = 3,column = 0,ipadx = 30,pady = 5)

def sign_in():
    global u_l
    u_l = {}
    conn2 = sqlite3.connect("Bank")
    c2 = conn2.cursor()
    
    c2.execute(""" SELECT * FROM users """)
    for f,u,i,p,g in c2.fetchall():
        u_l[u] = p
    
    if e1.get() in u_l.keys() and e2.get() == u_l[e1.get()]:
        root.destroy()
        sabu = Tk()
        geo = f"{sabu.winfo_screenwidth()}x{sabu.winfo_screenheight()}"

        ob = Sabratha_u(sabu,"Sabu",geo)
        
    else:
        messagebox.showerror("error","incorrect info")

b_sign = Button(frame,text = "Sign in",bg = "green",fg = "white",padx = 30,pady = 8,command = sign_in)
b_sign.grid(row = 4,column = 0,pady = 5)


# sign up widow

def sign_up():
    root_up = Toplevel()
    root_up.title("Sign up")
    root_up.geometry("450x350+400+150")
    root_up.configure(bg = "#aab7b8")
    
    #global new_img2
    #new_img2 = PhotoImage(file = "/home/wael/Downloads/Webp.net-resizeimage.png")

    #im_l = Label(root_up,image = new_img2)
    #im_l.place(x = 100 , y = 250 )
    
    l1 = Label(root_up,text = "Full Name",padx = 30,bg = "#F5F5F5")
    l1.grid(row = 0 ,column = 0)
    
    en1 = Entry(root_up,borderwidth = 3)
    en1.grid(row = 0,column = 1,ipadx = 50,ipady = 2)
    
    l2 = Label(root_up,text = "User name",padx = 30,bg = "#F5F5F5")
    l2.grid(row = 1 ,column = 0)
    
    en2 = Entry(root_up,borderwidth = 3)
    en2.grid(row = 1,column = 1,ipadx = 50,ipady = 2)
    
    l3 = Label(root_up,text = "ID",padx = 30,bg = "#F5F5F5")
    l3.grid(row = 2 ,column = 0)
    
    en3 = Entry(root_up,borderwidth = 3)
    en3.grid(row = 2,column = 1,ipadx = 50,ipady = 2)
    
    l4 = Label(root_up,text = "Password",padx = 30,bg = "#F5F5F5")
    l4.grid(row = 3 ,column = 0)
    
    en4 = Entry(root_up,borderwidth = 3)
    en4.grid(row = 3,column = 1,ipadx = 50,ipady = 2)
    
    s_v = StringVar()
    
    Radiobutton(root_up,text = "male",variable = s_v,value = 'male').place(x = 7,y = 140)
    Radiobutton(root_up,text = "female",variable = s_v,value = "female").place(x = 70,y = 140)
    
    en1.focus()
    def go_up():
        global user_n
        user_n = []
        ID = []
        if en1.get() and en2.get() and en3.get() and en4.get() and s_v.get() != "":
            conn = sqlite3.connect("Bank")
            c = conn.cursor()

            #c.execute(""" CREATE TABLE users (f_name,user_name,ID,pass,gender) """)
            c.execute(""" SELECT * FROM users """)
            for f,u,i,p,g in c.fetchall():
                user_n.append(u)
                ID.append(i)
  
            if en2.get() not in user_n and en3.get() not in ID :
                c.execute(f""" INSERT INTO users (f_name,user_name,ID,pass,gender) VALUES ('{en1.get()}','{en2.get()}','{en3.get()}','{en4.get()}','{s_v.get()}') """)
            
                en1.delete(0,END)
                en2.delete(0,END)
                en3.delete(0,END)
                en4.delete(0,END)
                
                messagebox.showinfo("message","succesfuly signed up")

            else:
                messagebox.showerror("error","user name or ID alrady taken!")
            conn.commit()
            conn.close()
           
        else:
            messagebox.showerror("error","check all fields")
    
    b_go = Button(root_up,text = "Sign Up",bg = "#3498db",fg = "white",padx = 100,pady = 10,command = go_up)
    b_go.grid(row = 4,column = 0 ,columnspan = 10,padx = 150,pady = 15)
    
b_up = Button(frame,text = "Sign up",bg = "#3498db",fg = "white",padx = 20,pady = 10,command = sign_up)
b_up.place(x = -135,y = -102)
e1.focus()


mainloop()

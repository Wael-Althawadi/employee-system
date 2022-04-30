from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import pandas as pd
import numpy
from tkinter import filedialog
from openpyxl import workbook,load_workbook
from tkinter import messagebox
from tkinter.font import Font

class Sabratha_u:
    def __init__(self,master,title,geometry):
        global i_b
        global i_b2
        global i_b3
        global i_b4
        
        self.my_font = Font(
        family = 'Times',
        size = 30,
        weight = 'bold',
        slant = 'roman',
        underline = 0,
        overstrike = 0
        )
        
        master.geometry(geometry)
        master.title(title)
        master.configure(bg = "white")
        self.B_frame = Frame(master,bg = "#80b5b0")
        self.B_frame.place(height = 70,width = 450,x = 430,y = 0)
        
        self.l = Label(self.B_frame,text = "Sabratha University",fg = "white",font = self.my_font,bg = "#80b5b0")
        self.l.place(width = 450, height =40, x= 0, y = 10)
        
        self.B_frame2 = Frame(master,bg = "white")
        self.B_frame2.place(height = 570,width = 1295,x = 0,y = 70)
        
        
        add_img = Image.open("/home/wael/un-sys/add-icon.jpg")
        i_b = ImageTk.PhotoImage(add_img)
        self.b_i = Button(master,image = i_b,bg = "white",command = self.add_user )
        self.b_i.place(x = 1000,y = 120)
        
        
        del_img = Image.open("/home/wael/un-sys/delete-icon.jpg")
        i_b2 = ImageTk.PhotoImage(del_img)
        self.b_i2 = Button(master,image = i_b2,bg = "white",command = self.delete_user )
        self.b_i2.place(x = 750,y = 120)

        
        srch_img = Image.open("/home/wael/un-sys/search-icon.jpg")
        i_b3 = ImageTk.PhotoImage(srch_img)
        self.b_i3 = Button(master,image = i_b3,bg = "white")
        self.b_i3.place(x = 450,y = 120)

        
        upd_img = Image.open("/home/wael/un-sys/update-icon.jpg")
        i_b4 = ImageTk.PhotoImage(upd_img)
        self.b_i4 = Button(master,image = i_b4,bg = "white")
        self.b_i4.place(x = 200,y = 120)
        
        self.menu2 = Menu(master,bg = "#80b5b0")
        self.sub_m = Menu(self.menu2,tearoff = 0) # or you can set tearoff to 0 to remove the line
        self.sub_m.add_command(label = "add users",command = self.add_user)
        self.sub_m.add_command(label = "delete users",command = self.delete_user)
        self.sub_m.add_separator()
        
        self.menu2.add_cascade(label = "edit",menu = self.sub_m)
        
        self.menu2.add_command(label = "exit",command = master.destroy)
        
        master.config(menu = self.menu2) 
        
        self.bottom_f = Frame(master,bg = "#80b5b0",bd = 0,relief = RIDGE)
        self.bottom_f.place(width = 1300,height = 25 ,x = 0,y = 653)
        
  
        
    def add_user(self):
        global pic
        global my_tree
        
        my_tree = ""
        
        root_add = Toplevel()
        root_add.geometry(f"{root_add.winfo_screenwidth()}x{root_add.winfo_screenheight()}")
        root_add.configure(bg = "#aab7b8")
        
        add_usr_ = Frame(root_add,bg = "#aab7b8",padx = 400)
        add_usr_.pack()

        add_pic = Image.open("/home/wael/un-sys/employee-icon.jpg")
        pic = ImageTk.PhotoImage(add_pic)

        l_img = Label(root_add,image = pic,bg = "#aab7b8",bd = 0)
        l_img.place(x = 1000,y = 30 )
        
        l_img2 = Label(root_add,image = pic,bg = "#aab7b8",bd = 0)
        l_img2.place(x = 100,y = 30 )
        
        l_1 = Label(add_usr_,text = "Full Name",padx = 30,bg = "#F5F5F5")
        l_1.grid(row = 0 ,column = 0)

        en_1 = Entry(add_usr_,borderwidth = 3)
        en_1.grid(row = 0,column = 1,ipadx = 90,ipady = 5)

        l_2 = Label(add_usr_,text = "age",padx = 30,bg = "#F5F5F5")
        l_2.grid(row = 1 ,column = 0)

        en_2 = Entry(add_usr_,borderwidth = 3)
        en_2.grid(row = 1,column = 1,ipadx = 90,ipady = 5)

        l_3 = Label(add_usr_,text = "ID",padx = 30,bg = "#F5F5F5")
        l_3.grid(row = 2 ,column = 0)

        en_3 = Entry(add_usr_,borderwidth = 3)
        en_3.grid(row = 2,column = 1,ipadx = 90,ipady = 5)

        l_4 = Label(add_usr_,text = "password",padx = 30,bg = "#F5F5F5")
        l_4.grid(row = 3 ,column = 0)

        en_4 = Entry(add_usr_,borderwidth = 3)
        en_4.grid(row = 3,column = 1,ipadx = 90,ipady = 5)

        s__v = StringVar()
        Radiobutton(add_usr_,text = "male",variable = s__v,value = 1).place(x = 130,y = 128)
        Radiobutton(add_usr_,text = "female",variable = s__v,value = 2).place(x = 300,y = 128)

        

        def go_add():
            
            if my_tree != "" :
                if en_1.get() and en_2.get() != "":
                    my_tree.insert("","end",values = (en_1.get(),en_2.get()))

                    wb = load_workbook(file_n)
                    ws = wb.active
                    ws.append([en_1.get(),en_2.get()])
                    wb.save(file_n)

                    messagebox.showinfo("message","succesfully added")
                    en_1.delete(0,END)
                    en_2.delete(0,END)
                else:
                    messagebox.showerror("error","check fields")
            else:
                messagebox.showerror("error","open file firist")

        add_go = Button(add_usr_,text = "ADD USER",bg = "#3498db",fg = "white",padx = 138,pady = 10,command = go_add)
        add_go.grid(row = 4 ,column = 1,pady = 25,rowspan = 4)


        def opn_file():
            global my_tree
            global df_rows_
            global file_n

            file_types = (("excel files","*.xlsx"),("all files","*.*"))
            file_n = filedialog.askopenfilename(initialdir = "/home/",title = "title",filetypes = file_types)

            if file_n:

                df = pd.read_excel(file_n)

                frame_add = Frame(root_add,bg = "#aab7b8")
                frame_add.place(width = 1291,x = 1,y = 250)

                my_tree = ttk.Treeview(frame_add)

                style_ = ttk.Style(frame_add)
                style_.theme_use('clam')

                my_tree["column"] = list(df.columns)
                my_tree["show"] = "headings"

                for col_ in df.columns:
                    my_tree.heading(col_,text=col_)

                df_rows_ = df.to_numpy().tolist()
                for row_ in df_rows_:
                    my_tree.insert("", "end",values= row_)


                my_tree.pack()
            else:
                messagebox.showwarning("warning","you did not choose a csv file")

        menu2 = Menu(root_add)
        root_add.config(menu = menu2)

        menu2.add_command(label = "open file",command = opn_file)


        
    def delete_user(self):
        global pic2
        del_usr = Toplevel()
        del_usr.geometry(f"{del_usr.winfo_screenwidth()}x{del_usr.winfo_screenheight()}")
        del_usr.configure(bg = "#aab7b8")
        
        del_usr_ = Frame(del_usr,bg = "#aab7b8",padx = 400)
        del_usr_.pack()
    
        add_pic2 = Image.open("/home/wael/un-sys/employee-icon.jpg")
        pic2 = ImageTk.PhotoImage(add_pic2)

        
        l_img_ = Label(del_usr,image = pic2,bg = "#aab7b8",bd = 0)
        l_img_.place(x = 1000,y = 30 )
        
        l_img_2 = Label(del_usr,image = pic2,bg = "#aab7b8",bd = 0)
        l_img_2.place(x = 100,y = 30 )
        
        l__1 = Label(del_usr_,text = "Full Name",padx = 30,bg = "#F5F5F5")
        l__1.grid(row = 0 ,column = 0)

        en__1 = Entry(del_usr_,borderwidth = 3)
        en__1.grid(row = 0,column = 1,ipadx = 90,ipady = 5)

        l__2 = Label(del_usr_,text = "age",padx = 30,bg = "#F5F5F5")
        l__2.grid(row = 1 ,column = 0)

        en__2 = Entry(del_usr_,borderwidth = 3)
        en__2.grid(row = 1,column = 1,ipadx = 90,ipady = 5)

        l__3 = Label(del_usr_,text = "ID",padx = 30,bg = "#F5F5F5")
        l__3.grid(row = 2 ,column = 0)

        en__3 = Entry(del_usr_,borderwidth = 3)
        en__3.grid(row = 2,column = 1,ipadx = 90,ipady = 5)

        l__4 = Label(del_usr_,text = "password",padx = 30,bg = "#F5F5F5")
        l__4.grid(row = 3 ,column = 0)

        en__4 = Entry(del_usr_,borderwidth = 3)
        en__4.grid(row = 3,column = 1,ipadx = 90,ipady = 5)

        s__v2 = StringVar()
        Radiobutton(del_usr_,text = "male",variable = s__v2,value = 1).place(x = 130,y = 128)
        Radiobutton(del_usr_,text = "female",variable = s__v2,value = 2).place(x = 300,y = 128)
        
        
        
        add_go = Button(del_usr_,text = "DELETE USER",bg = "#3498db",fg = "white",padx = 130,pady = 10)
        add_go.grid(row = 4 ,column = 1,pady = 25,rowspan = 4)


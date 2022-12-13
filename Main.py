from tkinter import * 
from tkinter import ttk  #Treeview library
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3
import Articles
import Login


class Main: 
    def __init__(self,window) -> None:
        self.window = window
        self.window.geometry('1600x600')
        self.window.title('Main Dashboard - 1.0')
######################################################################################################################
# ####################################################################################################################
#                                                   TASK BAR
#####################################################################################################################
#####################################################################################################################

        Taskbar = Menu(self.window)
        self.window.config(menu=Taskbar)
        #menu items
        def go_to_articles():
            win = Toplevel()
            Articles.Articles(win)
            #self.window.withdraw()
            #win.deiconify()
        
        def logout():
            win = Toplevel()
            Login.Login_Reg(win)
            self.window.withdraw()
            win.deiconify()

        Main = Menu(Taskbar)
        Taskbar.add_cascade(label= "Main", menu= Main)
        Main.add_command(label="Journal Papers", command=go_to_articles)
        Main.add_command(label="Logout",command=logout)
        

        #######################################################################
        # DataBase Connection
        #######################################################################


        conn = sqlite3.connect('Workflow.db')
        cursor = conn.cursor()

        cursor.execute(""" CREATE TABLE if not exists GroupProjects (
        Name text,
        Surname  text,
        Email text,
        Project text,
        Role,
        Task,
        Startdate ,
        Duedate ,
        Status text)

        """)
        conn.commit()
        conn.close()



        ##########################################################################
        #########################################################################

        # Treeview Styling

        style = ttk.Style()

        style.theme_use("default")
        style.configure('Treeview',background = '#D3D3D3', foreground = 'black', rowheight =25, fieldbackground = '#D3D3D3')
        style.map('Treeview',background = [('selected', "#347083")])

        tree_Frame = Frame(self.window)
        tree_Frame.pack(pady=10)


        tree_scroll = Scrollbar(tree_Frame)
        tree_scroll.pack(side= RIGHT,fill=Y)

        my_tree = ttk.Treeview(tree_Frame,yscrollcommand=tree_scroll.set,selectmode="extended")
        my_tree.pack()

        tree_scroll.config(command=my_tree.yview)

        #Define table columns
        my_tree['columns'] = ("ID","Name", "Surname", "Email", "Project","Role","Task", "Startdate", "Duedate", "Status")
        my_tree.column('#0',width=0, stretch =NO)
        my_tree.column("ID", anchor= W, width=40)
        my_tree.column("Name", anchor= CENTER, width=140)
        my_tree.column("Surname", anchor=CENTER , width=140)
        my_tree.column("Email", anchor=CENTER , width=170)
        my_tree.column("Project", anchor= CENTER, width=140)
        my_tree.column("Role", anchor= CENTER, width=140)
        my_tree.column("Task", anchor= CENTER, width=250)
        my_tree.column("Startdate", anchor= CENTER, width=140)
        my_tree.column("Duedate", anchor= CENTER, width=140)
        my_tree.column("Status", anchor=CENTER , width=140)

        my_tree.heading('#0',text='',anchor=W)
        my_tree.heading('ID',text='ID',anchor=W)
        my_tree.heading('Name',text='Name',anchor=CENTER)
        my_tree.heading('Surname',text='Surname',anchor=CENTER)
        my_tree.heading('Email',text='Email',anchor=CENTER)
        my_tree.heading('Project',text='Project',anchor=CENTER)
        my_tree.heading('Role',text='Role',anchor=CENTER)
        my_tree.heading('Task',text='Task',anchor=CENTER)
        my_tree.heading('Startdate',text='Startdate',anchor=CENTER)
        my_tree.heading('Duedate',text='Duedate',anchor=CENTER)
        my_tree.heading('Status',text='Status',anchor=CENTER)


        my_tree.tag_configure("Completed",background="lightgreen")
        my_tree.tag_configure("Overdue",background="red")
        my_tree.tag_configure("In-Progress",background="lightyellow")

        def QueryDB():
            for i in my_tree.get_children():
                my_tree.delete(i)
            conn = sqlite3.connect('Workflow.db')
            cursor = conn.cursor()

            cursor.execute("SELECT rowid,* FROM GroupProjects")

            records = cursor.fetchall()   
             
            
            for record in records:
                if record[9] == 'Completed':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9]), tags=('Completed',))

                elif record[9] == 'Overdue':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9]), tags=('Overdue',))

                else:
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9]), tags=('In-Progress',)) 

        
            conn.commit()
            conn.close()

        #########################################################################################################################################
        # #######################################################################################################################################
        #                                                       Entry Boxes
        ########################################################################################################################################
        ########################################################################################################################################

        data_frame = LabelFrame(self.window,text="Record")
        data_frame.pack(fill='x',expand=YES,padx=20)

        #Entries
        ID_entry = Entry(data_frame)

        Name_label = Label(data_frame,text="Name")
        Name_label.grid(row=0,column=0,padx=10,pady=10)
        Name_Entry = Entry(data_frame)
        Name_Entry.grid(row=0,column=1,padx=10, pady=10)

        Surname_label = Label(data_frame,text="Surname")
        Surname_label.grid(row=0,column=2,padx=10,pady=10)
        Surname_Entry = Entry(data_frame)
        Surname_Entry.grid(row=0,column=3,padx=10, pady=10)

        Email_label = Label(data_frame,text="Email")
        Email_label.grid(row=0,column=4,padx=10,pady=10)
        Email_Entry = Entry(data_frame)
        Email_Entry.grid(row=0,column=5, ipadx=20, pady=10)

        Role_label = Label(data_frame,text="Role")
        Role_label.grid(row=0,column=6,padx=10,pady=10)
        role_options = ["Lead", "Project Manager", "Resource", "Editor"]
        Role = ttk.Combobox(data_frame,value=role_options)
        Role.bind("<<ComboboxSelected>>")
        Role.grid(row=0,column=7,padx=10, pady=10)
        
        Task_label = Label(data_frame,text="Task")
        Task_label.grid(row=0,column=8,padx=10,pady=10)
        Task_Entry = Entry(data_frame)
        Task_Entry.grid(row=0,column=9, ipadx = 20, pady=10)


        Project_label = Label(data_frame,text="Project")
        Project_label.grid(row=1,column=0,padx=10,pady=10)
        project_options = ["MBA HEALTH", "CHIETA", "Book chapter", "BankSeta","Accenture Program","Joburg Water", "Rand Refinery","CWTT","Work Management"]
        Project = ttk.Combobox(data_frame,value=project_options)
        Project.bind("<<ComboboxSelected>>")
        Project.grid(row=1,column=1,padx=10, pady=10)
        
        Strtdate_label = Label(data_frame,text="Startdate")
        Strtdate_label.grid(row=1,column=2,padx=10,pady=10)
        Strtdate_Entry = DateEntry(data_frame)
        Strtdate_Entry.grid(row=1,column=3,padx=10, pady=10)


        Duedate_label = Label(data_frame,text="Duedate")
        Duedate_label.grid(row=1,column=4,padx=10,pady=10)
        Duedate_Entry = DateEntry(data_frame)
        Duedate_Entry.grid(row=1,column=5,padx=10, pady=10)

        Status_label = Label(data_frame,text="Status")
        Status_label.grid(row=1,column=6,padx=10,pady=10)
        status_options = ["In-Progress","Completed","Overdue"]
        Status = ttk.Combobox(data_frame,value=status_options)
        Status.bind("<<ComboboxSelected>>")
        Status.grid(row=1,column=7,padx=10, pady=10)

        
        ##################################################################################################################
        #################################################################################################################
        #                                           FUNCTIONS
        ################################################################################################################
        ################################################################################################################

        def Remove():
                
            response = messagebox.askyesno("WARNING","Are you sure you want to delete \nALL selected records?")
            
            if response == 1:
                        
                entries = my_tree.selection()

                #LIST OF IDs to delete
                ids_to_delete = []

                for entry in entries:
                    ids_to_delete.append(my_tree.item(entry,'values')[0])
                

                for entry in entries:
                    my_tree.delete(entry)


                conn = sqlite3.connect('Workflow.db')
                cursor = conn.cursor()

                cursor.executemany("DELETE FROM GroupProjects WHERE oid = ?",[(a,) for a in ids_to_delete])

                conn.commit()
                conn.close()
            clearEntries()


        def add_record():
            conn = sqlite3.connect('Workflow.db')
            cursor = conn.cursor() 

            cursor.execute("INSERT INTO GroupProjects VALUES (:Name, :Surname, :Email, :Project, :Role, :Task, :Startdate, :Duedate, :Status )",
            {
                'Name': Name_Entry.get(),
                'Surname': Surname_Entry.get(),
                'Email': Email_Entry.get(),
                'Project': Project.get(),
                'Role':Role.get(),
                'Task': Task_Entry.get(),
                'Startdate': Strtdate_Entry.get(),
                'Duedate': Duedate_Entry.get(),
                'Status': Status.get()
            }
            )

            conn.commit()
            conn.close()

            #clear entryboxes
            clearEntries()

            my_tree.delete(* my_tree.get_children())
            QueryDB()


        def Update():
            selected = my_tree.focus()
            my_tree.item(selected, text="", values=(ID_entry.get(),Name_Entry.get(), Surname_Entry.get(),Email_Entry.get(),Project.get(),Role.get(),Task_Entry.get(),Strtdate_Entry.get(),Duedate_Entry.get(),Status.get(), ))
            
            conn = sqlite3.connect('Workflow.db')
            cursor = conn.cursor() 

            cursor.execute(""" UPDATE GroupProjects SET
                        Name = :Name, 
                        Surname = :Surname, 
                        Email = :Email,
                        Project = :Project, 
                        Role = :Role,
                        Task = :Task,
                        Startdate =:Startdate, 
                        Duedate =:Duedate, 
                        Status =:Status       

                        WHERE oid = :oid """,
                        {
                            'Name': Name_Entry.get(),
                            'Surname': Surname_Entry.get(),
                            'Email': Email_Entry.get(),
                            'Project': Project.get(),
                            'Role': Role.get(),
                            'Task': Task_Entry.get(),
                            'Startdate': Strtdate_Entry.get(),
                            'Duedate': Duedate_Entry.get(),
                            'Status': Status.get(),
                            'oid': ID_entry.get()
                        })

            conn.commit()
            conn.close()

            clearEntries()
            #clear entryboxes
            
        def clearEntries():
            ID_entry.delete(0,END)
            Name_Entry.delete(0,END)
            Surname_Entry.delete(0,END)
            Email_Entry.delete(0,END)
            Project.delete(0,END)
            Role.delete(0,END),
            Task_Entry.delete(0,END),
            Strtdate_Entry.delete(0,END)
            Duedate_Entry.delete(0,END)
            Status.delete(0,END)

        def lookup_record():
            x = search_entry.get()
            searchbox.destroy()
            #Clear treeview
            for i in my_tree.get_children():
                my_tree.delete(i)

            conn = sqlite3.connect('Workflow.db')
            cursor = conn.cursor()

            cursor.execute("SELECT rowid,* FROM GroupProjects WHERE Name like ? OR Surname like ? OR Project like ?",(x,x,x,))

            records = cursor.fetchall()   
            #global count 
            #count = 0 
            

            for record in records:
                if record[9] == 'Completed':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9]), tags=('Completed',))

                elif record[9] == 'Overdue':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9]), tags=('Overdue',))

                else:
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9]), tags=('In-Progress',)) 


            conn.commit()
            conn.close()


        def search_record():
            global search_entry,searchbox
            searchbox = Toplevel(self.window)
            searchbox.title("Search Records")
            searchbox.geometry("250x150")
            searchframe = LabelFrame(searchbox)
            searchframe.pack(padx=20, pady=20)
            search_entry = Entry(searchframe)
            search_entry.pack(padx=10,pady=10)

            search_button = Button(searchbox,text= "Search", command=lookup_record)
            search_button.pack(padx=10,pady=10)

            
        def Selected (event):
            clearEntries()

            selected = my_tree.focus()
            values = my_tree.item(selected,'values')
            ID_entry.insert(0,values[0])
            Name_Entry.insert(0,values[1])
            Surname_Entry.insert(0,values[2])
            Email_Entry.insert(0,values[3])
            Project.insert(0,values[4])
            Role.insert(0,values[5])
            Task_Entry.insert(0,values[6])
            Strtdate_Entry.insert(0,values[7])
            Duedate_Entry.insert(0,values[8])
            Status.insert(0,values[9])

        #Bind
        my_tree.bind("<ButtonRelease-1>",Selected)

        ################################################################################################################################
        # ###########################################################################################################################3###
        #                                                               Buttons
        ##################################################################################################################################
        ##################################################################################################################################

        button_frame = LabelFrame(self.window, text='Commands')
        button_frame.pack(fill=X, expand=YES, padx=20)

        Search_button = Button(button_frame, text="Search Records", command=search_record)
        Search_button.grid(row = 0, column= 0, padx=10 , pady=10 )

        Refresh_button = Button(button_frame, text="Refresh Records",command=QueryDB)
        Refresh_button.grid(row=0,column=4,padx=10,pady=10)

        Add_button = Button(button_frame, text="Add New Record", command=add_record)
        Add_button.grid(row = 0, column= 1, padx=10 , pady=10 )

        Update_button = Button(button_frame, text="Update selected record",command=Update)
        Update_button.grid(row =0 , column=2 , padx= 10, pady=10 )

        Remove_button = Button(button_frame, text="Remove record(s)",command=Remove)
        Remove_button.grid(row =0 , column= 3, padx= 10, pady=10 )

        QueryDB()

        
def page():
    window =Tk()
    Main(window)
    window.mainloop()

if __name__ == '__main__':
    page()
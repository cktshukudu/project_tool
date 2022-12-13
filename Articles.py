from tkinter import * 
from tkinter import ttk  #Treeview library
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3


class Articles:
    def __init__(self,window) -> None:
        self.window = window
        self.window.geometry('1200x600')
        self.window.title('Articles Dashboard - 1.0')
       # self.window.state('zoomed')

        ###########################################################################################################################################################
                                                                         # DataBase Connection
        ############################################################################################################################################################

        conn = sqlite3.connect('Workflow.db')
        cursor = conn.cursor()

        cursor.execute(""" CREATE TABLE if not exists Articles (
        Name text,
        Surname  text,
        Email text,
        Paper text,
        Journal text,
        Status text)
        """)
        conn.commit()
        conn.close()

        #################################################################################################################################################################

        ############################################################################################################################################################

                                                                   #Styling Treeview                

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

        #Define table in treeview columns
        my_tree['columns'] = ("ID","Name", "Surname", "Email", "Paper","Conference/Journal","Status")
        my_tree.column('#0',width=0, stretch =NO)
        my_tree.column("ID", anchor= W, width=40)
        my_tree.column("Name", anchor= CENTER, width=140)
        my_tree.column("Surname", anchor=CENTER , width=140)
        my_tree.column("Email", anchor=CENTER , width=165)
        my_tree.column("Paper", anchor= CENTER, width=200)
        my_tree.column("Conference/Journal", anchor= CENTER, width=140)
        my_tree.column("Status", anchor= CENTER, width=140)


        my_tree.heading('#0',text='',anchor=W)
        my_tree.heading('ID',text='ID',anchor=W)
        my_tree.heading('Name',text='Name',anchor=CENTER)
        my_tree.heading('Surname',text='Surname',anchor=CENTER)
        my_tree.heading('Email',text='Email',anchor=CENTER)
        my_tree.heading('Paper',text='paper',anchor=CENTER)
        my_tree.heading('Conference/Journal',text='Conference/Journal',anchor=CENTER)
        my_tree.heading('Status',text='Status',anchor=CENTER)

        my_tree.tag_configure("Writting",background="#FFFFFF")
        my_tree.tag_configure("Editing",background="#CDCDBA")
        my_tree.tag_configure("Submitted",background="lightblue")
        my_tree.tag_configure("Accepted",background="lightgreen")
        my_tree.tag_configure("Rejected",background="tomato")
        my_tree.tag_configure("Published",background="PaleGreen3")


        def QueryDB():
            for i in my_tree.get_children():
                my_tree.delete(i)
            conn = sqlite3.connect('Workflow.db')
            cursor = conn.cursor()

            cursor.execute("SELECT rowid,* FROM Articles")

            records = cursor.fetchall()   
            #global count 
            #count = 0 
            

            for record in records:
                if record[6] == 'Writting':
                
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Writting',))

                elif record[6] == 'Editing':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Editing',))

                elif record[6] == 'Submitted':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Submitted',)) 

                elif record[6] == 'Accepted':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Accepted',))

                elif record[6] == 'Rejected':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Rejected',))

                else:
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Published',))


            conn.commit()
            conn.close()

        ###############################################################################################################################
        # #############################################################################################################################
        #                                          Entry Boxes (Record)
        ##############################################################################################################################
        #############################################################################################################################

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

        Paper_label = Label(data_frame,text="Paper")
        Paper_label.grid(row=0,column=8,padx=10,pady=10)
        Paper_Entry = Entry(data_frame)
        Paper_Entry.grid(row=0,column=9, ipadx = 20, pady=10)


        Journal_label = Label(data_frame,text="Journal or Conference")
        Journal_label.grid(row=1,column=0,padx=10,pady=10)
        Journal_Entry = Entry(data_frame)
        Journal_Entry.grid(row=1,column=1, padx=10, pady=10)


        Status_label = Label(data_frame,text="Status")
        Status_label.grid(row=1,column=2,padx=10,pady=10)

       
        status_options = ["Writting","Editing","Submitted","Accepted","Rejected","Published"]
        Status = ttk.Combobox(data_frame,value=status_options)
        Status.bind("<<ComboboxSelected>>")
        Status.grid(row=1,column=3,padx=10, pady=10)
    
    ###########################################################################################################################################################
    ##########################################################################################################################################################

    
    ###########################################################################################################################################################
    ###########################################################################################################################################################
                                                                            #Functions
    ##########################################################################################################################################################
    # #######################################################################################################################################################
                                                                            
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

                cursor.executemany("DELETE FROM Articles WHERE oid = ?",[(a,) for a in ids_to_delete])

                conn.commit()
                conn.close()
            clearEntries()


        def add_record():
            conn = sqlite3.connect('Workflow.db')
            cursor = conn.cursor() 

            cursor.execute("INSERT INTO Articles VALUES (:Name, :Surname, :Email, :Paper,:Journal,:Status )",
            {
                'Name': Name_Entry.get(),
                'Surname': Surname_Entry.get(),
                'Email': Email_Entry.get(),
                'Paper': Paper_Entry.get(),
                'Journal':Journal_Entry.get(),
                'Status':Status.get()
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
            my_tree.item(selected, text="", values=(ID_entry.get(),Name_Entry.get(), Surname_Entry.get(),Email_Entry.get(),Paper_Entry.get(),Journal_Entry.get(), Status.get(), ))
            
            conn = sqlite3.connect('Workflow.db')
            cursor = conn.cursor() 

            cursor.execute(""" UPDATE Articles SET
                        Name=:Name,
                        Surname=:Surname,
                        Email=:Email,
                        Paper=:Paper,
                        Journal=:Journal,
                        Status=:Status
                            
                        WHERE oid = :oid """,
                        {
                            'Name': Name_Entry.get(),
                            'Surname': Surname_Entry.get(),
                            'Email': Email_Entry.get(),
                            'Paper': Paper_Entry.get(),
                            'Journal':Journal_Entry.get(),
                            'Status': Status.get(),
                            'oid': ID_entry.get()
                        })

            conn.commit()
            conn.close()

            clearEntries()
            #clear entryboxes
            
        def clearEntries():
            Name_Entry.delete(0,END)
            Surname_Entry.delete(0,END)
            Email_Entry.delete(0,END)
            Paper_Entry.delete(0,END)
            Journal_Entry.delete(0,END)
            Status.delete(0,END)
            

        def lookup_record():
            x = search_entry.get()
            searchbox.destroy()
            #Clear treeview
            for i in my_tree.get_children():
                my_tree.delete(i)

            conn = sqlite3.connect('Workflow.db')
            cursor = conn.cursor()

            cursor.execute("SELECT rowid,* FROM Articles WHERE Name like ? OR Surname like ? OR Status like ?",(x,x,x,))

            records = cursor.fetchall()          

            for record in records:
                if record[6] == 'Writting':
                
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Writting',))

                elif record[6] == 'Editing':
                     my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Editing',))

                elif record[6] == 'Submitted':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Submitted',)) 

                elif record[6] == 'Accepted':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Accepted',))

                elif record[6] == 'Rejected':
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Rejected',))

                else:
                    my_tree.insert(parent='', index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('Published',))

        
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
            Paper_Entry.insert(0,values[4])
            Journal_Entry.insert(0,values[5])
            Status.insert(0,values[6])
            

        #Bind
        my_tree.bind("<ButtonRelease-1>",Selected)

        #######################################################################################################################
        # ################################################################################################################
        #                                                     Buttons
        ###################################################################################################################
        ###################################################################################################################

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
    Articles(window)
    window.mainloop()

if __name__ == '__main__':
    page()

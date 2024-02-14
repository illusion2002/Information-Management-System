from tkinter import*
from tkinter import ttk #module to provide access to TK themed widget set
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2
from tkcalendar import DateEntry
import tkinter as tk
import os 
import csv
from tkinter import filedialog

mydata=[]

class attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#size-x.axis-y.axis
        self.root.title("Face regonition system")
        
         ### variables declaration ###
        self.var_class = StringVar()
        self.var_section = StringVar()
        self.var_status = StringVar()
        self.var_atten = StringVar()
        self.var_roll= StringVar()
        self.var_name= StringVar()
        self.var_dep= StringVar()
        self.var_time= StringVar()
        self.var_date = StringVar()
        self.attendance_id = StringVar()

        
        #student registration 
        title_lbl=Label(text="ATTENDANCE SECTION",font=("times new roman",35,"bold"),bg="black",fg="white")#bgimg
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
    #Adding background image if you want 
        #img1 = Image.open(r"C:\Users\.....path......jpg")
        #img1 = img1.resize((1530,710),Image.LANCZOS )
        #self.photoimg1 = ImageTk.PhotoImage(img1)
        # bg_img = Label(self.root,image = self.photoimg1)
        #bg_img.place(x=0,y=45,width=1530,height=710)

#making frame 
        main_frame=Frame(bd=2) #bgimage add hane paxi change to (bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1530,height=790)
    
    #left side label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=700)  

     #left side label frame--current course
        current_course = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Attendance information",font=("times new roman",12,"bold"))
        current_course.place(x=10,y=10,width=720,height=150)
        
         #class combobox
        class_label = Label(current_course,text="Class",font=("times new roman",12,"bold"),bg="white")
        class_label.grid(row=0,column=0,padx=10)

        #combo box
        class_combo = ttk.Combobox(current_course,textvariable=self.var_class,font=("times new roman",12,"bold"),width=17,state="read only")
        class_combo["values"]=("Select Class","i","ii","iii","iv","v","vi","vii","viii","ix","x",)
        class_combo.current(0)
        class_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
    
     #Section Part
        section_label = Label(current_course,text="Section",font=("times new roman",12,"bold"),bg="white")
        section_label.grid(row=0,column=4,padx=10,pady=5,sticky=W)
        
        section_combo = ttk.Combobox(current_course,textvariable=self.var_section,font=("times new roman",12,"bold"),width=17,state="read only")
        section_combo["values"]=("Select Section","A","B")
        section_combo.current(0)
        section_combo.grid(row=0,column=5,padx=2,pady=5,sticky=W)
        #for manually entering section 
        # section_entry=ttk.Entry(current_course,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        # section_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

       #date Part
        date_label = Label(current_course,text="Date",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=1,column=0,padx=15,pady=5,sticky=W)

        # date_entry=ttk.Entry(current_course,textvariable=self.var_subject,width=20,font=("times new roman",12,"bold"))
        # date_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)
          # Use DateEntry instead of ttk.Entry for date entry
        cal = DateEntry(current_course, selectmode='day' , font=("times new roman", 12, "bold"))
        cal.grid(row=1, column=1, padx=2, pady=5, sticky="w")
         # Bind an event to capture date selection
        cal.bind("<<DateEntrySelected>>", self.get_selected_date)
    
   
   
       
  
        #Student Imformation
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Manage Attendance",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=160,width=720,height=500)  

        #attendance id
        attendanceID_entry = Label(class_student_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendanceID_entry.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendanceID_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten,width=20,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        #Student name
        student_name_label = Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

         #Roll Number
        roll_number_label = Label(class_student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        roll_number_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        roll_number_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_number_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        time_id_label = Label(class_student_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_id_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        timeID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_time,font=("times new roman",13,"bold"))
        timeID_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        date_id_label = Label(class_student_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_id_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        dateID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_date,font=("times new roman",13,"bold"))
        dateID_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        attendancestatusLabel = Label(class_student_frame,text = "Attendance Status",font=("times new roman",12,"bold"),bg = "white")
        attendancestatusLabel.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        self.atten_status = ttk.Combobox(class_student_frame,width=20,textvariable=self.attendance_id,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row = 4,column=1,pady = 8)
        self.atten_status.current(0)
        
        ######.........................................................................................................................................................................................
        #list button
        listbtn=Button(current_course,text="List All",command=self.fetch_data,font=("times now roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="grey",activeforeground="black",activebackground="silver")
        listbtn.grid(row=1,column=5,padx=5,pady=2,sticky=W)
       
  
       #Button Frame
        btn_frame = Frame(class_student_frame,bd=0,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=230,width=700,height=220)

        #Import CSV Button
        import_btn = Button(btn_frame,text="Import CSV",command=self.importCsv,width=70,font=("times new roman",13,"bold"),bg="black",fg="white",activeforeground="White",activebackground="silver")
        import_btn.grid(row=0,column=0,padx=5,pady=5)

        #Export CSV Button
        update_btn = Button(btn_frame,text="Export CSV",command=self.exportCsv,width=70,font=("times new roman",13,"bold"),bg="black",fg="white",activeforeground="white",activebackground="silver")
        update_btn.grid(row=1,column=0,padx=5,pady=5)

        #Import DB Button
        add_btn = Button(btn_frame,text="Import to Database",command=self.import_csv_to_mysql,width=70,font=("times new roman",13,"bold"),bg="white",fg="black",activeforeground="White",activebackground="silver")
        add_btn.grid(row=2,column=0,padx=5,pady=5)

        #Update Button
        delete_btn = Button(btn_frame,text="Update",width=70,font=("times new roman",13,"bold"),bg="grey",fg="white",activeforeground="black",activebackground="silver")
        delete_btn.grid(row=3,column=0,padx=5,pady=5)#command=self.delete_function,

        #Reset Button
        reset_btn = Button(btn_frame,text="Reset",width=70,font=("times new roman",13,"bold"),bg="grey",fg="white",activeforeground="black",activebackground="silver")
        reset_btn.grid(row=4,column=0,padx=5,pady=5)#,command=self.reset_data

         #right side label frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=710,height=700)

        # ####### Searching system #########
        # Search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        # Search_frame.place(x=10,y=10,width=680,height=70)  

        # Search_label = Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="grey",fg="white")
        # Search_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        # #search combo box
        # self.var_combo_search = StringVar()
        # search_combo = ttk.Combobox(Search_frame,textvariable=self.var_combo_search,font=("times new roman",12,"bold"),width=17,state="read only")
        # search_combo["values"]=("Select ","Roll","Name","Date","Time")
        # search_combo.current(0)
        # search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # self.var_search = StringVar()
        # search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        # search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        # search_btn = Button(Search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",13,"bold"),bg="Grey",fg="white")
        # search_btn.grid(row=0,column=3,padx=5,pady=5)
  
        ###########  Table Frame ##########

        Table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=10,y=100,width=680,height=550) 
 
  #Scroll Bar
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL) 
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL) 

        #self.student_table = ttk.Treeview(Table_frame,columns=("Class","Section","Name","Roll_no","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        self.student_table = ttk.Treeview(Table_frame,columns=("id","roll","name","class","section","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)      
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
      
        self.student_table.heading("id",text="ID")
        self.student_table.heading("roll",text="Roll")
        #self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("class",text="Class")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("Time",text="Time")
        self.student_table.heading("Date",text="Date")
        self.student_table.heading("Attendance",text="Attendance")
        self.student_table["show"] = "headings"

        self.student_table.column("id",width=100)
        self.student_table.column("roll",width=100)
        #self.student_table.column("ID",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("class",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("Time",width=100)
        self.student_table.column("Date",width=100)
        self.student_table.column("Attendance",width=100)
       
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
         #self.fetch_data()
        
    def get_selected_date(self, event):
            selected_date = event.widget.get_date()
            self.var_date.set(selected_date)

    def get_cursor(self,event=""):
            cursor_focus = self.student_table.focus()
            content = self.student_table.item(cursor_focus)  #item takes the content.
            data = content["values"]

            self.var_atten.set(data[0]),
            self.var_roll.set(data[1]),
            self.var_name.set(data[2]),
            self.var_class.set(data[3]),
            self.var_section.set(data[4]),
            self.var_time.set(data[5]),
            self.var_date.set(data[6]),
            self.attendance_id.set(data[7])   
        
    # def importDB(self):
    #    ()
    def reset_data(self):
        self.var_atten.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_class.set("")
        self.var_section.set(""),
        self.var_time.set("")
        self.var_date.set("")
        self.attendance_id.set("")

################################################searching data###########################################################
    # def search_data(self):
    #     if self.var_combo_search.get() == "" or self.var_search.get() == "":
    #         messagebox.showerror("Error", "Please select an option")
    #     else:
    #         try:
    #             conn = mysql.connector.connect(
    #                 host="localhost",
    #                 username="root",
    #                 password="qwerty123",
    #                 database="admin_minorproject"
    #             )
    #             my_cursor = conn.cursor()

    #             # Get the class value and section value from the variables
    #             class_value = self.var_class.get()
    #             section_value = self.var_section.get()

    #             # Construct the SQL query with filter conditions for class and section
    #             query = "SELECT * FROM student WHERE {} = %s AND Class = %s AND Section = %s".format(self.var_combo_search.get())

    #             # Pass the search value, class value, and section value as parameters to the execute method
    #             search_value = self.var_search.get()
    #             my_cursor.execute(query, (search_value, class_value, section_value))

    #             rows = my_cursor.fetchall()

    #             if len(rows) != 0:
    #                 self.student_table.delete(*self.student_table.get_children())
    #                 for row in rows:
    #                     self.student_table.insert("", END, values=row)
    #                 conn.commit()
    #             else:
    #                 messagebox.showinfo("No Data", "No matching records found")

    #         except mysql.connector.Error as e:
    #             messagebox.showerror("Error", f"Database error: {e}")

    #         except Exception as es:
    #             messagebox.showerror("Error", f"An error occurred: {es}")

    #         finally:
    #             if 'conn' in locals() and conn.is_connected():
    #                 my_cursor.close()
    #                 conn.close()

######################################fetch data from database############################################################### 
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="qwerty123",database="admin_minorproject")
            my_cursor = conn.cursor()

            # Get the string values from StringVar objects
            class_value = self.var_class.get()
            section_value = self.var_section.get()
            date_value= self.var_date.get()
            # Execute the SQL query with parameters
            my_cursor.execute("SELECT * FROM attendance WHERE class = %s AND section = %s AND date = %s",(class_value,section_value,date_value))

            data = my_cursor.fetchall()
            print(data)

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
                conn.commit()
        except mysql.connector.Error as e:
            print(f"Error fetching data: {e}")
        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()
        
        #### fetch data ###
    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)

    ##CSV file lai import gareko 
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter = ",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Function to import data from CSV to MySQL
    def import_csv_to_mysql(self):
        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='qwerty123',
                database='admin_minorproject'
            )
        
            cursor = conn.cursor()
            csv_file = 'attend.csv'
            table_name = 'attendance'
            # Read the CSV file
            with open(csv_file, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header row if it exists

                # Iterate over the CSV data and insert into the database
                for row in csv_reader:
                    query = f"INSERT INTO {table_name} (atten_id, roll, name, class,section,time,date,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(query, row)  # Assuming the order of columns in CSV matches the table

            # Commit the transaction
            conn.commit()
            messagebox.showinfo("IMPORT", "Successfully imported to database", parent=self.root)

        except mysql.connector.Error as err:
            print(f"MySQL error: {err}")

        finally:
            # Close the cursor and connection
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()
                
    def exportCsv(self):
                try:
                    if len(mydata)<1:
                        messagebox.showerror("No Data","NO Data found to export",parent = self.root)
                        return False
                    fln = filedialog.asksaveasfilename(initialdir = os.getcwd(),title = "Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)

                    with open(fln,mode = "w", newline="") as myFile:
                        exp_write = csv.writer(myFile,delimiter = ",")
                        for i in mydata:
                            exp_write.writerow(i)
                        messagebox.showinfo("Success","Your data has been successfully exported to"+os.path.basename(fln))
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

            
if __name__=="__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()


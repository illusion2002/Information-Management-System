from tkinter import*
from tkinter import ttk #module to provide access to TK themed widget set
from tkinter import messagebox
from PIL import Image,ImageTk

from msilib.schema import RadioButton
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#size-x.axis-y.axis
        self.root.title("Face regonition system")
        
         ### variables declaration ###
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_section = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

        #student registration 
        title_lbl=Label(text="ADMIN SECTION",font=("times new roman",35,"bold"),bg="black",fg="white")#bgimg
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
    #Adding background image
        #img1 = Image.open(r"C:\Users\.....path......jpg")
        #img1 = img1.resize((1530,710),Image.LANCZOS )
        #self.photoimg1 = ImageTk.PhotoImage(img1)
        # bg_img = Label(self.root,image = self.photoimg1)
        #bg_img.place(x=0,y=45,width=1530,height=710)

    #making frame 
        main_frame=Frame(bd=2) #bgimage add hane paxi change to (bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=40,width=1500,height=650)
    
    #left side label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=680)  


     #left side label frame--current course
        current_course = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=10,y=10,width=720,height=150)

     #Depatment combobox
        dep_label = Label(current_course,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        #combo box
        dep_combo = ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select department","Computer","Civil","Electronics","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
     #Year Combobox
        year_label = Label(current_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        
        year_combo = ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","First","Second","Third","Fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester Part
        sem_label = Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=4,padx=10)

        #combo box
        sem_combo = ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        sem_combo["values"]=("Select Semester","Odd","Even")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=5,padx=2,pady=10,sticky=W)

        #Student Imformation
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=160,width=720,height=490)  

        #student ID
        student_id_label = Label(class_student_frame,text="StudentId:",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        student_name_label = Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division
        section_label = Label(class_student_frame,text="Section:",font=("times new roman",12,"bold"),bg="white")
        section_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        

        section_combo = ttk.Combobox(class_student_frame,textvariable=self.var_section,font=("times new roman",12,"bold"),width=20,state="read only")
        section_combo["values"]=("Select Section","A","B")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

         #Roll Number
        roll_number_label = Label(class_student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        roll_number_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_number_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_number_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        Gender_label = Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=20,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Email
        email_label = Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone Number
        phone_number_label = Label(class_student_frame,text="Phone Number:",font=("times new roman",12,"bold"),bg="white")
        phone_number_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        phone_number_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_number_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Date of Birth
        DOB_label = Label(class_student_frame,text="D.O.B:",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label = Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=10,pady=10)
        
         
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn1.grid(row=5,column=1,padx=10,pady=10)

        #Button Frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=700,height=400)

        #Save Button
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=70,font=("times new roman",13,"bold"),bg="grey",fg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=5)

        #Update Button
        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=70,font=("times new roman",13,"bold"),bg="grey",fg="white")
        update_btn.grid(row=1,column=0,padx=5,pady=5)

        #Delete Button
        delete_btn = Button(btn_frame,text="Delete",command=self.delete_funtion,width=70,font=("times new roman",13,"bold"),bg="maroon",fg="white")
        delete_btn.grid(row=2,column=0,padx=5,pady=5)

        #Reset Button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=70,font=("times new roman",13,"bold"),bg="grey",fg="white")
        reset_btn.grid(row=3,column=0,padx=5,pady=5)
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn1.grid(row=5,column=1,padx=10,pady=10)
        
          #Take_photo Button
        Take_photo_btn = Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=70,font=("times new roman",13,"bold"),bg="grey",fg="white")
        Take_photo_btn.grid(row=5,column=0,padx=5,pady=5)

        #Update_photo Button
        Update_photo_btn = Button(btn_frame,text="Update Photo Sample",width=70,font=("times new roman",13,"bold"),bg="grey",fg="white")
        Update_photo_btn.grid(row=6,column=0,padx=5,pady=5)
        
          #right side label frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=710,height=680)  

        ######## Searching system ##########

        Search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        Search_frame.place(x=10,y=10,width=680,height=70)  

        Search_label = Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="grey",fg="white")
        Search_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)
     
           #search combo box
        self.var_combo_search = StringVar()
        search_combo = ttk.Combobox(Search_frame,textvariable=self.var_combo_search,font=("times new roman",12,"bold"),width=17,state="read only")
        search_combo["values"]=("Select ","Roll","Phone","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search = StringVar()
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        search_btn = Button(Search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",13,"bold"),bg="Grey",fg="white")
        search_btn.grid(row=0,column=3,padx=5,pady=5)

        show_all_btn = Button(Search_frame,command=self.fetch_data,text="Show All",width=12,font=("times new roman",13,"bold"),bg="Grey",fg="white")
        show_all_btn.grid(row=0,column=4,padx=5,pady=5)
        
         ###########  Table Frame ##########

        Table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=10,y=100,width=680,height=550) 
 
         #Scroll Bar
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL) 
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL) 

        self.student_table = ttk.Treeview(Table_frame,columns=("Dep","Year","Sem","ID","Name","Section","Roll_no","Gender","DOB","Phone_Number","Email","Address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Roll_no",text="Roll Number")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DateOfBirth")
        self.student_table.heading("Phone_Number",text="Phone Number")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Roll_no",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Phone_Number",width=100)
        self.student_table.column("Email",width=200)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

        ############# Function for Adding Data ##################

    def add_data(self):
        if self.var_dep.get()=="Select department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)   ##showing error if name and id empty
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="qwerty123",database="admin_minorproject")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
     
     
     
     
      ###### Fetching data from database ##########33
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="qwerty123",database="admin_minorproject")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        print(data)

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
 

      # ---------------->>> Update function <<<-----------

    def update_data(self):
        if self.var_dep.get()=="Select department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)   ##showing error if name and id empty

        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this student details", parent=self.root)
                if Update==True:
                    conn = mysql.connector.connect(host="localhost",username="root",password="qwerty123",database="admin_minorproject")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student set Dep=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_year.get(),
                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                        self.var_section.get(),
                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated.",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

   ## delete
    def delete_funtion(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student?",parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="qwerty123",database="admin_minorproject")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student",parent=self.root)
           
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    
    ############ RESET FUntion ###############

    def reset_data(self):
        
        
        self.var_dep.set("Select department")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_section.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_radio1.set("")


    ##################### Generating Dataset ####################

    def generate_dataset(self):
        if self.var_dep.get()=="Select department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)   ##showing error if name and id empty

        else:
            try:
                
                conn = mysql.connector.connect(host="localhost",username="root",password="qwerty123",database="admin_minorproject")
                my_cursor = conn.cursor()
                my_cursor.execute(" select * from student")
                my_result = my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("UPDATE student set Department=%s,Year=%s,Semester=%s,Name=%s,Section=%s,RollNumber=%s,Gender=%s,DOB=%s,PhoneNumber=%s,Email=%s,Address=%s,PhotoSample=%s where StudentId=%s",(

                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_year.get(),
                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                        self.var_section.get(),
                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                        self.var_std_id.get()==id+1
                                                                   
                                                                                                                                                             ))


                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                 ######## Loading faces by haarcascade ######3
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                #current working file ma bhako le nam matra deko natra full path dinu parxa"
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #min neighbour = 5
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                image_id = 0
                while True:
                    ret,frame = cap.read()
                    if face_cropped(frame) is not None:
                        image_id+=1
                        face = cv2.resize(face_cropped(frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user."+str(id)+"."+str(image_id)+".jpg"   
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(image_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(image_id)==200:
                        break
                cap.release()
                cv2.destroyAllWindows()        
                messagebox.showinfo("Result","Generating dataset completed!!")

            
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    
    #Search data
    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="qwerty123",database="admin_minorproject")
                my_cursor = conn.cursor()
                my_cursor.execute(" select * from student where "+str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows = my_cursor.fetchall()
                
                if len(rows)!= 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert('',END,values = i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # ------------------------->get cursor <---------------

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)  #item takes the content.
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_std_id.set(data[3]),
        self.var_std_name.set(data[4]),
        self.var_section.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_email.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])
    
        

if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
import cv2
import numpy as np
import os
from tkinter import Tk, Button, messagebox
from PIL import Image,ImageTk

class Training:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200")
        self.root.title("Face Recognition Training")

        b1_l = Button(
            self.root,
            text="Train Data",
            command=self.train_image,
            cursor="hand2",
            font=("times new roman", 20, "bold"),
            bg="maroon",
            fg="white",
        )
        b1_l.pack(pady=20)

 ########## Training images LBPH algorithm ################
    def train_image(self):
        data_dir = "data"
        path = [os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces = []
        ids = []
        
        for image in path:
            img= Image.open(image).convert('L')         ## Converting to grayscale
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)
        
        ########### Training classifier ##########3
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!")

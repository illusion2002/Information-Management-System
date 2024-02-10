import cv2
import os
import numpy as np
from tkinter import Tk, Button, messagebox

class Training:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200")
        self.root.title("Face Recognition Training")

        b1_l = Button(
            self.root,
            text="Train Data",
            command=self.train_classifier,
            cursor="hand2",
            font=("times new roman", 20, "bold"),
            bg="maroon",
            fg="white",
        )
        b1_l.pack(pady=20)

    def train_classifier(self):
        data_dir = "Data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
            imageNp = cv2.resize(img, (550, 550))
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

        ids = np.array(ids)

        # Train the classifier
        recognizer = cv2.face.LBPHFaceRecognizer_create() if cv2.__version__.startswith('3') else cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, ids)
        recognizer.save("classifier.yml")  

        messagebox.showinfo("Result", "Training Datasets Completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Training(root)
    root.mainloop()

from ast import main
import PIL
from customtkinter import filedialog
import customtkinter as ctk
from PIL import Image
import io
#import base64



class Application(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Image Enhancer")

        self.geometry("1280x720")

        self.minsize(1000, 600)

        ctk.set_appearance_mode("dark")
        self.img = None
        ctk.CTkButton(self, text="select image", command=self.ImageIN).pack(pady=20)

    def ImageIN(self): 
        imgpath = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])

    if ImageIN:
        self.img = Image.open(imgpath).copy()
        self.ImgUp = self.img.copy()

    def ImgOut(self):
        self.ImgUp.thumbnail((600, 400), Image.Resampling.LANCZOS)
        
         

        ctk.CTkImage(self, Image.open(self.ImgOut)) 
        size: (600, 400)
        

#            if 

#            else:
#                self.ImageOUT == None:
#                ctk.CTkLabel(self, text="No image selected").pack(pady=20)
            
            
              









































def main():
    app = Application()
    app.mainloop()



if __name__ == "__main__":
    main()
import Tkinter as tk
from Tkinter import Tk, RIGHT, BOTH, RAISED, Label, Radiobutton
from ttk import Frame, Button, Style
from PIL import Image, ImageTk
import tkFont

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
geoscreen = "%dx%d" % (screen_width, screen_height)

# print  tkFont.families()


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()

    
    def initUI(self):
      
        self.parent.title("Project Avocado")
        self.style = Style()

        # print self.style.theme_names() 'clam', 'alt', 'default', 'classic'
        self.style.theme_use("clam")

        self.pack(fill=BOTH, expand=1)

        self.style.configure("TFrame")
        
        logo = Image.open("logo.png")
        logow , logoh = logo.size
        logoObj = ImageTk.PhotoImage(logo)
        logoLabel = Label(self, image=logoObj)
        logoLabel.image = logoObj
        logoLabel.place(x = (screen_width - logow)/2, y = 0)

        shareButton = Button(self, text="Share",
                             command=self.create_ShareWin)
        shareButton.place(x = screen_width/4, y=screen_height/2)

        acceptButton = Button(self, text="Accept",
                              command=self.create_AcceptWin)
        acceptButton.place(x = screen_width/2, y=screen_height/2)
        
    def create_AcceptWin(self):
        acceptWin = tk.Toplevel(self)
        acceptWin.title('Accept Window')
        acceptWin.geometry(geoscreen)
        acceptWin.configure()

        submitButton = Button(acceptWin, text="Submit", command=acceptWin.destroy) 
        submitButton.pack()

    def create_ShareWin(self):
        shareWin = tk.Toplevel(self)
        shareWin.title('Accept Window')
        shareWin.geometry(geoscreen)
        shareWin.configure()


        menuLabel = Label(shareWin)
        menuLabel.config(text="Please select the appropriate options below")
        menuLabel.pack()

        Q1 = Label(shareWin)
        Q1.config(text="Please Choose your Food Type:")
        Q1.pack()

        Q1R1 = Radiobutton(shareWin, text="Meat", value="meat")
        Q1R1.pack()

        Q1R2 = Radiobutton(shareWin, text="Dairy", value="dairy")
        Q1R2.pack()

        Q1R3 = Radiobutton(shareWin, text="Baked", value="baked")
        Q1R3.pack()

        Q1R4 = Radiobutton(shareWin, text="Produce", value="produce")
        Q1R2.pack()

        Q1R5 = Radiobutton(shareWin, text="Non Preishable", value="non-perishable")
        Q1R5.pack()

        Q1R6 = Radiobutton(shareWin, text="Frozen", value="frozen")
        Q1R6.pack()

        Q1R7 = Radiobutton(shareWin, text="Other", value="other")
        Q1R7.pack()

        #=========================Second questions=====================
        Q2 = Label(shareWin)
        Q2.config(text="Select all the Dietary Options")
        Q2.pack()

        Q2R1 = Radiobutton(shareWin, text="Gluten Free", value="gluten-free")
        Q2R1.pack()

        Q2R2 = Radiobutton(shareWin, text="Tree Nut Free", value="tree nut free")
        Q2R2.pack()

        Q2R3 = Radiobutton(shareWin, text="Peanut Free", value="peanut free")
        Q2R3.pack()

        Q2R4 = Radiobutton(shareWin, text="Milk Free", value="milk free")
        Q2R2.pack()

        Q2R5 = Radiobutton(shareWin, text="Vegan", value="vegan")
        Q2R5.pack()

        Q2R6 = Radiobutton(shareWin, text="Kosher", value="kosher")
        Q2R6.pack()

        Q2R7 = Radiobutton(shareWin, text="Halal", value="halal")
        Q2R7.pack()

        Q2R8 = Radiobutton(shareWin, text="Other", value="other")
        Q2R8.pack()
        
        

        submitButton = Button(shareWin, text="Submit", command=shareWin.destroy) 
        submitButton.pack()
        


def main():
    # root.geometry("650x150+300+300")
    root.geometry(geoscreen)
    root.tk_setPalette(background='#fff', foreground='slate gray',
               activeBackground='slate gray')
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()

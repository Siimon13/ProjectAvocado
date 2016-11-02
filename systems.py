import Tkinter as tk
from Tkinter import Tk, RIGHT, BOTH, RAISED, Label
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

        self.style.configure("TFrame", background ="#333")
        
        logo = Image.open("logo.png")
        logow , logoh = logo.size
        logoObj = ImageTk.PhotoImage(logo)
        logoLabel = Label(self, image=logoObj)
        logoLabel.image = logoObj
        logoLabel.place(x = (screen_width - logow)/2, y = 0)

        shareButton = Button(self, text="Share",
            command=self.quit)
        shareButton.place(x = screen_width/4, y=screen_height/2)

        acceptButton = Button(self, text="Accept",
                              command=self.create_AcceptWin)
        acceptButton.place(x = screen_width/2, y=screen_height/2)
        
    def create_AcceptWin(self):
        acceptWin = tk.Toplevel(self)
        acceptWin.title('Accept Window')
        acceptWin.geometry("400x400")
        acceptWin.configure(background ="#333")

        submitButton = Button(acceptWin, text="Submit", command=acceptWin.destroy) 
        submitButton.pack()

        


def main():


    # root.geometry("650x150+300+300")
    root.geometry(geoscreen)
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()

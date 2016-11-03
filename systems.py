import Tkinter as tk
from Tkinter import Tk, RIGHT, BOTH, RAISED, Label, Radiobutton, StringVar
from ttk import *
from PIL import Image, ImageTk
import tkFont

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
geoscreen = "%dx%d" % (screen_width, screen_height)
# root.overrideredirect(1)
# print  tkFont.families()




class Example(Frame):
  
    class MyButton(Frame):
        def __init__(self, parent, height=None, width=None, text="", command=None, style=None):
            Frame.__init__(self, parent, height=height, width=width, style="MyButton.TFrame")

            self.pack_propagate(0)
            self._btn = Button(self, text=text, command=command, style=style)
            self._btn.pack(fill=tk.BOTH, expand=1)
            # self._btn.place(x = screen_width/2, y=screen_height/2)



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

        shareButton = self.MyButton(self, text="Share",
                             command=self.create_ShareWin, 
                                    width = 200, height=100)
        shareButton.place(x = screen_width/4, y=screen_height/2)
        # shareButton.grid(row=1,column=0)

        acceptButton = self.MyButton(self, text="Accept",
                              command=self.create_AcceptWin,
                              width = 200, height=100)
        acceptButton.place(x = screen_width/2, y=screen_height/2)
        # acceptButton.grid(row=6,column=2)

        quitButton = Button(self, text="Quit",
                              command=self.quit)
        # quitButton.grid(sticky=bottom)
        quitButton.pack()

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

        # shareWin.overrideredirect(1)
        menuLabel = Label(shareWin)
        menuLabel.config(text="Please select the appropriate options below")
        menuLabel.pack()

        Q1 = Label(shareWin)
        Q1.config(text="Please Choose your Food Type:")
        Q1.pack()

        # Q1R1 = Radiobutton(shareWin, text="Meat", value="meat")
        # Q1R1.pack()

        # Q1R2 = Radiobutton(shareWin, text="Dairy", value="dairy")
        # Q1R2.pack()

        # Q1R3 = Radiobutton(shareWin, text="Baked", value="baked")
        # Q1R3.pack()

        # Q1R4 = Radiobutton(shareWin, text="Produce", value="produce")
        # Q1R2.pack()

        # Q1R5 = Radiobutton(shareWin, text="Non Preishable", value="non-perishable")
        # Q1R5.pack()

        # Q1R6 = Radiobutton(shareWin, text="Frozen", value="frozen")
        # Q1R6.pack()

        # Q1R7 = Radiobutton(shareWin, text="Other", value="other")
        # Q1R7.pack()
        q1list = ['Meat', 'Dairy', 'Baked', 'Produce', 'Non Perishable', 'Frozen', 'Other']
        var1 = StringVar()
        drop1 = OptionMenu(shareWin, var1, *q1list)
        drop1.pack()

        #=========================Second questions=====================
        Q2 = Label(shareWin)
        Q2.config(text="Select all the Dietary Options")
        Q2.pack()

        # Q2R1 = Radiobutton(shareWin, text="Gluten Free", value="gluten-free")
        # Q2R1.pack()

        # Q2R2 = Radiobutton(shareWin, text="Tree Nut Free", value="tree nut free")
        # Q2R2.pack()

        # Q2R3 = Radiobutton(shareWin, text="Peanut Free", value="peanut free")
        # Q2R3.pack()

        # Q2R4 = Radiobutton(shareWin, text="Milk Free", value="milk free")
        # Q2R2.pack()

        # Q2R5 = Radiobutton(shareWin, text="Vegan", value="vegan")
        # Q2R5.pack()

        # Q2R6 = Radiobutton(shareWin, text="Kosher", value="kosher")
        # Q2R6.pack()

        # Q2R7 = Radiobutton(shareWin, text="Halal", value="halal")
        # Q2R7.pack()

        # Q2R8 = Radiobutton(shareWin, text="Other", value="other")
        # Q2R8.pack()
        q2list = ['Gluten Free', 'Tree Nut Free', 'Peanut Free', 'Milk Free', 'Vegan', 'Kosher', 'Halal' ,'Other']
        var2 = StringVar()
        drop2 = OptionMenu(shareWin, var2, *q2list)
        drop2.pack()
        

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

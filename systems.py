import Tkinter as tk
from Tkinter import Tk, RIGHT, BOTH, RAISED, Label, Radiobutton, StringVar, IntVar
from ttk import *
from PIL import Image, ImageTk
import tkFont

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
geoscreen = "%dx%d" % (screen_width, screen_height)

#Stores list of dics with keys descp, type, diet, allergen
localdb = []
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
        acceptButton.place(x = screen_width/4*2.5, y=screen_height/2)
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
        # acceptWin.overrideredirect(1)

        menuLabel = Label(acceptWin)
        menuLabel.config(text="Please select the food you want to take")
        menuLabel.pack()
        
        enable = {}
        checkbuts = {}
        for f in localdb:
            key = f['descp']
            enable[key] = IntVar()
            checkbuts[key] = Checkbutton(acceptWin, text='%s Food-Type:%s Diet:%s Allergens:%s' % tuple(f.values()), variable=enable[key])
            checkbuts[key].pack()

        def submitAccept():
            for e in enable:
                if enable[e].get() == 1:
                    checkbuts[key].destroy()
                    localdb[:] = [d for d in localdb if d['descp'] != key]
                    
            acceptWin.destroy()
        
        submitButton = Button(acceptWin, text="Submit", command=submitAccept) 
        submitButton.pack()

    def create_ShareWin(self):
        shareWin = tk.Toplevel(self)
        shareWin.title('Share Window')
        shareWin.geometry(geoscreen)
        shareWin.configure()
        # shareWin.overrideredirect(1)

        menuLabel = Label(shareWin)
        menuLabel.config(text="Please enter appropriate data below")
        menuLabel.pack()

        descLabel = Label(shareWin)
        descLabel.config(text="Enter a description of the item")
        descLabel.pack()
        
        descEntry = Entry(shareWin)
        descEntry.pack()
        
        Q1 = Label(shareWin)
        Q1.config(text="Please Choose your Food Type:")
        Q1.pack()

        q1list = ['Meat', 'Dairy', 'Baked', 'Produce', 'Non Perishable', 'Frozen', 'Other']
        var1 = StringVar()
        drop1 = OptionMenu(shareWin, var1, *q1list)
        drop1.pack()

        #=========================Second questions=====================
        Q2 = Label(shareWin)
        Q2.config(text="Select all the Dietary Options")
        Q2.pack()
        q2list = ['None','Gluten Free', 'Lactose Free', 'Vegan', 'Kosher', 'Halal' ,'Other']
        var2 = StringVar()
        drop2 = OptionMenu(shareWin, var2, *q2list)
        drop2.pack()
        
        #=========================Second questions=====================
        Q3 = Label(shareWin)
        Q3.config(text="Select all possible Allergen")
        Q3.pack()
        q3list = ['None', 'Tree Nut', 'Peanut', 'Lactose', 'Other']
        var3 = StringVar()
        drop3 = OptionMenu(shareWin, var3, *q3list)
        drop3.pack()
        
        def submitFood():
            localdb.append({'descp':descEntry.get(),
                            'type':var1.get(),
                            'diet':var2.get(),
                            'allergen':var3.get()})
            shareWin.destroy()

        submitButton = Button(shareWin, text="Submit", command=submitFood) 
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


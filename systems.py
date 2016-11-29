import Tkinter as tk
from Tkinter import Tk, RIGHT,TOP, LEFT, BOTTOM, BOTH, RAISED, Label, Radiobutton, StringVar, IntVar, Frame, SUNKEN
import tkFont
from ttk import Button, Style, Frame, Entry, OptionMenu, Checkbutton
from PIL import Image, ImageTk
import tkFont
import csv

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


geoscreen = "%dx%d" % (screen_width, screen_height)

#Stores list of dics with keys descp, type, diet, allergen
localdb = []
iddb = []
foodList = {}

# root.overrideredirect(1)
# print  tkFont.families()

#Globals to keep track of the button Clicks
#Food Types
packagedClicked = False
frozenClicked = False
bakedClicked = False
produceClicked = False
dairyClicked = False
meatClicked = False

foodtypeDic = {'Meat': meatClicked,
               'Dairy': dairyClicked,
               'Produce': produceClicked,
               'Baked' : bakedClicked,
               'Frozen' : frozenClicked,
               'Packaged' : packagedClicked}
#Allergens
wheatAClicked = False
soyaAClicked = False
peanutsAClicked = False
nutsAClicked = False
shellfishAClicked = False
milkAClicked = False
fishAClicked = False
eggAClicked = False

allergenDic = {'Egg' : eggAClicked,
               'Fish' : fishAClicked,
               'Milk' : milkAClicked,
               'Nuts' : nutsAClicked,
               'Peanuts' : peanutsAClicked,
               'Soya' : soyaAClicked,
               'Wheat' : wheatAClicked,
               'Shellfish' : shellfishAClicked}

def clearDic():
    for f in allergenDic:
        allergenDic[f] = False
    for f in foodtypeDic:
        foodtypeDic[f] = False

def writeToCSV():
    with open('ID' + '.csv', 'w') as mycsvfile:
     thedatawriter = csv.writer(mycsvfile)
     for row in iddb:
         thedatawriter.writerow(row)


    with open('Food' + '.csv', 'w') as mycsvfile:
     thedatawriter = csv.writer(mycsvfile)
     for row in localdb:
         thedatawriter.writerow(row)

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

        self.style.configure("TFrame", background='#1BA',
                             font=("Helvetica","18"), foreground="white")
        self.style.configure("TButton", font=("Helvetica","100"), 
                             foreground="white",background="purple")
        self.style.configure("TLabel", font=("Helvetica","18"), 
                             foreground="white")
        self.style.configure("TCheckbutton", font=("Helvetica","18"), 
                             background="#1BA",foreground="white")


        self.style.configure("share.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")


        logo = Image.open("logo.png")
        logow , logoh = logo.size
        logoObj = ImageTk.PhotoImage(logo)
        logoLabel = Label(self, image=logoObj)
        logoLabel.image = logoObj
        logoLabel.place(x = (screen_width - logow)/2, y = 0)

        shareButton = self.MyButton(self, text="Give",
                                    command=self.create_ShareWin, 
                                    width = screen_width/2, 
                                    height=screen_height/2
        )

        shareButton.place(x = 0, y=screen_height/2)
        # shareButton.grid(row=1,column=0)

        acceptButton = self.MyButton(self, text="Accept",
                                     command=self.create_AcceptWin,
                                     width = screen_width/2, 
                                     height=screen_height/2)
        acceptButton.place(x = screen_width/2, y=screen_height/2+5)
        # acceptButton.grid(row=6,column=2)

        # quitButton = Button(self, text="Quit",
        #                       command=self.quit)
        # quitButton.grid(sticky=bottom)
        # quitButton.pack()

    def create_AcceptWin(self):
        acceptWin = tk.Toplevel(self)
        acceptWin.title('Accept Window')
        acceptWin.geometry(geoscreen)
        acceptWin.configure()
        # acceptWin.overrideredirect(1)

        menuLabel = Label(acceptWin)
        menuLabel.config(text="Thank You", fg="white", font=("Helvetica", 48))
        menuLabel.pack()
        
        idText = Label(acceptWin, text="Do you want updates? Please enter your netid:", fg="white", font=("Helvetica", 16))
        idText.pack()

        idvar = StringVar()
        idE = Entry(acceptWin, textvariable=idvar)

        idE.pack()

        
        def submitAccept():
            if len(idvar.get()) > 0: iddb.append([idvar.get()])

            print localdb
            print iddb
            writeToCSV()

            acceptWin.destroy()
        
        self.style.configure("accept.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        submitButton = Button(acceptWin, text="Done", command=submitAccept,
                              style="accept.TButton") 
        submitButton.pack()

    def create_ShareWin(self):
        shareWin = tk.Toplevel(self)
        shareWin.title('Share Window')
        shareWin.geometry(geoscreen)
        shareWin.configure()
        # shareWin.overrideredirect(1)

        menuLabel = Label(shareWin)
        menuLabel.config(text="Please select all that apply", 
                         font=("Helvetica",18), foreground="white")
        menuLabel.grid(row=0, column= 1)



        
        Q1 = Label(shareWin)
        Q1.config(text="Food Type", 
                         font=("Helvetica",24), foreground="white")
        Q1.grid(row=1, column=0)

        def pressM():
            global foodtypeDic

            foodtypeDic['Meat'] = not foodtypeDic['Meat']

            if foodtypeDic['Meat']:
                self.style.configure("meat.TButton", background="gray")
            else:
                self.style.configure("meat.TButton", background="purple")


        self.style.configure("meat.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        meatButton = self.MyButton(shareWin, text="Meat",
                                   width = screen_width/10, 
                                   height=screen_height/10,
                                   style="meat.TButton",
                                   command=pressM)

        meatButton.grid(row=2, column=0, pady=5)


        def pressD():
            global foodtypeDic

            foodtypeDic['Dairy'] = not foodtypeDic['Dairy']

            if foodtypeDic['Dairy']:
                self.style.configure("dairy.TButton", background="gray")
            else:
                self.style.configure("dairy.TButton", background="purple")


        self.style.configure("dairy.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        dairyButton = self.MyButton(shareWin, text="Dairy",
                                   width = screen_width/10, 
                                   height=screen_height/10,
                                    style="dairy.TButton",
                                    command = pressD)
        dairyButton.grid(row=3, column=0, pady=5)


        def pressP():
            global foodtypeDic

            foodtypeDic['Produce'] = not foodtypeDic['Produce']

            if foodtypeDic['Produce']:
                self.style.configure("produce.TButton", background="gray")
            else:
                self.style.configure("produce.TButton", background="purple")


        self.style.configure("produce.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        produceButton = self.MyButton(shareWin, text="Produce",
                                      width = screen_width/10, 
                                      height=screen_height/10,
                                      style="produce.TButton",
                                      command = pressP)
        produceButton.grid(row=4, column=0, pady=5)

        def pressB():
            global foodtypeDic

            foodtypeDic['Baked'] = not foodtypeDic['Baked']

            if foodtypeDic['Baked']:
                self.style.configure("baked.TButton", background="gray")
            else:
                self.style.configure("baked.TButton", background="purple")


        self.style.configure("baked.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        bakedButton = self.MyButton(shareWin, text="Baked",
                                    width = screen_width/10, 
                                    height=screen_height/10,
                                    style="baked.TButton",
                                    command = pressB)
        bakedButton.grid(row=5, column=0, pady=5)

        def pressF():
            global foodtypeDic

            foodtypeDic['Frozen'] = not foodtypeDic['Frozen']

            if foodtypeDic['Frozen']:
                self.style.configure("frozen.TButton", background="gray")
            else:
                self.style.configure("frozen.TButton", background="purple")


        self.style.configure("frozen.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        frozenButton = self.MyButton(shareWin, text="Frozen",
                                   width = screen_width/10, 
                                   height=screen_height/10,
                                     style="frozen.TButton",
                                     command=pressF)
        frozenButton.grid(row=6, column=0, pady=5)

        def pressPack():
            global foodtypeDic

            foodtypeDic['Packaged'] = not foodtypeDic['Packaged']

            if allergenDic['Packaged']:
                self.style.configure("packaged.TButton", background="gray")
            else:
                self.style.configure("packaged.TButton", background="purple")


        self.style.configure("packaged.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")
        
        packagedButton = self.MyButton(shareWin, text="Packaged",
                                       width = screen_width/10, 
                                       height=screen_height/10,
                                       style="packaged.TButton",
                                       command=pressPack)
        packagedButton.grid(row=7, column=0, pady=5)


        Q2 = Label(shareWin)
        Q2.config(text="Possible Allergens", 
                         font=("Helvetica",24), foreground="white")
        Q2.grid(row=1, column=2)


        def pressEggA():
            global allergenDic

            allergenDic['Egg'] = not allergenDic['Egg']

            if allergenDic['Egg']:
                self.style.configure("egg.TButton", background="gray")
            else:
                self.style.configure("egg.TButton", background="purple")


        self.style.configure("egg.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")
        
        eggButton = self.MyButton(shareWin, text="Egg",
                                   width = screen_width/15, 
                                   height=screen_height/15,
                                   style="egg.TButton",
                                  command=pressEggA)
        eggButton.grid(row=2, column=2, pady=2)

        def pressFishA():
            global allergenDic

            allergenDic['Fish'] = not allergenDic['Fish']

            if allergenDic['Fish']:
                self.style.configure("fish.TButton", background="gray")
            else:
                self.style.configure("fish.TButton", background="purple")


        self.style.configure("fish.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")


        fishButton = self.MyButton(shareWin, text="Fish",
                                   width = screen_width/15, 
                                   height=screen_height/15,
                                   style="fish.TButton",
                                   command=pressFishA)
        fishButton.grid(row=3, column=2, pady=2)

        def pressMilkA():
            global allergenDic

            allergenDic['Milk'] = not allergenDic['Milk']

            if allergenDic['Milk']:
                self.style.configure("milk.TButton", background="gray")
            else:
                self.style.configure("milk.TButton", background="purple")


        self.style.configure("milk.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        milkButton = self.MyButton(shareWin, text="Milk",
                                   width = screen_width/15, 
                                   height=screen_height/15,
                                   style="milk.TButton",
                                   command=pressMilkA)
        milkButton.grid(row=4, column=2, pady=2)

        def pressNutsA():
            global allergenDic

            allergenDic['Nuts'] = not allergenDic['Nuts']

            if allergenDic['Nuts']:
                self.style.configure("nuts.TButton", background="gray")
            else:
                self.style.configure("nuts.TButton", background="purple")


        self.style.configure("nuts.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        nutsButton = self.MyButton(shareWin, text="Nuts",
                                   width = screen_width/15, 
                                   height=screen_height/15,
                                   style="nuts.TButton",
                                   command=pressNutsA)
        nutsButton.grid(row=5, column=2, pady=2)

        def pressPeanutsA():
            global allergenDic

            allergenDic['Peanuts'] = not allergenDic['Peanuts']

            if allergenDic['Peanuts']:
                self.style.configure("peanuts.TButton", background="gray")
            else:
                self.style.configure("peanuts.TButton", background="purple")


        self.style.configure("peanuts.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        peanutsButton = self.MyButton(shareWin, text="Peanuts",
                                      width = screen_width/15, 
                                      height=screen_height/15,
                                      style="peanuts.TButton",
                                      command=pressPeanutsA)
        peanutsButton.grid(row=6, column=2, pady=2)

        def pressShellfishA():
            global allergenDic

            allergenDic['Shellfish'] = not allergenDic['Shellfish']

            if allergenDic['Shellfish']:
                self.style.configure("shellfish.TButton", background="gray")
            else:
                self.style.configure("shellfish.TButton", background="purple")


        self.style.configure("shellfish.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        shellfishButton = self.MyButton(shareWin, text="Shellfish",
                                        width = screen_width/15, 
                                        height=screen_height/15,
                                        style="shellfish.TButton",
                                        command=pressShellfishA)
        shellfishButton.grid(row=2, column=3, pady=2)

        def pressSoyaA():
            global allergenDic

            allergenDic['Soya'] = not allergenDic['Soya']

            if allergenDic['Soya']:
                self.style.configure("soya.TButton", background="gray")
            else:
                self.style.configure("soya.TButton", background="purple")


        self.style.configure("soya.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")


        soyaButton = self.MyButton(shareWin, text="Soya",
                                   width = screen_width/15, 
                                   height=screen_height/15,
                                   style="soya.TButton",
                                   command=pressSoyaA)
        soyaButton.grid(row=3, column=3, pady=2)

        def pressWheatA():
            global allergenDic

            allergenDic['Wheat'] = not allergenDic['Wheat']

            if allergenDic['Wheat']:
                self.style.configure("wheat.TButton", background="gray")
            else:
                self.style.configure("wheat.TButton", background="purple")


        self.style.configure("wheat.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        wheatButton = self.MyButton(shareWin, text="Wheat",
                                    width = screen_width/15, 
                                    height=screen_height/15,
                                    style="wheat.TButton",
                                    command=pressWheatA)
        wheatButton.grid(row=4, column=3, pady=2)

        
        def submitFood():
            global foodtypeDic, allergenDic, foodList
            
            typestr = "Type: "
            for f in foodtypeDic:
                if foodtypeDic[f]:
                    typestr += f + " "
                    
            allergenstr = "Allergen: "
            for f in allergenDic :
                if allergenDic[f]:
                    allergenstr += f + " "
                
            localdb.append([typestr,allergenstr])

            clearDic()
            if len(idvar.get()) > 0: iddb.append([idvar.get()])

            print localdb
            print iddb

            writeToCSV()


            shareWin.destroy()

        # updatevar = StringVar()
        
        # emailCheck = Checkbutton(shareWin ,variable=updatevar, 
        #                          text="Do you want updates? Enter yo")

        # emailCheck.grid(row=12,column=1)

        idText = Label(shareWin, text="Do you want updates? Please enter your netid:", fg="white", font=("Helvetica", 16))
        idText.grid(row=12, column=1)

        idvar = StringVar()
        idE = Entry(shareWin, textvariable=idvar)

        idE.grid(row=13, column=1)
        
        submitButton = Button(shareWin, text="Submit", command=submitFood) 
        submitButton.grid(row=14, column=1)
        

def main():
    root.geometry(geoscreen)
    root.tk_setPalette(background='#1BA', foreground='slate gray',
               activeBackground='slate gray')

    app = Example(root)

    root.mainloop()  


if __name__ == '__main__':
    main()


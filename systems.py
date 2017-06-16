import Tkinter as tk
import ttk
from Tkinter import Tk, RIGHT,TOP, LEFT, BOTTOM, BOTH, RAISED, Label, Radiobutton, StringVar, IntVar, Frame, SUNKEN
import tkFont
from ttk import Style, Frame, Entry, OptionMenu, Checkbutton, Button
from PIL import Image, ImageTk
import tkFont
import csv
import subprocess
from datetime import datetime

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def activateKeyboard(event):
    subprocess.call("./keyboard.sh", shell=True)

def deactivateKeyboard():
    subprocess.call("./kill.sh", shell=True)

geoscreen = "%dx%d" % (screen_width, screen_height)

#Stores list of dics with keys descp, type, diet, allergen
localdb = []
iddb = []
scandb = []
foodList = {}
accepts = 0
shares = 0

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
    with open('ID.csv', 'w') as mycsvfile:
     thedatawriter = csv.writer(mycsvfile)
     for row in iddb:
         thedatawriter.writerow(row)

    with open('SCAN.csv', 'w') as mycsvfile:
     thedatawriter = csv.writer(mycsvfile)
     for row in scandb:
         thedatawriter.writerow(row)


    with open('Food.csv', 'w') as mycsvfile:
     thedatawriter = csv.writer(mycsvfile)
     for row in localdb:
         thedatawriter.writerow(row)

class Example(Frame):

    
    class MyButton(Frame):
        def __init__(self, parent, height=None, width=None, text="", command=None, style=None):
            Frame.__init__(self, parent, height=height, width=width, style="MyButton.TFrame")

            self.pack_propagate(0)
            self._btn = ttk.Button(self, text=text, command=command, style=style)
            self._btn.config()
            self._btn.pack(fill=tk.BOTH, expand=1)
            # self._btn.place(x = screen_width/2, y=screen_height/2)


    def __init__(self, parent):
        Frame.__init__(self, parent)   
        
        self.parent = parent
        
        self.initUI()

    
    def initUI(self):
        
        self.menuWin = self.parent
        self.menuWin.title('Main Window')
        self.menuWin.geometry(geoscreen)
        self.menuWin.configure()
        self.style = Style()

        self.style.configure("menu.TButton", font=("Helvetica","24"),foreground="white",background="purple")

        
        logo = Image.open("logo.png")
        logow , logoh = logo.size
        logoObj = ImageTk.PhotoImage(logo)
        logoLabel = Label(self.menuWin, image=logoObj)
        logoLabel.image = logoObj
        logoLabel.place(x = (screen_width - logow)/2, y = 0)

        logoLabel = Label(self.menuWin)
        logoLabel.config(text="NYU Freedge", fg="purple", font=("Helvetica","50" ))
        logoLabel.place(relx=.5, rely=.3, anchor="center")

        shareButton = self.MyButton(self.menuWin, text="Give Food",
                                    command=self.create_ShareWin, 
                                    width = screen_width/2.5, 
                                    height=screen_height/2.5,
                                    style="menu.TButton"
            )

        shareButton.place(x = 20, y=screen_height/2)


        acceptButton = self.MyButton(self.menuWin, text="Take Food",
                                         command=self.create_AcceptWin,
                                         width = screen_width/2.5, 
                                         height=screen_height/2.5,
                                            style="menu.TButton")
        acceptButton.place(x = screen_width/2, y=screen_height/2)
        
    def create_AcceptWin(self):
        global accepts

        #self.menuWin.destroy()
        
        accepts += 1
        print 'Number of Accepts: %d' % accepts
        acceptWin = tk.Toplevel(self)
        acceptWin.title('Accept Window')
        acceptWin.geometry(geoscreen)
        acceptWin.configure()
        # acceptWin.overrideredirect(1)

        menuLabel = Label(acceptWin)
        menuLabel.config(text="Thank You", fg="purple", font=("Helvetica", 48))
        menuLabel.pack()

        def submitAccept():
            if len(idvar.get()) > 0: iddb.append([idvar.get()])

            writeToCSV()
            deactivateKeyboard()
            acceptWin.destroy()

        self.style.configure("accept.TButton", font=("Helvetica","24"),
                             foreground="white",background="purple")

        submitButton = Button(acceptWin, text="Done", command=submitAccept,
                              style="accept.TButton") 
        submitButton.pack(side=BOTTOM)

        idvar = StringVar()
        idE = Entry(acceptWin, textvariable=idvar)
        idE.bind("<FocusIn>",activateKeyboard)
        idE.pack(side=BOTTOM)

        idText = Label(acceptWin, text="Do you want updates? Please enter your netid:", fg="purple", font=("Helvetica", 16))
        idText.pack(side=BOTTOM)
            


    def create_ShareWin(self):
        global shares

        #self.menuWin.destroy()
        shares += 1
        print 'Number of Shares: %d' % shares
        shareWin = tk.Toplevel(self)
        shareWin.title('Share Window')
        shareWin.geometry(geoscreen)
        shareWin.configure()
        # shareWin.overrideredirect(1)

        menuLabel = Label(shareWin)
        menuLabel.config(text="Please select all that apply", 
                         font=("Helvetica",14), foreground="purple")
        menuLabel.grid(row=0, column= 1)




        Q1 = Label(shareWin)
        Q1.config(text="Food Type", 
                         font=("Helvetica",16), foreground="purple")
        Q1.grid(row=1, column=0)

        def pressM():
            global foodtypeDic

            foodtypeDic['Meat'] = not foodtypeDic['Meat']

            if foodtypeDic['Meat']:
                self.style.configure("meat.TButton", background="green")
            else:
                self.style.configure("meat.TButton", background="purple")


        self.style.configure("meat.TButton", font=("Helvetica","14"),
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
                self.style.configure("dairy.TButton", background="green")
            else:
                self.style.configure("dairy.TButton", background="purple")


        self.style.configure("dairy.TButton", font=("Helvetica","14"),
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
                self.style.configure("produce.TButton", background="green")
            else:
                self.style.configure("produce.TButton", background="purple")


        self.style.configure("produce.TButton", font=("Helvetica","14"),
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
                self.style.configure("baked.TButton", background="green")
            else:
                self.style.configure("baked.TButton", background="purple")


        self.style.configure("baked.TButton", font=("Helvetica","14"),
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
                self.style.configure("frozen.TButton", background="green")
            else:
                self.style.configure("frozen.TButton", background="purple")


        self.style.configure("frozen.TButton", font=("Helvetica","14"),
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
                self.style.configure("packaged.TButton", background="green")
            else:
                self.style.configure("packaged.TButton", background="purple")


        self.style.configure("packaged.TButton", font=("Helvetica","14"),
                             foreground="white",background="purple")

        packagedButton = self.MyButton(shareWin, text="Packaged",
                                       width = screen_width/10, 
                                       height=screen_height/10,
                                       style="packaged.TButton",
                                       command=pressPack)
        packagedButton.grid(row=7, column=0, pady=5)


        Q2 = Label(shareWin)
        Q2.config(text="Possible Allergens", 
                         font=("Helvetica",16), foreground="white")
        Q2.grid(row=1, column=2)


        def pressEggA():
            global allergenDic

            allergenDic['Egg'] = not allergenDic['Egg']

            if allergenDic['Egg']:
                self.style.configure("egg.TButton", background="green")
            else:
                self.style.configure("egg.TButton", background="purple")


        self.style.configure("egg.TButton", font=("Helvetica","14"),
                             foreground="white",background="purple")

        eggButton = self.MyButton(shareWin, text="Egg",
                                  width = screen_width/10, 
                                  height=screen_height/10,
                                  style="egg.TButton",
                                  command=pressEggA)
        eggButton.grid(row=2, column=2, pady=2)

        def pressFishA():
            global allergenDic

            allergenDic['Fish'] = not allergenDic['Fish']

            if allergenDic['Fish']:
                self.style.configure("fish.TButton", background="green")
            else:
                self.style.configure("fish.TButton", background="purple")


        self.style.configure("fish.TButton", font=("Helvetica","14"),
                             foreground="white",background="purple")


        fishButton = self.MyButton(shareWin, text="Fish",
                                   width = screen_width/10, 
                                   height=screen_height/10,
                                   style="fish.TButton",
                                   command=pressFishA)
        fishButton.grid(row=3, column=2, pady=2)

        def pressMilkA():
            global allergenDic

            allergenDic['Milk'] = not allergenDic['Milk']

            if allergenDic['Milk']:
                self.style.configure("milk.TButton", background="green")
            else:
                self.style.configure("milk.TButton", background="purple")


        self.style.configure("milk.TButton", font=("Helvetica","14"),
                             foreground="white",background="purple")

        milkButton = self.MyButton(shareWin, text="Milk",
                                   width = screen_width/10, 
                                   height=screen_height/10,
                                   style="milk.TButton",
                                   command=pressMilkA)
        milkButton.grid(row=4, column=2, pady=2)

        def pressNutsA():
            global allergenDic

            allergenDic['Nuts'] = not allergenDic['Nuts']

            if allergenDic['Nuts']:
                self.style.configure("nuts.TButton", background="green")
            else:
                self.style.configure("nuts.TButton", background="purple")


        self.style.configure("nuts.TButton", font=("Helvetica","14"),
                             foreground="white",background="purple")

        nutsButton = self.MyButton(shareWin, text="Nuts",
                                   width = screen_width/10, 
                                   height=screen_height/10,
                                   style="nuts.TButton",
                                   command=pressNutsA)
        nutsButton.grid(row=5, column=2, pady=2)

        def pressPeanutsA():
            global allergenDic

            allergenDic['Peanuts'] = not allergenDic['Peanuts']

            if allergenDic['Peanuts']:
                self.style.configure("peanuts.TButton", background="green")
            else:
                self.style.configure("peanuts.TButton", background="purple")


        self.style.configure("peanuts.TButton", font=("Helvetica","12"),
                             foreground="white",background="purple")

        peanutsButton = self.MyButton(shareWin, text="Peanuts",
                                      width = screen_width/10, 
                                      height=screen_height/10,
                                      style="peanuts.TButton",
                                      command=pressPeanutsA)
        peanutsButton.grid(row=6, column=2, pady=2)

        def pressShellfishA():
            global allergenDic

            allergenDic['Shellfish'] = not allergenDic['Shellfish']

            if allergenDic['Shellfish']:
                self.style.configure("shellfish.TButton", background="green")
            else:
                self.style.configure("shellfish.TButton", background="purple")


        self.style.configure("shellfish.TButton", font=("Helvetica","10"),
                             foreground="white",background="purple")

        shellfishButton = self.MyButton(shareWin, text="Shellfish",
                                        width = screen_width/10, 
                                        height=screen_height/10,
                                        style="shellfish.TButton",
                                        command=pressShellfishA)
        shellfishButton.grid(row=2, column=3, pady=2)

        def pressSoyaA():
            global allergenDic

            allergenDic['Soya'] = not allergenDic['Soya']

            if allergenDic['Soya']:
                self.style.configure("soya.TButton", background="green")
            else:
                self.style.configure("soya.TButton", background="purple")


        self.style.configure("soya.TButton", font=("Helvetica","14"),
                             foreground="white",background="purple")


        soyaButton = self.MyButton(shareWin, text="Soya",
                                   width = screen_width/10, 
                                   height=screen_height/10,
                                   style="soya.TButton",
                                   command=pressSoyaA)
        soyaButton.grid(row=3, column=3, pady=2)

        def pressWheatA():
            global allergenDic

            allergenDic['Wheat'] = not allergenDic['Wheat']

            if allergenDic['Wheat']:
                self.style.configure("wheat.TButton", background="green")
            else:
                self.style.configure("wheat.TButton", background="purple")


        self.style.configure("wheat.TButton", font=("Helvetica","14"),
                             foreground="white",background="purple")

        wheatButton = self.MyButton(shareWin, text="Wheat",
                                    width = screen_width/10, 
                                    height=screen_height/10,
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

            writeToCSV()

            deactivateKeyboard()
            shareWin.destroy()

        # updatevar = StringVar()

        # emailCheck = Checkbutton(shareWin ,variable=updatevar, 
        #                          text="Do you want updates? Enter yo")

        # emailCheck.grid(row=12,column=1)

        idText = Label(shareWin, text="Do you want updates? Please enter your netid:", fg="purple", font=("Helvetica", 12))
        idText.grid(row=6, column=1)



        idvar = StringVar()
        idE = Entry(shareWin, textvariable=idvar)
        idE.bind("<FocusIn>",activateKeyboard)
        idE.grid(row=7, column=1)


        self.style.configure("submit.TButton", font=("Helvetica","14"),
                             foreground="white",background="purple")

        submitButton = self.MyButton(shareWin, text="Submit",
                                     width = screen_width/10, 
                                     height=screen_height/10,
                                     command=submitFood,
                                     style='submit.TButton') 
        submitButton.grid(row=8, column=1)


def main():
    root.geometry(geoscreen) 
    root.tk_setPalette(background='white', foreground='slate gray',
               activeBackground='slate gray')

    app = Example(root)

    root.mainloop()  


if __name__ == '__main__':
    main()


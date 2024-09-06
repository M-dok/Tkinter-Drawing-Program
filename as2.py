import tkinter as tk 
from tkinter import messagebox

class DrawingApp(object):
    def __init__(self):
        self._root = tk.Tk()
        self._root.geometry("900x600")
        self._root.title("Drawing")
        
        self._colour = '' 
        self._shape = '' 
        self._event1 = None 
        self._event2 = None
        self._clickCounter = 0 

        self._left_frame = tk.Frame(self._root,width=260,height=600,background="orange")
        self._left_frame.grid(row=0,column=0,padx=2)
        self._left_frame.grid_propagate(False)

        self._right_frame = tk.Frame(self._root,width=640,height=600,background="grey")
        self._right_frame.grid(row=0,column=150,padx=2)
        self._right_frame.grid_propagate(False)

        self._MyCanvas = tk.Canvas(self._right_frame,highlightbackground="black",width=640,height=600,bg="white")
        self._MyCanvas.grid(row=0,column=150,padx=3)
        #Colours
        self._cTitle = tk.Label(self._left_frame,text="Colours",font=18).grid(row=0,column=0) 
        self._colour1_btn = tk.Button(self._left_frame, text="red",command=lambda:self.SetColour("red")).grid(row=20,column=0,pady=5,padx=10)
        self._colour2_btn = tk.Button(self._left_frame, text="yellow",command=lambda:self.SetColour("yellow")).grid(row=40,column=0,pady=5)
        self._colour3_btn = tk.Button(self._left_frame, text="blue",command=lambda:self.SetColour("blue")).grid(row=60,column=0,pady=5)
        #Shape
        self._sTitle = tk.Label(self._left_frame,text="Shapes",font=18,highlightbackground="black").grid(row=100,column=0,pady=5) 
        self._shape1_btn = tk.Button(self._left_frame, text="oval",command=lambda:self.SetShape("oval")).grid(row=120,column=0,pady=5)
        self._shape2_btn = tk.Button(self._left_frame, text="rectangle",command=lambda:self.SetShape("rectangle")).grid(row=140,column=0,pady=5)
        self._shape3_btn = tk.Button(self._left_frame, text="line",command=lambda:self.SetShape("line")).grid(row=160,column=0,pady=5)
        


        self._UserChoiceVar = tk.StringVar()
        self._UserChoice = tk.Label(self._left_frame,textvariable=self._UserChoiceVar,justify="center").grid(row=200,column=0,pady=5,padx=10)
        self._UserChoiceVar.set(f'''To Draw on canvas 
        select colour and shape''')

        self._rbtn = tk.Button(self._left_frame, text="reset", command=self.reset).grid(row=240,column=0,pady=5)
        self._MyCanvas.bind("<Button-1>",self.ClickCounter)


        self._root.mainloop()

    
    def Draw(self):
        if self._shape == "oval":
            self._MyCanvas.create_oval(self._event1.x,self._event1.y,self._event2.x,self._event2.y,fill=self._colour)
        
        elif self._shape == "rectangle":
            self._MyCanvas.create_rectangle(self._event1.x,self._event1.y,self._event2.x,self._event2.y,fill=self._colour)
        
        elif self._shape == "line":
            self._MyCanvas.create_line(self._event1.x,self._event1.y,self._event2.x,self._event2.y,fill=self._colour, width=3)

    def ClickCounter(self,event):
        if self._colour == '' or self._shape == '':
            self.der()
            return  #exits out of method 
        if self._clickCounter == 0:
                self._event1 = event 
                self._clickCounter += 1
        elif self._clickCounter < 2:
                self._event2 = event 
                self._clickCounter += 1
                if self._clickCounter >=2:
                    self._clickCounter = 0
                    self.Draw()
                    self._event1 = ''
                    self._event2 = ''
                
    
    def reset(self):
        self._colour = ''
        self._shape  = ''   
        self._event1 = None
        self._event2 = None
        self._clickCounter = 0 
        self._UserChoiceVar.set(f'''To Draw on canvas 
         select colour and shape''')
        self._MyCanvas.delete("all")

    def SetColour(self,colour):
        self._colour = colour
        self._UserChoiceVar.set(f'''    Colour:{self._colour}
        Shape:{self._shape} ''')

    def SetShape(self,shape):
        self._shape = shape
        self._UserChoiceVar.set(f'''    Colour:{self._colour}
        Shape:{self._shape} ''')

    def der(self):
            self._event1 = None 
            self._event2 = None
            self._clickCounter = 0
            
            if self._colour == '' and self._shape == '':
                messagebox.showerror('User Error','Please select a colour and a shape')
            elif self._colour=='':
                messagebox.showerror('User Error','Please select a colour')
            else:
                messagebox.showerror('User Error','Please select a shape')


if __name__ == "__main__":
    DrawingApp()
 
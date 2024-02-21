
from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
from PIL import ImageTk,Image,ImageGrab


class Draw():
    def __init__(self,root):
        self.root =root
        self.window=root
        self.root.title("Drawing App")
        self.root.geometry("810x530")
        self.root.configure(background="white")

        self.pointer= "black"
        self.erase="white"

        text=Text(root)
        text.tag_configure("tag_name", justify='center', font=('arial',25),background='#292826',foreground='orange')

        text.insert("1.0", "Drawing Application ")

        text.tag_add("tag_name", "1.0", "end")
        text.pack()

        self.pick_color = LabelFrame(self.root,text='Colors',font =('arial',15),bd=6,relief=RIDGE,bg="white")
        self.pick_color.place(x=20,y=40,width=110,height=188)

        colors = ['blue','red','green', 'orange','violet','black','yellow','purple','pink','gold','brown','indigo','white','gray','skyblue','lightgreen','navyblue','deeppink']
        i=j=0
        for color in colors:
            Button(self.pick_color,bg=color,bd=2,relief=RIDGE,width=3,command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j+=1

        self.eraser_btn= Button(self.root,text="Eraser",bd=4,bg='white',command=self.eraser,width=14,relief=RIDGE)
        self.eraser_btn.place(x=20,y=230)

        self.clear_screen= Button(self.root,text="Clear Screen",bd=4,bg='white',command= lambda : self.background.delete('all'),width=14,relief=RIDGE)
        self.clear_screen.place(x=20,y=260)

        self.save_btn= Button(self.root,text="Save",bd=4,bg='white',command=self.save_drawing,width=14,relief=RIDGE)
        self.save_btn.place(x=20,y=290)

        self.bg_btn= Button(self.root,text="Background",bd=4,bg='white',command=self.canvas_color,width=14,relief=RIDGE)
        self.bg_btn.place(x=20,y=320)

        self.pointer_frame= LabelFrame(self.root,text='size',bd=5,bg='white',font=('arial',15,'bold'),relief=RIDGE)
        self.pointer_frame.place(x=30,y=350,height=200,width=90)

        self.pointer_size =Scale(self.pointer_frame,orient=VERTICAL,from_ =48 , to =0, length=168)
        self.pointer_size.set(1)
        self.pointer_size.grid(row=0,column=1,padx=15)

        self.background = Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=700,width=950)
        self.background.place(x=250,y=50)

        self.background = Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=700,width=950)
        self.background.place(x=250,y=50)

#Bind the background Canvas with mouse click
        self.background.bind("<B1-Motion>",self.paint) 

        self.pick_shapes = LabelFrame(self.root,text='Shapes',font =('arial',15),bd=6,relief=RIDGE,bg="white")
        self.pick_shapes.place(x=20,y=550,width=110,height=138)
        self.shapes1=[]
        for i in  range(1,13):
            self.shapes1.append(self.shapes(i))

        i=j=0
        k=1
        for shape in self.shapes1:
            Button(self.pick_shapes,image=shape,bd=2,relief=RAISED,width=26, command=lambda: self.control(k)).grid(row=i,column=j)
            i+=1
            k+=1
            if i==4:
                i=0
                j+=1

    def shapes(self, counter):
        match counter:
            case 1:
                return ImageTk.PhotoImage(Image.open("Pictures/line.jpg").resize((20, 20), Image.Resampling.LANCZOS))

            case 2:
                return ImageTk.PhotoImage(Image.open("Pictures/dashed_line.png").resize((20, 20), Image.Resampling.LANCZOS))

            case 3:
                return ImageTk.PhotoImage(Image.open("Pictures/rectangle.jpg").resize((20, 20), Image.Resampling.LANCZOS))

            case 4:
                return ImageTk.PhotoImage(Image.open("Pictures/parallelogram.png").resize((20, 20), Image.Resampling.LANCZOS))

            case 5:
                return ImageTk.PhotoImage(Image.open("Pictures/traingle.jpg").resize((20, 20), Image.Resampling.LANCZOS))

            case 6:
                return ImageTk.PhotoImage(Image.open("Pictures/pentagon.png").resize((20, 20), Image.Resampling.LANCZOS))

            case 7:
                return ImageTk.PhotoImage(Image.open("Pictures/hexagon.png").resize((20, 20), Image.Resampling.LANCZOS))

            case 8:
                return ImageTk.PhotoImage(Image.open("Pictures/arrow.png").resize((20, 20), Image.Resampling.LANCZOS))

            case 9:
                return ImageTk.PhotoImage(Image.open("Pictures/circle.png").resize((20, 20), Image.Resampling.LANCZOS))

            case 10:
                return ImageTk.PhotoImage(Image.open("Pictures/right_angled_traingle.png").resize((20, 20), Image.Resampling.LANCZOS))

            case 11:
                return ImageTk.PhotoImage(Image.open("Pictures/rounded_rectangle.png").resize((20, 20), Image.Resampling.LANCZOS))

            case 12:
                return ImageTk.PhotoImage(Image.open("Pictures/left_arrow.png").resize((20, 20), Image.Resampling.LANCZOS))

# Functions are defined here

# Paint Function for Drawing the lines on Canvas
    def paint(self,event):       
        x1,y1 = (event.x-2), (event.y-2)  
        x2,y2 = (event.x+2), (event.y+2)  

        self.background.create_oval(x1,y1,x2,y2,fill=self.pointer,outline=self.pointer,width=self.pointer_size.get())

# Function for choosing the color of pointer  
    def select_color(self,col):
        self.pointer = col

# Function for defining the eraser
    def eraser(self):
        self.pointer= self.erase

# Function for choosing the background color of the Canvas    
    def canvas_color(self):
        color=colorchooser.askcolor()
        self.background.configure(background=color[1])
        self.erase= color[1]

# Function for saving the image file in Local Computer
    def save_drawing(self):
        try:
            # self.background update()
            file_ss =filedialog.asksaveasfilename(defaultextension='jpg')
            #print(file_ss)
            x=self.root.winfo_rootx() + self.background.winfo_x()
            #print(x, self.background.winfo_x())
            y=self.root.winfo_rooty() + self.background.winfo_y()
            #print(y)

            x1= x + self.background.winfo_width() 
            #print(x1)
            y1= y + self.background.winfo_height()
            #print(y1)
            ImageGrab.grab().crop((x , y, x1, y1)).save(file_ss)
            messagebox.showinfo('Drawing Successfully Saved as' + str(file_ss))

        except:
            print("Error in saving the drawing")



if __name__ =="__main__":
    root = Tk()
    p= Draw(root)
    root.mainloop()
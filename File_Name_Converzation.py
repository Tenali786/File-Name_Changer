import os
from tkinter import *
from os.path import join
from tkinter import font
from tkinter import filedialog,messagebox

class File_Name_Changer():
    
    def __init__(self):
        L1 = Label(root,text="Tenali File Name Changer",font=('Berlin Sans FB Demi',25,),fg='lime',bg="crimson")
        L1.place(x=450,y=5)

    def Select_Folder(self):
        self.FileName= StringVar()
        self.FileExt = StringVar()
        self.Path = StringVar()
        self.Default = "C:/Users/Mr. Monu/Pictures"
        self.E1  = Entry(root,width=40,font=('Arial',15),fg='green',borderwidth=2,textvariable=self.Path)
        self.E1.place(x=370,y=250)
        self.Path.set(self.Default)


        self.B1 = Button(root,cursor="hand2",text="Select Path",command=File.Select,font=('Berlin Sans FB Demi',12),fg='blue',border=None,bg='white',relief=GROOVE,borderwidth=2)
        self.B1.place(x=270,y=250)
    
        self.Name= Label(root,text="Set File Name",font=("Berlin Sans FB Demi",12),bg='crimson')
        self.Name.place(x=250,y=350)
        self.E2  = Entry(root,width=20,font=('Arial',15),fg='green',borderwidth=2,textvariable=self.FileName)
        self.E2.place(x=250,y=380)

        self.Ext = Label(root,text="Set File Extention",font=("Berlin Sans FB Demi",10),bg='crimson')
        self.Ext.place(x=650,y=350)

        self.E3  = Entry(root,width=20,font=('Arial',15),fg='green',borderwidth=2,textvariable=self.FileExt)
        self.E3.place(x=650,y=380)

        Start = Button(root,cursor="hand2",text='Stat Converzation',font=("",12),command=lambda:File.StartConverzation(2))
        Start.place(x=450,y=610)
        root.bind('<Return>',File.StartConverzation)


    def Select(self):
        self.Select_Path = filedialog.askdirectory(title='Select Folder')
        self.Path.set("")
        self.Path.set(self.Select_Path)
    

    def StartConverzation(self,a):
        if self.FileExt.get()==""  and self.FileName.get()=='':
            messagebox.showerror("File Name Converzation","Please... \n Fill The File Name and File Extention")

        elif self.FileName.get()=='':
            messagebox.showerror("File Name Converzation","Please... \n Fill The File Name \n As You want to set")
        elif self.FileExt.get()=="":
            messagebox.showerror("File Name Converzation","Please... \n Fill The File Extention \n As You want to set")

        else:
            files= os.listdir(self.Select_Path)
          
            files.remove('File_Name_Converzation.py')
            for i in range(1,len(files)):
                os.rename(files[i],f"{self.FileName.get()}{i}.{self.FileExt.get()}")
            
            messagebox.showinfo(title="File Name Converzation",message= 'The Process of Changing Files Name is!!!!   Complete')
            self.Path.set('')
            self.FileName.set("")
            self.FileExt.set("")


if __name__=="__main__":
    root = Tk()
    root.geometry('1368x778')
    root.title('File Name Changer')
    root.config(bg='crimson')

    File = File_Name_Changer()
    File.Select_Folder()

    root.mainloop()




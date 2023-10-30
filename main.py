import customtkinter as tkc
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import datetime
from datetime import datetime
import os
data_=datetime.now().time()
print(data_)
DAY=datetime.now().date()
print(DAY)
fileofdb="app.db"
#if not os.path.exists(fileofdb):
db=sqlite3.connect("app.db")
db.execute("CREATE TABLE if not exists PRODUCE(name TEXT,price_sell FLOAT,price FLOAT,moant INTEGER,data TEXT,phonenum INTEGER,day TEXT)")
db.execute(f"INSERT INTO PRODUCE (name, price_sell, price, moant, DATA, phonenum,day) VALUES ('لبتون شاي', 15, 12, 300, '{data_}', '01157470072',{DAY})")
db.execute(f"INSERT INTO PRODUCE (name, price_sell, price, moant, DATA, phonenum,day) VALUES ('علبة جبنة عبور لاند', 8, 5, 350, '{data_}', '01157470072','{DAY}')")
db.execute(f"INSERT INTO PRODUCE (name, price_sell, price, moant, DATA, phonenum,day) VALUES ('لبن المراعي', 28, 20, 20, '{data_}', '01157470072','{DAY}')")
list2003 = db.execute( "SELECT name FROM PRODUCE").fetchall()
#DATABASE
#raise ValueError("not allow")
class app(tkc.CTk):
    def __init__(self):
        super().__init__()
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.title("m&y")
        self.geometry( ""+str(self.width)+"x"+str(self.height)+"")
        self.resizable()
        #frame ofmain1
        self.mainframe1 = tkc.CTkFrame(self, width=self.width, height=self.height)

        self.mainframe1.pack(fill="both",expand=True)
        #frame main 2
        self.mainframe2 = tkc.CTkFrame(self   ,width=self.width ,height=self.height)#fg_color="antiquewhite",bg_color="lightblue",

        self.OPTVAR = tkc.StringVar(self)
        self.opttionmenu0()
        self.labels()
        self.scroll( x1=224,y1=148,hei=855)
        self.list()
        self.framelist ={self.mainframe1}
        self.scrollframe()
        self.search=tkc.CTkEntry(self.mainframe1 ,width=400)
        self.search.place(x=400, y=150)
        dscrollbar=tk.Frame(self.mainframe2,height=30,width=self.width*2,background="grey")
        dscrollbar.place(y=360,x=0)
        #mainframe
        while True:
            if 0xff==ord("y"):
                print("a7a")

    def opttionmenu0(self):

        self.language=('English','عربي')

        opttionmenu=tk.ttk.OptionMenu(self,self.OPTVAR,self.language[0],*self.language,command = self.command)

        opttionmenu.place(x=0,y=0)
    def inmageadd(self):
        photopath = filedialog.askopenfilename(title="Select Image",filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")))
        return photopath

    def labels(self):

        #الشريط الازرق
        self.tittyle=tkc.CTkFrame(self,width=1000,height=18,bg_color="skyblue",fg_color="skyblue")
        self.tittyle.place(x=60,y=0)

        #الرساله
        self.wada3a=tkc.CTkLabel(self.tittyle,text_color="black",width=1479,height=18,text="لها الدعاء ارجوا جدتي روح علي العمل هذا")
        self.wada3a.pack()
        #الصور

        try:
            iMG2 = Image.open("test.png")
            self.imagesea = ImageTk.PhotoImage(iMG2)
        except:
            print("no error")

        #frame 2

        #self.frame2 =tkc.CTkFrame(self.mainframe1  ,width=1640  ,height=450,bg_color="gray",fg_color="gray")
        #self.frame2.place(x=0,y=18)
        #frame buttons
        self.buttonframe=tkc.CTkFrame(self,width=1537,height=101,bg_color="steelblue",fg_color="navy",border_color="seashell")
        self.buttonframe.place(x=0,y=19)

        self.buttonmenu =tkc.CTkButton(self.buttonframe,corner_radius=5,width=200,height=50,text="القائمة الرئيسية",font=("Arial", 24),command=lambda :self.mainframecomm())#need command
        self.buttonmenu.place(x=10,y=40)
        self.button1=tkc.CTkButton(self.buttonframe,corner_radius=5,width=200,height=50,text="المبيعات",font=("Arial", 24),command=lambda :self.mainframe2comm())#need command
        self.button1.place(x=230,y=40)
        self.button2=tkc.CTkButton(self.buttonframe,corner_radius=5,width=200,height=50,text="التقرير",font=("Arial", 24))
        self.button2.place(x=442,y=40)
        self.buttonprice=tkc.CTkButton(self.mainframe2,command=lambda :self.pricecommandbutton())
        self.buttonprice.place(x=150,y=200)
        self.searchbutton=tkc.CTkButton(self.mainframe1,command=self.search_listbox,text="search")
        self.searchbutton.place(x=220,y=150)

        #holy quranw
        # frameof main 2
        self.entryprice = tkc.CTkEntry(master=self.mainframe2)
        self.entryprice.place(x=110, y=150)
        self.entryprice.insert(0, "price")
        self.buttongetorder=tkc.CTkButton(self.mainframe2,text="order",command=self.datebaseoperation)
        self.buttongetorder.place(x=300,y=150)
        self.entrypricelabel = tkc.CTkLabel(self.mainframe2, text=f"i a      price", corner_radius=15,
                                            fg_color="honeydew", width=150, font=("Arial", 18), text_color="peru")
        self.entrypricelabel.place(x=-50, y=150)
        self.scrollframer = tkc.CTkFrame(self.mainframe2, fg_color="blue", width=1536, height=650,corner_radius=0)
        self.scrollframer.place(x=0, y=300)
#.....................................................
        self.inputname=tkc.CTkEntry(self.mainframe1)
        self.inputname.place(x=220,y=300)
        self.frameinputname=tkc.CTkLabel(self.mainframe1,text="اسم المنتج",text_color="orange",width=100, font=("Arial", 22))
        self.frameinputname.place(x=360,y=300)

#****************************************************
        self.inputprice = tkc.CTkEntry(self.mainframe1)
        self.inputprice.place(x=220,y=500)
    #********************************************
        self.frameinputprice = tkc.CTkLabel(self.mainframe1, text="سعر المنتج", text_color="orange", width=100,
                                           font=("Arial", 22))
        self.frameinputprice.place(x=360, y=500)
        #****************************************صورة المنتج
#*****************************
        self.inputmount = tkc.CTkEntry(self.mainframe1)
        self.inputmount.place(x=220,y=600)
        self.frameinputphoto = tkc.CTkLabel(self.mainframe1, text="اضافة صورة", text_color="orange", width=100,
                                            font=("Arial", 22))
        self.frameinputphoto.place(x=360, y=700)

        self.frameinputmount = tkc.CTkLabel(self.mainframe1, text="اضافة كمية", text_color="orange", width=100,
                                            font=("Arial", 22))
        self.frameinputmount.place(x=360, y=600)

        self.inputpricesell=tkc.CTkEntry(self.mainframe1)
        self.inputpricesell.place(x=220,y=400)
        self.inputpricesellframe=tkc.CTkLabel(self.mainframe1,text="سعر البيع",text_color="orange",width=100,font=("Arial" ,22))
        self.inputpricesellframe.place(x=360,y=400)

        self.adddatebase=ttk.Button(self.mainframe1,text="اضافة",width=20,command=self.add_frame)
        self.adddatebase.place(x=1080,y=190)

        self.updatadatebase = ttk.Button(self.mainframe1, text="تعديل",width=20)
        self.updatadatebase.place(x=1210, y=190)


    def counterplus(self, indexrow, indexcol, num_frames_col):
        index = indexrow * num_frames_col + indexcol
        self.counters[index] += 1
        self.screens[index].configure(text=self.counters[index])

    def countermin(self, index):
        if self.counters[index] > 0:
            self.counters[index] -= 1
        self.screens[index].configure(text=self.counters[index])

    def get_frame_values(self):
        result = [screen.cget("text") for screen in self.screens]

    def add_frame(self):
        #**********************************************************************************************************
        namedata=self.inputname.get()

        pricesell=self.inputpricesell.get()

        price=self.inputprice.get()

        mount=self.inputmount.get()

        self.inputprice.delete(0,tk.END)
        self.inputmount.delete(0,tk.END)
        self.inputpricesell.delete(0,tk.END)
        self.inputname.delete(0,tk.END)

        pathphoto=self.inmageadd()

        if len(mount) ==0 or len(price)==0 or len(pricesell)==0 or len(namedata)==0 or len(pathphoto)==0:
            messagebox.showerror("ادخال خطاء","الرجاء ادخل جميع الخانات و اختر صوره للمنتج")



        ohotopath=self
    def scrollframe(self):
        self.canvas = tk.Canvas(self.scrollframer, width=1896, height=620)
        self.canvas.pack(side=tk.LEFT, expand=True)
        scrollbar = ttk.Scrollbar(self.scrollframer, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.scrollable_frame = tk.Frame(self.canvas, border=5, borderwidth=10, bg="black")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", state=tk.NORMAL)
        # Define the number of frames
        num_frames_row = 8#int(len(list2003)/3)
        num_frames_col = 3
        self.counters = [0] * (num_frames_row * num_frames_col)
        self.frames = []
        self.screens = []

        self.scroll_lock = False  # Scroll lock flag

        for i in range(num_frames_row):
            for j in range(num_frames_col):
                yyy = tkc.CTkFrame(self.scrollable_frame, width=600, height=241, fg_color="black")
                zz = tkc.CTkButton(yyy, width=450, height=190, text="value", image=self.imagesea)
                zz.grid(column=0, row=0)

                framecounter = tkc.CTkFrame(yyy, width=400, height=51, fg_color="black", corner_radius=30)
                contermin = tkc.CTkButton(framecounter, width=120, height=50, text="-", corner_radius=15,
                                          command=lambda index=i * num_frames_col + j: self.countermin(index))
                contermin.grid(row=0, column=2)
                screen = tkc.CTkLabel(framecounter, width=210, height=5, corner_radius=10,
                                      text=self.counters[i * num_frames_col + j])
                screen.grid(row=0, column=1)
                contermax = tkc.CTkButton(framecounter, width=120, height=50, text="+", corner_radius=15,
                                          command=lambda indexrow=i, indexcol=j,
                                                         num_frames_col=num_frames_col: self.counterplus(indexrow,
                                                                                                         indexcol,
                                                                                                         num_frames_col))
                contermax.grid(row=0, column=0)

                framecounter.grid(row=1, column=0)
                yyy.grid(row=i, column=j, padx=30, pady=5)

                self.frames.append(yyy)
                self.screens.append(screen)

        self.canvas.bind("<Configure>", self.configure_scroll_region)
        self.canvas.bind("<ButtonPress-1>", self.lock_scroll)
        self.canvas.bind("<ButtonRelease-1>", self.unlock_scroll)

    def configure_scroll_region(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        if not self.scroll_lock:
            self.render_frames()

    def lock_scroll(self, event=None):
        self.scroll_lock = True

    def unlock_scroll(self, event=None):
        self.scroll_lock = False
        self.render_frames()

    def render_frames(self):
        for screen in self.screens:
            screen.update_idletasks()
            screen.update()
    def scroll(self,x1,y1,hei):
        self.scroll = tk.Scrollbar(self.mainframe1, orient="vertical")
        self.scroll.place(x=x1-9, y=y1, height=hei)
    def list(self):
        self.mylist = tk.Listbox(self.mainframe1, yscrollcommand=self.scroll.set, height=35,width=14,fg="white", font=("Arial",20),background="midnightblue",selectmode="BROWSE",highlightbackground="midnightblue")
        self.listlol=[]
        for i in range(len(list2003)):
            value=list2003[i]
            value=str(value).strip("{('")
            value = str(value).strip(",')}")
            self.listlol.append(value)
            print(type(self.listlol))


        for line in self.listlol:
            self.mylist.insert(0,line)

        self.mylist.place(x=0, y=150)
        self.scroll.configure(command=self.mylist.yview)
        self.mylist.bind("<<ListboxSelect>>", self.commandscroll)

    def commandscroll(self, event):
        self.selection=self.mylist.get(self.mylist.curselection())
        print(self.selection)
        #photo=ImageTk.PhotoImage(open(file="hh.jpg",mode='a'))
        #self.buttonimg=tkc.CTkButton(image=photo)
        #self.buttonimg.pack()
    def command(self,*args):
        selector=self.OPTVAR.get()

    def mainframecomm(self):
        #self.mainframe1.pack_forget()
        self.mainframe2.pack_forget()
        self.mainframe1.pack(fill="both", expand=True)
    def mainframe2comm(self):

        self.mainframe1.pack_forget()
        #self.mainframe2.pack_forget() x=t4g53125567

        self.mainframe2.pack(fill="both",expand=True)
    def pricecommandbutton(self,*args):
        self.valueprice= self.entryprice.get()
        self.entryprice.delete(0,tk.END)
        print(self.valueprice)
    def search_listbox(self):
        self.query=self.search.get()                                      #
        self.search.delete(0,tk.END)
        #self.search.delete(0, tk.END)  # Clear the search entry widget
        self.mylist.delete(0, tk.END)
        for item in self.listlol:
            if self.query.lower() in item.lower():
                self.mylist.insert(tk.END,"")
                self.mylist.insert(tk.END,item)

    def datebaseoperation(self):
        ordervalus=self.get_frame_values()
        for i in range(len(ordervalus)):
            list_tuble=[]
            list_tuble=ordervalus
            newi=0
        for i in list_tuble:
            if i !=0:
                index200=list_tuble.index(i,newi)
                print(index200+1)
            newi = newi + 1
                #db.execute("")
        db.commit()
        db.close()

#################################################################################################
                                                                                      #######
if __name__=="__main__":                                                         ##########
    app1=app()                                                              ########
    app1.mainloop()                                                              ##########
                                                                                      #######
#################################################################################################

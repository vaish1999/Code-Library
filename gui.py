import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk



root = Tk()
root.title("smart anotator")
v=0
val=0
var = IntVar()
gp=StringVar()
entry=[]
radio=[]
button=[]
classes=[]
i=3
j=0

def add_radiobutton(catagory='',vble=None,fn=None,ROW=0,COLUMN=0,ROWSPAN=1,COLUMNSPAN=1,PADX=0,PADY=0):
	global val
	val+=1
	x=Radiobutton(root,text=catagory,indicatoron=0,width=30,command=fn,variable=vble,value=val)
	x.grid(row=ROW,column=COLUMN,rowspan=ROWSPAN,padx=PADX,pady=PADY)
	return x


def add_listbox(hgt=10,wdt=20,mode=BROWSE,ROW=0,COLUMN=0,ROWSPAN=1,COLUMNSPAN=1,PADX=0,PADY=0):
	x=Listbox(root,height=hgt,width=wdt,selectmode=mode)
	x.grid(row=ROW,column=COLUMN,rowspan=ROWSPAN,padx=PADX,pady=PADY)
	return x



def add_textentry(vble,ROW=0,COLUMN=0,ROWSPAN=1,COLUMNSPAN=1,PADX=0,PADY=0):
	x=(Entry(root,textvariable=vble))
	x.grid(row=ROW,column=COLUMN,rowspan=ROWSPAN,padx=PADX,pady=PADY)
	return x


def add_button(labl,fn,ROW=0,COLUMN=0,ROWSPAN=1,COLUMNSPAN=1,PADX=0,PADY=0):
	x=(Button(root,text=labl,command=fn))
	x.grid(row=ROW,column=COLUMN,rowspan=ROWSPAN,padx=PADX,pady=PADY)



def printabcd():
	print("abcd")
def add_menu():

	menu=Menu(root)

	filemenu=Menu(menu,tearoff=0)

	filemenu.add_command(label="load images",command=printabcd)
	filemenu.add_command(label="convert video",command=None)


	filemenu.add_separator()

	filemenu.add_command(label="exit",command=None)

	menu.add_cascade(label='File',menu=filemenu)



	edit=Menu(menu,tearoff=0)

	edit.add_command(label="create folders",command=None)
	edit.add_command(label="write file",command=None)
	

	menu.add_cascade(label='Annotation',menu=edit)

	hlp=Menu(menu,tearoff=0)

	menu.add_cascade(label='Help',menu=hlp)

	About=Menu(menu,tearoff=0)

	menu.add_cascade(label='About',menu=About)

	root.config(menu=menu)
#def add_checkbox():
def add_messagebox():


def add_image(path,x=300,y=300):
	load=Image.open(path)
	render=ImageTk.PhotoImage(load)
	img=ttk.Label(image=render)
	img.image=render
	img.place(x=x,y=y)



def create_class():
	global radio,classes,i,j
	if gp.get()=='':
		print("error:enter valid string")
		return
	classes.append(gp.get())
	radio.append(add_radiobutton(gp.get(),var,printradio,i,5))
	entry[0].delete(first=0,last=END)
	i+=1

def printclass():
	print(classes)

def printradio():
	print(str(var.get()))




add_menu()
add_radiobutton('images',ROW=0,COLUMN=0)
add_radiobutton(ROW=0,COLUMN=1)
add_radiobutton(ROW=0,COLUMN=2)
add_radiobutton(ROW=0,COLUMN=3)
add_radiobutton(ROW=0,COLUMN=4)
add_radiobutton('Add class',ROW=0,COLUMN=5)
for k in range(40):
	add_radiobutton(ROW=k,COLUMN=6)

val=0

button.append(add_button("   create   ",create_class,2,5))
button.append(add_button("   >>   ",None,20,3))
button.append(add_button("   <<   ",None,20,1))
button.append(add_button("   play/pause   ",None,22,2))
button.append(add_button("   predict   ",None,24,2))
#button.append(add_button("printclass",printclass,1,1))
entry.append(add_textentry(gp,1,5))

#add_image("c:/users/girishhegde/iitdimg/dog2.jpg")
add_listbox(hgt=60,wdt=30,mode=MULTIPLE,ROW=2,COLUMN=0,ROWSPAN=60)






root.mainloop()
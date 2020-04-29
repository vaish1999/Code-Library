import cv2
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import time
import pyautogui
import re
import pickle
import shutil
from tkinter import messagebox
import numpy as np

root = Tk()
root.title("Flossify")
root.config(bg='skyblue')
v=0
val=0
#catagory index variable
var = IntVar()
#catgory name varible from text entry               
gp=StringVar()
#frame slide variable
slider=IntVar()
#from frame variable
from_frame = IntVar()
#to_frame variable
to_frame = IntVar()

#path textentry variable
paath = StringVar()

#output folder path variable
output_path = StringVar()

#final frame variable
fframe = IntVar()

first_frame = IntVar()

#annotation checkbox variable
check = IntVar()

#video conver option checkbox variable
full = IntVar()


xthreshold = IntVar()

ythreshold = IntVar()


file_path = StringVar()

speed = 1
entry=[]
radio=[]
button=[]
classes=[]


classfile = []

currentframe = 0
finalframe = 0
path = ''


i=3
j=0
f=0
t=100

def add_radiobutton(catagory='',vble=None,fn=None,ROW=0,COLUMN=0,ROWSPAN=1,COLUMNSPAN=1,PADX=0,PADY=0,bgg=None):
	global val
	val+=1
	x=Radiobutton(root,text=catagory,indicatoron=0,width=30,command=fn,variable=vble,value=val,bg=bgg)
	x.grid(row=ROW,column=COLUMN,rowspan=ROWSPAN,padx=PADX,pady=PADY)
	return x


def add_listbox(hgt=10,wdt=20,mode=SINGLE,x1=0,y1=0,PADX=0,PADY=0):
	x=Listbox(root,height=hgt,width=wdt,selectmode=mode)
	x.place(x=x1,y=y1,height=wdt,width=hgt)
	return x

def add_slider(vble=None,orientation=HORIZONTAL,fn = None,frm=0,to=0,wdt=10,lnth=100,x1=0,y1=0):
	x=Scale(root,orient=orientation,width=wdt,length=lnth,variable=vble,command=fn,from_=frm,to=to)
	x.place(x=x1,y=y1,height=wdt,width=lnth)
	return x 



def add_textentry(vble,ROW=0,COLUMN=0,ROWSPAN=1,COLUMNSPAN=1,PADX=0,PADY=0):
	x=(Entry(root,textvariable=vble))
	x.grid(row=ROW,column=COLUMN,rowspan=ROWSPAN,padx=PADX,pady=PADY)
	return x


def add_checkbox(lble,vble,cmd=None,ROW=0,COLUMN=0,ROWSPAN=1,COLUMNSPAN=1,PADX=0,PADY=0):
	x=(Checkbutton(root,text=lble,variable=vble,onvalue=1,offvalue=0,command=cmd,height=1,width=20))
	x.grid(row=ROW,column=COLUMN,rowspan=ROWSPAN,padx=PADX,pady=PADY)
	return x

def add_button(labl,fn,ROW=0,COLUMN=0,ROWSPAN=1,COLUMNSPAN=1,PADX=0,PADY=0):
	x=(Button(root,text=labl,command=fn))
	x.grid(row=ROW,column=COLUMN,rowspan=ROWSPAN,padx=PADX,pady=PADY)
	return x

def sort_dir(data):
	convert=lambda text:int(text) if text.isdigit() else text.lower()
	ak=lambda key:[convert(c) for c in re.split('([0-9]+)',key)]
	return sorted(data,key=ak)



def add_menu():

	menu=Menu(root)

	filemenu=Menu(menu,tearoff=0)

	#filemenu.add_command(label="Load frames",command=load_frames)
	#filemenu.add_command(label="Convert video",command=video_to_frame)
	filemenu.add_command(label="Load video",command=load_video)


	filemenu.add_separator()

	filemenu.add_command(label="Exit",command=exitfun)

	menu.add_cascade(label='File',menu=filemenu)



	edit=Menu(menu,tearoff=0)

	#edit.add_command(label="Create folders",command=None)
	edit.add_command(label="Load table and create folder",command=None)
	edit.add_command(label="Speed up",command=increasevideospeed)
	edit.add_command(label="Slow down",command=deccreasevideospeed)

	

	menu.add_cascade(label='Annotation',menu=edit)

	hlp=Menu(menu,tearoff=0)

	menu.add_cascade(label='Help',menu=hlp)

	About=Menu(menu,tearoff=0)

	menu.add_cascade(label='About',menu=About)

	root.config(menu=menu)

def exitfun():

	cv2.destroyAllWindows()
	exit()

'''
def load_frames():

	global path,finalframe,s,classfile


	path = paath.get()

	items=[]


	errorbox.delete('1.0',END)
	errorbox.delete('2.0',END)  #line.column


	if os.path.exists(path) :



		if full.get() :

			errorbox.insert(END,"Loading whole directory .................")

			items = sort_dir(os.listdir(path))


			finalframe = len(items) - 1
		
		else:

			cf=first_frame.get()

			finalframe = fframe.get()

			errorbox.insert(END,"Loading"+str(finalframe)+"frames .................")


			items = (sort_dir(os.listdir(path))[cf:cf+finalframe])



		for i in range(len(items)):

			l.insert(i,items[i])

		for i in range(finalframe+1):
			classfile.append(-1)

		s=add_slider(vble=slider,fn = slide,frm=0,to=finalframe,wdt=40,lnth=490,x1=305,y1=530)

		errorbox.insert('2.0','\nsuccess')

		show()

	else :
		errorbox.delete('1.0',END)

		errorbox.insert('1.0',"error : invalid path")
'''

def load_video():

	global path,finalframe,s,classfile,currentframe,fffirst,cap


	path = file_path.get()

	items=[]


	if os.path.exists(path) :

		cap = cv2.VideoCapture(path)

		if full.get() :

			cf = 0

			finalframe = int(cap.get(7))-1


			for i in range(finalframe+1):

				l.insert(i,i)

		
		else:

			cf=first_frame.get()

			if cf + fframe.get() < cap.get(7) :

				finalframe = cf + fframe.get() -1

			else :
				messagebox.showerror("error","frame index out of range")
				return


			for i in range(finalframe-cf+1):

				l.insert(i,i+cf)


			#errorbox.insert(END,"Loading"+str(finalframe)+"frames .................")


			#items = (sort_dir(os.listdir(path))[cf:cf+finalframe])

		currentframe = cf

		fffirst  = cf

		for i in range(finalframe+1):
			classfile.append(0)

		s=Scale(root,orient=HORIZONTAL,width=10,length=490,variable=slider,command=slide,from_=0,to=finalframe-cf)
		s.grid(row=21,column=0,columnspan=5,rowspan=2)
	
		cv2.destroyAllWindows()

		show()

	else :
		errorbox.delete('1.0',END)

		errorbox.insert('1.0',"error : invalid path")

		

'''

def video_to_frame():

	p = file_path.get()


	errorbox.delete('1.0',END)
	errorbox.delete('2.0',END)  #line.column

	opath = output_path.get()

	if os.path.isfile(p) == False :
		errorbox.insert('1.0',"error : invalid source file")
		return

	if os.path.exists(opath) == False :

		errorbox.insert('1.0',"creating destination directory...........")

		os.mkdir(opath)

		errorbox.insert('2.0',"\nsuccess")

	cap = cv2.VideoCapture(p)

	if full.get() == 0:

		cf=first_frame.get()

		ff  = fframe.get()

		entry[3].delete(0,END)

		entry[3].insert(0," No. of frames ")

		ret = 1

		temp=0

		errorbox.insert('3.0',"\nconverting"+str(ff)+"frames...........")

		while temp < cf and ret:

			ret , frame =cap.read()

			temp += 1

		ret = 1

		ff = ff + cf

		while (cf  < ff) and ret:

			ret , frame =cap.read()

			filename  = opath+'/'+str(cf)+'.jpg'

			cv2.imwrite(filename,frame)

			cf+=1
		

	else :

		errorbox.insert('3.0',"\nconverting whole video into frames...........")

		cf = 1

		success = 1

		while success:

			success , frame =cap.read()

			filename  = opath+'/'+str(cf)+'.jpg'

			cv2.imwrite(filename,frame)

			cf +=1

	errorbox.insert(END,"\ndone")

	cap.release()

'''

def increasevideospeed():
	global speed
	if speed > 0:
		speed -= 1

def deccreasevideospeed():
	global speed
	if speed < 20:
		speed += 1

def create_class():
	global radio,classes,i,j

	errorbox.delete('1.0',END)
	errorbox.delete('2.0',END)  #line.column
	if gp.get()=='':
		errorbox.insert(END,"error : enter valid class name")
		print("error:enter valid string")
		messagebox.showerror('ERROR','enter valid class name')
		return

	classes.append(gp.get())
	radio.append(add_radiobutton(gp.get(),var,present,i,5,bgg='lightpink'))
	entry[0].delete(first=0,last=END)
	i+=1

	errorbox.insert(END,"new class :"+str(gp.get())+"created")

flag=1

def present():
	global classfile,currentframe
	if len(classfile)<1:
		return
	classfile[currentframe] = var.get()
	l.delete(currentframe)
	l.insert(currentframe,str(currentframe+fffirst)+'---'+str(var.get()))

'''

def videoplay():
	
	global currentframe,finalframe,path,flag,speed

	errorbox.delete('1.0',END)
	if os.path.exists(path) == False:
		errorbox.insert(END,"error : inavalid path or frames not loaded")
		return
	x =sort_dir(os.listdir(path))

	flag=1
	cv2.destroyAllWindows()	
	cf = currentframe
	t1 = time.time()

	errorbox.insert(END,"playing video")
	
	while (currentframe < finalframe):
			
			fm =os.path.join(path,x[currentframe])
			frame = cv2.imread(fm)
			cv2.imshow("frame",frame)
			cv2.setMouseCallback('frame',rect)
			l.activate(currentframe)
			s.set(currentframe)
			currentframe += 1
			if flag==0:
				break

			for j in range(speed):
				cv2.waitKey(1)
	t2 = time.time()

	if check.get():
		errorbox.insert(END,"\nannotating....")
		for i in range(cf,currentframe+1):
			classfile[i] = var.get()
		errorbox.insert(END,"done")

	if t2-t1 !=0 and currentframe - cf != 0:

		spd = (currentframe-cf)/(t2-t1)

		errorbox.insert(END,"\n"+str(spd)+"fps")

		print(spd,"fps")

'''




def videoplay():
	
	global currentframe,finalframe,path,flag,speed

	errorbox.delete('1.0',END)
	if os.path.exists(path) == False:
		errorbox.insert(END,"error : inavalid path ")
		messagebox.showerror("error","video not loaded")
		return

	flag=1
	cv2.destroyAllWindows()	
	cf = currentframe
	t1 = time.time()

	errorbox.insert(END,"playing video")
	
	while (currentframe <= finalframe):

			show()
			
			cv2.setMouseCallback('frame',rect)

			l.activate(currentframe)
			s.set(currentframe)
			currentframe += 1
			if flag==0:
				break

			for j in range(speed):
				cv2.waitKey(1)

	cv2.destroyAllWindows()
	show()

	t2 = time.time()

	if check.get():
		errorbox.insert(END,"\nannotating....")
		for i in range(cf,currentframe+1):
			classfile[i] = var.get()
			l.delete(i)
			l.insert(i,str(i+fffirst)+'---'+str(var.get()))


		errorbox.insert(END,"done")

	if t2-t1 !=0 and currentframe - cf != 0:

		spd = (currentframe-cf)/(t2-t1)

		errorbox.insert(END,"\n"+str(spd)+"fps")

		print(spd,"fps")





def next_image():
	global currentframe,finalframe,path

	errorbox.delete('1.0',END)

	if os.path.exists(path) == False:
		messagebox.showerror("error","video not loaded")
		return

	if currentframe < finalframe :

		currentframe+=1

	else:
		errorbox.insert(END,"no next image to show")

	if check.get():

		classfile[currentframe] = var.get()
		l.delete(currentframe)
		l.insert(currentframe,str(currentframe+fffirst)+"---"+str(var.get()))

	cv2.destroyAllWindows()
	l.activate(currentframe)
	s.set(currentframe)
	show()


def prev_image():
	global currentframe,finalframe,path
	
	errorbox.delete('1.0',END)
	

	if os.path.exists(path) == False:
		messagebox.showerror("error","video not loaded")
		
		return
	if currentframe > 0  :
		currentframe -= 1

	else :
		errorbox.insert(END,"no previous image to show")


	if check.get():
		classfile[currentframe] = var.get()
		l.delete(currentframe)
		l.insert(currentframe,str(currentframe+fffirst)+"---"+str(var.get()))



	cv2.destroyAllWindows()
	l.activate(currentframe)
	s.set(currentframe)
	show()





def fromtoannotate():
	global c
	errorbox.delete('1.0',END)
	x = from_frame.get()
	y = to_frame.get()
	c = var.get()

	if x < 0 or y > finalframe:
		messagebox.showerror("error","index out of range")
		print('error')
		return

	entry[1].delete(first=0,last=END)
	entry[2].delete(first=0,last=END)
	entry[1].insert(0,0)
	entry[2].insert(0,0)

	errorbox.insert(END,"Annotating...............")

	for i in range(x,y):
		classfile[i] = c
		l.delete(i)
		l.insert(i,str(i+fffirst)+"---"+str(c))




	errorbox.insert(END,"\ndone")

def listboxfn(event):
	global currentframe
	currentframe = l.curselection()[0]+fffirst
	l.activate(currentframe)
	s.set(currentframe)
	cv2.destroyAllWindows()
	show()

def show():
	
	cap.set(1,currentframe)
	ret,frame = cap.read()
	frame = cv2.resize(frame,(500,281),interpolation = cv2.INTER_AREA)
	#cv2.putText(frame,str(currentframe),(20,20),cv2.FONT_HERSHEY_SIMPLEX,2,255)
	cv2.imshow("frame",frame)

def dshow():

	cv2.destroyAllWindows()
	show()


def slide(x=None):
	
	global currentframe,finalframe,path
	cv2.destroyAllWindows()
	currentframe = (slider.get())
	l.activate(currentframe)
	show()

def rect(event,x,y,flags,param):
	global xy,i,flag
	if event==cv2.EVENT_LBUTTONDOWN:
		errorbox.insert(END,"\nPaused")
		flag=0

def cleartext1(event):
	ipth = filedialog.askdirectory()
	entry[4].delete(0,END)
	entry[4].insert(0,ipth)

def cleartext2(event):
	
	ipth = filedialog.askdirectory()
	entry[5].delete(0,END)
	entry[5].insert(0,ipth)


def cleartext3(event):
	ipth = filedialog.askopenfilename(initialdir = '/',title = "select file",filetypes = (("video",'*.*'),('all files','*.*')))
	entry[6].delete(0,END)
	entry[6].insert(0,ipth)




def cleartext4(event):
	entry[3].delete(0,END)
	entry[3].insert(0,0)


def printclass():
	print(classes)

def pause():
	global flag
	flag=0



def writefile():
	global classfile,classes
	dest = output_path.get()
	if os.path.exists(dest) == False:
		messagebox.showerror("error","path not given")
		return
	errorbox.delete('1.0',END)
	print("writing...")
	errorbox.insert(END,"\nwriting file")
	
	file = open(dest+'/classified.pkl','wb')
	pickle.dump(classfile,file)
	file.close()
	file = open(dest+'/classes.pkl','wb')
	pickle.dump(classes,file)
	file.close()
	errorbox.insert(END,"\ndone")
	print("done")
'''
def createfolder():
	global path,classfile,classes

	errorbox.delete('1.0',END)

	dest = output_path.get()

	for folder in classes :
		if os.path.exists(dest+'/'+folder) == False:
			os.mkdir(dest+'/'+folder)
		else :
			shutil.rmtree(dest+'/'+folder)
			os.mkdir(dest+'/'+folder)

	items = sort_dir(os.listdir(path))

	errorbox.insert(END,"\ncopying to specific folders........")
	for i in range(len(classfile)) :
		if classfile[i] > 0 :
			#print(classes[classfile[i]])
			#print(items[i])
			shutil.copy(path+'/'+items[i],dest+'/'+classes[classfile[i]-1])
	errorbox.insert(END,"\ndone")
	print("donnnneeeee")
	'''
'''
def load_create():

	dest = output_path.get()
	pth = paath.get()
	table = open(pth,'rb')
	x=pickle.load(table)
	file.close()

	pth = paath.get()
	table = open(pth,'rb')
	clss=pickle.load(table)
	file.close()



	for folder in clss :
		if os.path.exists(dest+'/'+folder) == False:
			os.mkdir(dest+'/'+folder)
		else :
			shutil.rmtree(dest+'/'+folder)
			os.mkdir(dest+'/'+folder)

	items = sort_dir(os.listdir(fromaddress))

	for i in range(len(x)) :
		if x[i] > 0 :
			#print(classes[classfile[i]])
			#print(items[i])
			shutil.copy(pth+'/'+items[i],dest+'/'+clss[x[i]-1])
	print("donnnneeeee")

'''

def select_point(event, x, y, flags, params):
    global point, point_selected, old_points,flag,xx
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        point_selected = True
        old_points1 = np.array([[x, y]], dtype=np.float32)
        if flag==1:
            old_points=np.concatenate((old_points,old_points1))
            xx=np.concatenate((xx,old_points1))
            
        else:
            old_points=old_points1
            xx=old_points1
            flag=1


def sflow():


	cap = cv2.VideoCapture(0)
	# Create old frame
	_, frame = cap.read()
	old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Lucas kanade params
	lk_params = dict(winSize = (20,20),
	                 maxLevel = 4,
	                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
	# Mouse function

	        #old_points1=np.array(list(old_points).append([x,y]),dtype=np.float32)
	cv2.namedWindow("Frame2")
	cv2.setMouseCallback("Frame2", select_point)
	point_selected = False
	point = ()
	flag=0
	xx=0
	#yy=0
	old_points = np.array([[]])

	#old_points = np.array([[xx, yy]], dtype=np.float32)
	th1=100
	th2=100
	while True:
	    _, frame = cap.read()
	    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    if point_selected is True:
	        cv2.circle(frame, point, 5, (0, 0, 255), 2)
	        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lk_params)
	        old_gray = gray_frame.copy()
	        
	        z=new_points-xx
	        z1=z[:,0]
	        z2=z[:,1]
	        for f in range(len(z1)):
	            if  z1[f]>th1: 
	                print("enter 'h' for label or any key to continue")
	                key=cv2.waitKey(0)
	                if(key==ord('h')):
	                    label(i)
	            if  z2[f]>th2:
	                print("enter 'v' for label or any key to continue")
	                key=cv2.waitKey(0)
	                if(key==ord('v')):
	                    label(i)
	            if z1[f] >th1 and z2[f]>th2:
	                print("enter 'd' for label or any key to continue")
	                key=cv2.waitKey(0)
	                if(key==ord('d')):
	                    label(i)
	                

	        
	        for i,(new,old) in enumerate(zip(new_points,old_points)):
	            x,y = new.ravel()
	            c,d = old.ravel()
	            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
	        old_points = new_points
	        #x, y = new_points.ravel()
	        #
	    cv2.imshow("Frame2", frame)
	    key = cv2.waitKey(1)
	    if key == 27:
	        print(xx)
	        print("hi")
	        print(new_points)
	        break

	return


def dflow():
	global cap,currentframe
	cap.set(1,currentframe)
	ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    flag=0
    temp=0
    z2=0
    count=0
    #print("dflow")
    while(1):
        ret, frame2 = cap.read()
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        nx=0
        ny=0
        if (flag == 0):
            x = flow[0]
            y = flow[1]
            x1 = x**2
            y1 = y**2
            z1 = np.sqrt(np.sum(x1)+np.sum(y1))
            flag = 1
            count=count+1
        else:
            x = flow[0]
            y = flow[1]
            
            for i in range(np.shape(x)[0]):
                for j in range(np.shape(x)[1]):
                    if x[i,j]:
                        nx=nx+1
            for i in range(np.shape(x)[0]):
                for j in range(np.shape(x)[1]):
                    if y[i,j]:
                        ny=ny+1
                        
            x1 = x**2
            y1 = y**2
            z2=np.sqrt(np.sum(x1)+np.sum(y1))
                   
            temp = 1
            count=count+1
        print('z1-', z1)
        print('z2-', z2)
        print('z2-z1=', abs(z1-z2))
        c=max(nx,ny)

        if (temp == 1):
            z = (abs(z1 - z2))/c
            print(float(z))
            if (z >0.0 ):
                print("enter 'l' for label or any key to continue")
        
                cv2.imshow('frame',prvs)
                key = cv2.waitKey(0)
                
                if (key == 'l'):
                    label=str(input('enter the label'))
                #if (key==ord('s')):
                    #break
                    
        if temp==1:
            z1=z2
        cv2.imshow('frame',prvs)
        prvs=next
        k=cv2.waitKey(1)
        if k==27:
            break









add_menu()
add_radiobutton('No. of frames',ROW=0,COLUMN=0)
add_radiobutton('from',ROW=0,COLUMN=1)
add_radiobutton(ROW=0,COLUMN=2)
add_radiobutton('to',ROW=0,COLUMN=3)
add_radiobutton(ROW=0,COLUMN=4)
add_radiobutton('Add class',ROW=0,COLUMN=5)
add_radiobutton(ROW=0,COLUMN=6)

add_radiobutton(ROW=0,COLUMN=7)

add_radiobutton(ROW=0,COLUMN=8)

for k in range(40):
	add_radiobutton(ROW=k,COLUMN=9)

val=0

errorbox = Text(root,height=3)
errorbox.grid(row=24,column=1,rowspan=3,columnspan=3)



errorbox.insert('1.0',"initializing..............")

button.append(add_button("   create   ",create_class,2,5))
button.append(add_button("   >>   ",next_image,20,3))
button.append(add_button("   <<   ",prev_image,20,1))
button.append(add_button("   play   ",videoplay,20,2))
button.append(add_button("   predict   ",None,23,1))
#button.append(add_button("printclass",printclass,1,1))
#class text entry
entry.append(add_textentry(gp,1,5))




entry.append(add_textentry(from_frame,1,1))
entry.append(add_textentry(to_frame,1,3))
button.append(add_button("   catagorise   ",fromtoannotate,1,2))

#l = add_listbox(hgt=190,wdt=520,x1=10,y1=140)

l=Listbox(root,height=32,width=29,selectmode=SINGLE)
#l.place(relx=0.01,rely=0.2,height=520,width=190)
l.grid(row=0,column=0,rowspan = 32)
#sy = Scrollbar()

#sy.grid(row=0,column=0,rowspan = 50,sticky=E)
#sy.config(command = l.yview)
#l.config(yscrollcommand = sy.set)
l.bind("<Button-1>",listboxfn) 

add_checkbox(lble = 'annotate',vble = check ,cmd = dshow ,ROW=23,COLUMN=3)


#path text entry

'''
entry.append(add_textentry(paath,1,0))
entry[3].insert(0,"enter the input path ")
entry[3].bind("<Button-1>",cleartext1)

entry.append(add_textentry(output_path,2,0))
entry[4].insert(0,"enter output path")
entry[4].bind("<Button-1>",cleartext2)
'''


add_checkbox(lble = 'full load',vble = full ,ROW=4,COLUMN=0)


#button.append(add_button("   write file   ",writefile,3,4))
b1=Button(root,text='writefile',command=writefile)
b1.grid(row=1,column=4)
b1.config(bg='yellow')

#b2=Button(root,text='create folders',command=createfolder)
#b2.grid(row=2,column=4)

l1=ttk.Label(root,text="input file")
l1.grid(row=8,column=4)

l2=ttk.Label(root,text="output directory")
l2.grid(row=6,column=4)

#l3=ttk.Label(root,text="input directory")
#l3.grid(row=4,column=4)

l4=ttk.Label(root,text="No. of frames")
l4.grid(row=0,column=0)

l5=ttk.Label(root,text="From frame")
l5.grid(row=2,column=0)

entry.append(add_textentry(fframe,1,0))
#entry[3].insert(0,'')
entry[3].bind("<Button-1>",cleartext4)

#entry.append(add_textentry(paath,5,4))
#entry[4].bind("<Button-1>",cleartext1)
entry.append(0)


entry.append(add_textentry(output_path,7,4))
entry[5].bind("<Button-1>",cleartext2)

entry.append(add_textentry(file_path,9,4))
entry[6].bind("<Button-1>",cleartext3)


entry.append(add_textentry(first_frame,3,0))

errorbox.insert(END,"\ndone")

button.append(add_button("sparse optical flow",sflow,15,4))
entry.append(add_textentry(xthreshold,17,4))
entry.append(add_textentry(ythreshold,19,4))
l5=ttk.Label(root,text="x-threshold")
l5.grid(row=16,column=4)

l7=ttk.Label(root,text="y-threshold")
l7.grid(row=18,column=4)

button.append(add_button("dense optical flow",dflow,21,4))

#errorbox.insert('3.0',"abcdefgk")
#errorbox.delete('1.0',END)
for b in button:
	b.config(bg='yellow')

#button.append(add_button("   create folders   ",None,4,4))
#x=Scale(root,orient=HORIZONTAL,width=40,length=490,variable=slider,command=slide,from_=0,to=400)
#x.place(x=305,y=530,height=40,width=490)
root.geometry('1320x670+0+0')
root.mainloop()
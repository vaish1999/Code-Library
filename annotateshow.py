import cv2
import pandas
import sys
import os
import numpy as np

arguments  = sys.argv

print(arguments)

folderpath = arguments[1] 
if os.path.isfile(folderpath + '/classifiedcsv.csv'):
	file = pandas.read_csv(folderpath + '/classifiedcsv.csv')
	x = (file.ix[:,2])
	print(len(x))
	cap = cv2.VideoCapture(folderpath+'/'+folderpath+'.avi')
	ret  = True
	i=1
	while (ret):
		ret,frame = cap.read()
		if i >= len(x)-1:
			break
		if pandas.isna(x[i]) == False :
			cv2.putText(frame,x[i],(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1,cv2.LINE_AA)
		cv2.imshow("frame",frame)
		i = i+2
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
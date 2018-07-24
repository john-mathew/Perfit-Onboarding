from os import listdir
from os.path import isfile, join
import cv2
folder = "D:/Python"
images = [f for f in listdir(folder) if isfile(join(folder, f))] #Stores all files in array
print(images) #Prints the list of all files read
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

for image in images:
	img = cv2.imread(folder+"/"+image)
	cv2.imshow('image',img)
	cv2.waitKey(1000) #Change number for increasing or decreasing image duration 
cv2.destroyAllWindows()
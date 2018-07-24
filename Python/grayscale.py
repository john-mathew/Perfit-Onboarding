import cv2
import argparse
import os

ap = argparse.ArgumentParser() #Argument Parser
ap.add_argument("-i", required = True)
args = vars(ap.parse_args())

filename =  args["i"]
img = cv2.imread( filename ) #Filename given as command line argument
img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
cv2.imwrite( "gs.png", img ) #Output saved as png file

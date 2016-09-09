
from PIL import Image


def median(pixelList): # our median function 
	lengthOfImages = len(allImages)
	pixelList.sort() 
	median = (((lengthOfImages + 1)/2) - 1)
	return pixelList[median] # returning function of pixelList


# to load the image. 
im1 = Image.open('Project1Images/1.png')
im2 = Image.open('Project1Images/2.png')
im3 = Image.open('Project1Images/3.png')
im4 = Image.open('Project1Images/4.png')
im5 = Image.open('Project1Images/5.png')
im6 = Image.open('Project1Images/6.png')
im7 = Image.open('Project1Images/7.png')
im8 = Image.open('Project1Images/8.png')
im9 = Image.open('Project1Images/9.png')


allImages = [im1, im2, im3, im4, im5, im6, im7, im8, im9] # array containing all the images. 

for image in allImages: # print the size of each image. 
	print(image.size)
	
# dimensions of our images. 

imageWidth = 495
imageHeight = 557

newImage = Image.new("RGB", im1.size, (0, 0, 0))
newImageData = newImage.load() # creating a blank canvas for our image. 
for x in range(0, imageWidth): # rows or our width, going form 0 to 495
        for y in range(0, imageHeight): # columns or our height going from 0 to 557. 
                redPixelList = [] # new empty lists for red, green, blue
                greenPixelList = []
                bluePixelList = []

                for myImage in allImages: # create new pixel
                        data = myImage.load() # pixel access
                        pixel = data[x,y] # will give current pixel
                        redPixelList.append(pixel[0]) #index 0 = red
                        greenPixelList.append(pixel[1]) #index 1 = green
                        bluePixelList.append(pixel[2]) #index 2 = blue
                newImageData[x,y] = (median(redPixelList), median(greenPixelList), median(bluePixelList)) # calling our median functions for red green and blue. 
newImage.show() # gives us the image without the man walking around the statue. 
        

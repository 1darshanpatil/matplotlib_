import matplotlib.image as pmig                               # needed to read image
import matplotlib.pyplot as plt                          # to plot the array as image plt.imshow(array_of_image)
img_data = pmig.imread('path.format')    #This stores array of image to img_data
print(img_data) # prints the array of image
plt.imshow(img_data)

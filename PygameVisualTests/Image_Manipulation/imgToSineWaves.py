import cv2 
import numpy as np

low_res = (50,50)


# Load the image 
image = cv2.imread('images.jpg') 
    
# Convert the image to grayscale 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
img = cv2.resize(gray_image, low_res)

# print(np.amax(img))

# Save the grayscale image 
# cv2.imwrite('output_image.jpg', img) 

x = 149

y = round(x/255 * 10)

print(x, y)
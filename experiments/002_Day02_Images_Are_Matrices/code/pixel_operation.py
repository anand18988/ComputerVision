import cv2
import numpy as np
from pathlib import Path

# read image
file_path = Path(__file__).parent
root_folder = file_path.parent.parent.parent

image_path = root_folder/"datasets"/"raw"/"Ice Thumbnail.png"

img = cv2.imread(str(image_path))

print("shape: ", img.shape)

cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# pointing toward pixel
print("pointing toward a pixel and finding pixel value", img[10,10])

# setting values of the pixel
img[10:100,0:25] = (255,0,0)

img2 = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imshow("edited image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# finding where the pixel in the photo is white replace it with other color using mask

change_pixel_array = ((img[:,:,0]==255) & (img[:,:,1]==255) & (img[:,:,2]==255))
print("pixels with white color", change_pixel_array)

img[change_pixel_array]= (0,0,255)
cv2.imshow("changet white pixel to red",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# create new image
canvas = np.random.randint(0,255,size = (800,800),dtype = np.uint8)
cv2.imshow("noise", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

array = np.random.randint(0,255,size = (300,300))
canvas2 = array.astype(np.uint8)
cv2.imshow("noise", canvas2)
cv2.waitKey(0)
cv2.destroyAllWindows()




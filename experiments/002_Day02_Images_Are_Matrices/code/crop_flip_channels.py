import cv2
from pathlib import Path

script_folder_path = Path(__file__).parent
root_folder = script_folder_path.parent.parent.parent

img_path = root_folder/"datasets"/"raw"/"Ice thumbnail.png"

img = cv2.imread(str(img_path))

crop = img[10:800,100:500]

cv2.imshow("cropped ", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

# horizontal flip
cv2.imshow("Horizontal flip ",cv2.flip(crop,1))
cv2.waitKey(0)
cv2.destroyAllWindows()

# vertical flip
cv2.imshow("vertical flip ",cv2.flip(crop,0))
cv2.waitKey(0)
cv2.destroyAllWindows()

# split channels
b,g,r = cv2.split(img)

cv2.imshow("blue ", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("green ", g)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("red ", r)
cv2.waitKey(0)
cv2.destroyAllWindows()

merge_img = cv2.merge([r,g,b])
edited_image_path = root_folder/"datasets"/"processed"/"merge_img.png"
cv2.imshow("merged ", merge_img)
cv2.imwrite(edited_image_path, merge_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


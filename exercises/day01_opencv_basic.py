"""
-------------------------------------------------
Day 1 : OpenCV Basics

Author : Anand Pandey

Objectives

✔ Read an image
✔ Display an image
✔ Convert to grayscale
✔ Resize
✔ Rotate
✔ Draw rectangle
✔ Draw circle
✔ Add text
✔ Save image

-------------------------------------------------
"""
import cv2
from pathlib import Path

# Folder containing this script
script_dir = Path(__file__).parent
print(script_dir)

# Go to ComputerVision/datasets/images/newton.jpeg
image_path = script_dir.parent / "datasets" / "images" / "newton.jpeg"

img = cv2.imread(str(image_path))

if img is None:
    print("❌ Image not found!")
else:
    print("✅ Image loaded successfully!")
    print("Image shape:", img.shape)
    print(type(img))
    
cv2.imshow("Original Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized = cv2.resize(img, (100,300))
cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw rectangle
cv2.rectangle(img, (50,50), (250,200), (0,255,0), 3) # Top Left (50,50) Bottom Right (250,200) Green Thickness = 3

# Draw circle
cv2.circle(img, (350,150), 50, (255,0,0), 3)         # Center (300,150) Radius 50 pixels Blue Thickness 3

# Add text
cv2.putText(
    img,                                             # Text Location Font Scale Color Thickness
    "ShipVerse",
    (50,450),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0,0,255),
    2
)

# Show edited image
cv2.imshow("Edited", img)
cv2.imwrite("output.jpg", img)                        # saves image
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
from pathlib import Path

file_path = Path(__file__).parent

img_path = file_path.parent.parent.parent/'datasets'/'raw'/'Ice Thumbnail.png'

img = cv2.imread(str(img_path))

if img is None:
    print("could not find image")
else:
    print("image shape, dtype, size :", img.shape, img.dtype, img.size)
    height , width = img.shape[:2]
    print("height of image:", height)
    print("width of image:", width)
    channel = img.shape[2] if len(img.shape)== 3 else 1
    print('channel is: ', channel)


# Python Program to Find the Size (Resolution) of an Image
import PIL
from PIL import Image
img=PIL.Image.open("C:/Users/ADMIN/OneDrive/Pictures/PHOTOGRAPH (2).jpg")
width,height=img.size
print(width,"x",height)

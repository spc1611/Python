import os
from PIL import Image                               # pip install pillow
# from IPython.display import Image as Img
# from IPython.display import display               # Don't need to memorize just search and import

path = os.path.dirname(__file__)                    # To show where the images are
path = f"{path}/images"                             # More specifically 

img_list = os.listdir(path)
img_list_1 = [path + '/' + x for x in img_list]       # read "for x in img_list" first. then read "path + '/' + x". --> ex) ...images/07 jpg (format)
images = [Image.open(x) for x in img_list_1]          # This is for images opening: and the img_list here is different (overwritten) from the above img_list

file_name = input("Save File name : ")

gif_img = images[0]
gif_img.save(f'{file_name}.gif', save_all = True, append_images = images[1:], loop = 0xff, duration = 1000)     # No actual order. ":" = to the end, duration is miliseconds.




print(path)
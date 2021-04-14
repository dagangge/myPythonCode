from PIL import Image
import numpy as np

a=np.array(Image.open("d:\Source\myPythonCode\pillow\imagename.jpg").convert('L'))
print(a.shape)
print(a.dtype)
b=255-a
im=Image.fromarray(b.astype('uint8'))
im.save('d:\Source\myPythonCode\pillow\imagename3.jpg')

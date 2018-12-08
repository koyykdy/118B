
# coding: utf-8

# In[82]:


import PIL
from PIL import Image
from PIL import ImageStat

import cv2
import numpy as np

img = Image.open("C:/Users/iknne/Desktop/YO/cogsci/COGS 118B/Final/grayed_asl/grayed_asl_train/A+/A520+.jpg")

brightness = (ImageStat.Stat(img)).rms[0]

if brightness > 130:
    img_bright = img.point(lambda p: p * 0.8)
    
elif brightness <= 130:
        img_bright = img.point(lambda p: p * 2.0)

img_bright.show()
img = np.asarray(img_bright)

edges = cv2.Canny(img,20,25)

cv2.imshow("Edge Detected Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

imgarr = np.asarray(edges)
imgarr_1d = imgarr.reshape(-1)
print(imgarr.shape)
print(imgarr_1d.shape)

np.savetxt("A1+.csv", imgarr_1d, delimiter = ",")


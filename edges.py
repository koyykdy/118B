
# coding: utf-8

# In[216]:


import PIL
import os


import cv2
import numpy as np

size = (10,10)

img = cv2.imread("A1+.jpg")

img_ = 

edges = cv2.Canny(img,20,25)

#edges.resize(size)

cv2.imshow("Edge Detected Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

imgarr = np.asarray(edges)
imgarr_1d = imgarr.reshape(-1)
print(imgarr.shape)
print(imgarr_1d.shape)

np.savetxt("A1+.csv", imgarr_1d, delimiter = ",")


# In[215]:


img = cv2.imread("A510+.jpg")

edges = cv2.Canny(img,20,25)

cv2.imshow("Edge Detected Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

imgarr = np.asarray(edges)
imgarr_1d = imgarr.reshape(-1)
print(imgarr.shape)
print(imgarr_1d.shape)

np.savetxt("A1+.csv", imgarr_1d, delimiter = ",")


# In[120]:


img = cv2.imread("A1.jpg")
edges = cv2.Canny(img,0,791)

cv2.imshow("Edge Detected Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


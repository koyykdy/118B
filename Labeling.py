
# coding: utf-8

# In[19]:


#Ignore the commented out code, that was me trying to attempt an alternate approach.
#For now, it seems that my computer is unable to produce an array of the size that we need.
#However, I believe that at the very least the script itself is on the right track towards what we need for this part of the project
#Please remember to change the path for the files in your local computer

from PIL import Image
import numpy as np

letters = np.matrix(('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','nothing'))
#I tranpose the array below later on so do not worry about the shape for now. This was to make it easier for me to understand
#as I was writing the code
labeled = np.empty([81000,40001])

for i in range(0,27):
    #currentLabel = np.empty([3000,40001])
    for j in range(0,3000):
        img = Image.open('C:/Users/Brian Suh/Desktop/118B FP/grayed_asl_train/'+str(letters[0,i])+'+/'+str(letters[0,i])+str(j+1)+'+.jpg')
        imgArray = np.array(img)
        flattened = np.ravel(imgArray)
        incLabel = np.append(flattened,i)
        #currentLabel = np.vstack((currentLabel,incLabel))
        labeled = np.vstack((labeled,incLabel))
        
labeled = np.transpose(labeled)
print(labeled.size)


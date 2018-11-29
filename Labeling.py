from PIL import Image
import numpy as np
import csv

letters = np.matrix(('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','nothing'))

with open('C:/Users/cjaik/Desktop/ASL/labeled_asl.csv',mode='w') as file:
    file_writer = csv.writer(file,delimiter=',')
    for i in range(len(letters)):
        #currentLabel = np.empty([3000,40001])
        for j in range(0,3000):
            img = Image.open('C:/Users/cjaik/Desktop/ASL/grayed_asl/grayed_asl_train/'+str(letters[0,i])+'+/'+str(letters[0,i])+str(j+1)+'+.jpg')
            imgArray = np.array(img)
            flattened = np.ravel(imgArray)
            incLabel = np.append(flattened,i)
            
            file_writer.writerow(incLabel)
from PIL import Image
import numpy as np
import csv

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','nothing']

with open('C:/Users/cjaik/Desktop/ASL/labeled_asl.csv', newline = '', mode='w') as file:
    file_writer = csv.writer(file,delimiter=',')
        print(letters[i])
        for j in range(0,3000):
            img = Image.open('C:/Users/cjaik/Desktop/ASL/grayed_asl/grayed_asl_train/'+str(letters[i])+'+/'+str(letters[i])+str(j+1)+'+.jpg')
            imgArray = np.array(img)
            flattened = np.ravel(imgArray)
            incLabel = np.append(i,flattened)
            
            file_writer.writerow(incLabel)
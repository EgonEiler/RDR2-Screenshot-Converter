import glob
import os
import sys

origImgPath = input("Input the path to the original RDR2 Images. (Type exit to abort)")
if(origImgPath == "exit"):
    sys.exit()
resultImgPath = input("Input the path to the folder where the new images will be saved. (Type exit to abort)")
if(resultImgPath == "exit"):
    sys.exit()

imgFileNames = glob.glob(origImgPath+"/*") #"./rdr2_img/*"

for imgName in imgFileNames:
    imgBasename = os.path.basename(imgName)
    
    fr = open(imgName, "rb")
    text = fr.read()
    headerLocation = 0
    
    for i in range(0,len(text) - 3): 
        # Searches for the magic string. All following bytes are then copied to the new file
        if(text[i]==255 and text[i + 1]==216 and text[i + 2]==255 and text[i + 3]==224):
            headerLocation = i
            break
           
    fr.close()

    fw = open(resultImgPath+"/"+imgBasename+".jpeg", "wb") #"./result/"
    fw.write(text[headerLocation:])
    fw.close()

    


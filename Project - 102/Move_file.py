import os
import shutil

fromdir = 'C:/Users/anvit/Downloads'
todir = 'C:/Document files'
list_of_files = os.listdir(fromdir)
print(list_of_files)

for fileName in list_of_files:
    root , extensions = os.path.splitext(fileName)
    print(root)
    print(extensions)

    if extensions == '':
        continue
    if extensions in ['.txt' , '.docx' , '.doc' , '.pdf']:
        path1 = fromdir + '/' + fileName
        path2 = todir + '/' + "Document files"
        path3 = todir + '/' + "Document files" + fileName

        print("path1" , path1)
        print("path3" , path3)

        if os.path.exists(path2):
            print("moving" + fileName + "...")
            shutil.move(path1 , path3)

        else:
            os.makedirs(path2)
            print("moving" + fileName + "....")
            shutil.move(path1 , path3)
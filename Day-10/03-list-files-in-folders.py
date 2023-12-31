# let's create a program to list the files inside a folder
import os
folders = input("please provide list of folders name with a space between: ").split()

if len(folders)<=0 :
    print("please give at least one input")
    
for folder in folders:
    try:
        files= os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name: ")
        break
# this will give us only folder but we cant files as well.
    for file in files:
        print(file)    
## What if user gives a folder which does not exists in our system.
    
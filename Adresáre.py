import os
userinp=input("Napíš cestu, z ktorej si prosíš vypísať priečinky: ")
def files(directory, level=0):
    for item in os.listdir(directory):
        if os.path.isdir(directory+"\\"+item) and item[0] not in ".$":
            if len(os.listdir(directory+"\\"+item))!=0:
                print("-",' '*level,item)
                files(directory+"\\"+item,level+1)
files(userinp)
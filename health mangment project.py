#import datetime
#l=datetime.datetime.now()
#print(l)
def gettime():
    import time
    return time.asctime(time.localtime(time.time()))
print("todays date is",gettime())
def store_diet():
    #this funtion is to store diet
    with open("file_diet.txt","a+") as f:
        time=str(gettime())
        take_diet=input("enter your todays diet:")
        f.write("["+time+"]")
        f.write("\t"+take_diet+"\n")
def store_exersise():
    with open("file_exr.txt","a+") as f:
        time=str(gettime())
        take_exr=input("enter your todays exersise:")
        f.write("["+time+"]")
        f.write("\t"+take_exr+"\n")
def retrive_diet():
        with open("file_diet.txt","r") as f:
           print(f.read())
def retrive_exer():
        with open("file_exr.txt","r") as f:5

print(".......welcome to my heath management file..............")
while(1):
    print("press.1 store diet\npress 2. store exercise\npress 3. retrive diet\npress 4.retrive exercise\npress 5.exit")
    n=int(input("enter your choice:"))
    if n==1:
        store_diet()
    elif n==2:
        store_exersise()
    elif n==3:
        retrive_diet()
    elif n==4:
        retrive_exer()
    elif n==5:
        break
    else:
        print("enter correct choice")


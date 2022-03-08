#Assignment 5
# Ques1
#GST Rate Calculator
from tkinter import * # Importing Tkinter module
def calc(): #Defining calc function for calculation of GST rate
    global gst
    if(netprice.get().isdecimal()==False):
        gst.set("Invalid Input") #If the Output Does Not Contain Numbers
        g.update() #Screen Shows Invalid Input
    else:
        gstrate = ((float(netprice.get()) - float(originalcost.get())) * 100) / float(originalcost.get())
        if (gstrate >= 0): #If The gst rate comes positive only then the screen is updated with rate
            gst.set(gstrate)
            g.update()
        else: #Else the screen will show Invalid Input
            gst.set("Invalid Input")
            g.update()



root=Tk() #Creating A New GUI Window
root.geometry("300x200") #Defining Size of GUI Window
root.maxsize(300,200) #Setting Maximum Limit of GUI Window Size
root.minsize(300,200) #Setting Minimum Limit of GUI Window Size
lab1=Label(text="GST Tax Finder Calculator",font="comicsans 10 bold") # Defining Heading of The GUI Window
lab1.grid(row=0,column=1) #Packing The Label in form of grid
np1=Label(text="Net Price:") #Defining Label
np1.grid(row=1,column=0) #Packing The Label in form of grid
#Creating three String Variable
netprice=StringVar()
originalcost=StringVar()
gst=StringVar()
#Creating Entry Column
e1=Entry(root,textvariable=netprice,font="comicsans 10 bold")
e1.grid(row=1,column=1)
#Creating Label
oc1=Label(text="Original Cost:")
oc1.grid(row=2,column=0) #Packing The Label in form of grid
oc=Entry(root,textvariable=originalcost,font="comicsans 10 bold") #Creating Entry
oc.grid(row=2,column=1)  #Packing The Label in form of Grid
cal=Button(text="Calculate GST Rate",command=calc) #Creating a button named Calculate GST Rate
cal.grid(row=3,column=1) #Packing The Label in form of grid
g1=Label(text="GST Rate:")#Creating Label
g1.grid(row=4,column=0)#Packing The Label in form of grid
g=Entry(root,textvariable=gst,font="comicsans 10 bold")#Creating Label
g.grid(row=4,column=1)#Packing The Label in form of grid
root.mainloop()

#Ques 2
#Calendar

from tkinter import * #Importing Tkinter Module
import calendar #Importing Calendar Module

root=Tk()
def cal1(): #cal1 function is defined
    global year
    new=Tk() # A New GUI is created
    new.geometry("600x700") #Defining Size of GUI Window
    root.minsize(600, 700)#Setting Minimum Limit of GUI Window Size
    root.maxsize(600, 700)#Setting Maximum Limit of GUI Window Size
    l1=Label(new,text=(calendar.calendar(int(year.get()))), font = "Consolas 10 bold") #Creating Label
    l1.grid(row=0,column=0,padx=30)#Packing The Label in form of grid and padding it in X Axis
    new.mainloop()
root.geometry("200x200")#Defining Size of GUI Window
root.minsize(200,200)#Setting Maximum Limit of GUI Window Size
root.maxsize(200,200)#Setting Minimum Limit of GUI Window Size
#Creating Label and providing font style comicsans font size=10 and bold in style
heading=Label(text="Calendar",font="comicsans 10 bold")
heading.place(x=80,y=1)#Using place to pack the label
year1=Label(text="Enter Year: ")#Creating Label
year1.place(x=0,y=30)#Using place to pack the label
year=StringVar() #Creating String Variable
e2=Entry(root,textvariable=year) # Creating Entry Label
e2.place(x=60,y=30) #Using place to pack the label

cal=Button(text="Show Calendar",command=cal1) #Creating Button
cal.place(x=60,y=50) #Packing The button using place function


root.mainloop()

#Ques 3
#Calculator
from tkinter import *

def b0i(): #Creating a function to add 0 in String Variable
    global ent
    ent.set(ent.get()+'0') #Adding 0 to the string
    inoutvar.update() #Updating the screen
def b1i(): #Creating a function to add 1 in String Variable
    global ent
    ent.set(ent.get()+'1') #Adding 1 to the string
    inoutvar.update() #Updating the screen
def b2i(): #Creating a function to add 2 in String Variable
    global ent
    ent.set(ent.get()+'2')#Adding 2 to the string
    inoutvar.update() #Updating the screen
def b3i(): #Creating a function to add 3 in String Variable
    global ent
    ent.set(ent.get()+'3')#Adding 3 to the string
    inoutvar.update() #Updating the screen
def b4i(): #Creating a function to add 4 in String Variable
    global ent
    ent.set(ent.get()+'4')#Adding 4 to the string
    inoutvar.update() #Updating the screen
def b5i(): #Creating a function to add 5 in String Variable
    global ent
    ent.set(ent.get()+'5')#Adding 5 to the string
    inoutvar.update() #Updating the screen
def b6i(): #Creating a function to add 6 in String Variable
    global ent
    ent.set(ent.get()+'6')#Adding 6 to the string
    inoutvar.update() #Updating the screen
def b7i(): #Creating a function to add 7 in String Variable
    global ent
    ent.set(ent.get()+'7')#Adding 7 to the string
    inoutvar.update() #Updating the screen
def b8i(): #Creating a function to add 8 in String Variable
    global ent
    ent.set(ent.get()+'8')#Adding 8 to the string
    inoutvar.update() #Updating the screen
def b9i(): #Creating a function to add 9 in String Variable
    global ent
    ent.set(ent.get()+'9')#Adding 9 to the string
    inoutvar.update() #Updating the screen
def clear(): #Creating the clear function to clear the string
    global ent
    ent.set("")
    inoutvar.update() #Update the Screen
def equal():
    global ent
    variable=eval(inoutvar.get()) #Creating A Variable and using eval function to calculate the value
    ent.set(variable) #Setting the String
    inoutvar.update() #Update the screen


def plus(): #Creating a function to add plus in string
    global ent
    ent.set(ent.get() + '+')#Setting the String
    inoutvar.update()#Update the screen

def sub():#Creating a function to add subtract in string
    global ent
    ent.set(ent.get()+'-')#Setting the String
    inoutvar.update()#Update the screen


def mul(): #Creating a function to add multiply in string
    global ent
    ent.set(ent.get() + '*') #Setting the String
    inoutvar.update()#Update the screen


def div(): #Creating a function to add division in string
    global ent
    ent.set(ent.get() + '/') #Setting the String
    inoutvar.update() #Update the screen
def dot(): #Creating a function to add division in string
    global ent
    ent.set(ent.get() + '.') #Setting the String
    inoutvar.update() #Update the screen
def power(): #Creating a function to add division in string
    global ent
    ent.set(ent.get() + '**') #Setting the String
    inoutvar.update() #Update the screen

root=Tk()
root.geometry("400x440") #Defining Size of GUI Window
root.minsize(400,440) #Setting Minimum Limit of GUI Window Size
root.maxsize(400,440) #Setting Maximum Limit of GUI Window Size
label1=Label(text="Calculator",font="comicsans 20 bold") #Creating Label
label1.pack(padx=20) #Packing the Label
ent=StringVar() #Creating a String Variable
inoutvar=Entry(textvariable=ent,font="comicsans 30 bold") #Creating a Entry Column
inoutvar.pack(padx=10) #Packing the entry column and padding it

button0=Button(text="0",padx=20, command=b0i,font="comicsans 14 bold") #Creating a button named 0 and given a command to add 0 in the string
button0.place(x=160,y=220) #Placing it at (160,220)
button1=Button(text="1",padx=20, command=b1i,font="comicsans 14 bold")#Creating a button named 1 and given a command to add 1 in the string
button1.place(x=80,y=100) #Placing it at (80,100)
button2=Button(text="2",padx=20, command=b2i,font="comicsans 14 bold")#Creating a button named 2 and given a command to add 2 in the string
button2.place(x=160,y=100)#Placing it at (160,100)
button3=Button(text="3",padx=20, command=b3i,font="comicsans 14 bold")#Creating a button named 3 and given a command to add 3 in the string
button3.place(x=240,y=100)#Placing it at (240,100)
button4=Button(text="4",padx=20, command=b4i,font="comicsans 14 bold")#Creating a button named 4 and given a command to add 4 in the string
button4.place(x=80,y=140)#Placing it at (80,140)
button5=Button(text="5",padx=20, command=b5i,font="comicsans 14 bold")#Creating a button named 5 and given a command to add 5 in the string
button5.place(x=160,y=140)#Placing it at (160,140)
button6=Button(text="6",padx=20, command=b6i,font="comicsans 14 bold")#Creating a button named 6 and given a command to add 6 in the string
button6.place(x=240,y=140)#Placing it at (240,140)
button7=Button(text="7",padx=20, command=b7i,font="comicsans 14 bold")#Creating a button named 7 and given a command to add 7 in the string
button7.place(x=80,y=180)#Placing it at (80,180)
button8=Button(text="8",padx=20, command=b8i,font="comicsans 14 bold")#Creating a button named 8 and given a command to add 8 in the string
button8.place(x=160,y=180)#Placing it at (160,180)
button9=Button(text="9",padx=20, command=b9i,font="comicsans 14 bold")#Creating a button named 9 and given a command to add 9 in the string
button9.place(x=240,y=180)#Placing it at (240,180)
buttondot=Button(text=".",padx=20, command=dot,font="comicsans 14 bold")#Creating a button named . and given a command to add . in the string
buttondot.place(x=80,y=220,width=67)#Placing it at (80,220)
buttonpower=Button(text="^",padx=20, command=power,font="comicsans 14 bold")#Creating a button named ^ and given a command to add ** in the string
buttonpower.place(x=240,y=220,width=67)#Placing it at (240,220)
buttonplus=Button(text="+",padx=20, command=plus,font="comicsans 14 bold")#Creating a button named + and given a command to add + in the string
buttonplus.place(x=80,y=260,width=67)#Placing it at (80,260)
buttonsub=Button(text="-",padx=20, command=sub,font="comicsans 14 bold")#Creating a button named - and given a command to add - in the string
buttonsub.place(x=160,y=260,width=67)#Placing it at (160,260)
buttonmul=Button(text="X",padx=20, command=mul,font="comicsans 14 bold")#Creating a button named X and given a command to add X in the string
buttonmul.place(x=240,y=260,width=67)#Placing it at (240,260)
buttondiv=Button(text="/",padx=20, command=div,font="comicsans 14 bold")#Creating a button named / and given a command to add / in the string
buttondiv.place(x=80,y=300,width=67)#Placing it at (80,300)
buttonequal=Button(text="=",padx=20, command=equal,font="comicsans 14 bold")#Creating a button named = and given a command to evaluate and update the string
buttonequal.place(x=160,y=300,width=67)#Placing it at (160,300)
buttonclear=Button(text="C",padx=20, command=clear,font="comicsans 14 bold")#Creating a button named C and given a command to clear the string
buttonclear.place(x=240,y=300,width=67)#Placing it at (240,300)
root.mainloop()


#Ques 4
#Defining Quicksort Function
def QuickSort(array,start,end):
    if(start>=end): #If a single element or no element is there return
        return
    pivot=start #Creating a Variable with value of start
    count=start #Creating a Variable with value of start
    for i in range(start+1,end): #Counting number of terms less than or equal to pivot point
        if(array[i]<=array[pivot]):
            count+=1
    temp=array[pivot] #Substituting the value at pivot point with value at start
    array[pivot]=array[count]
    array[count]=temp
    pivot=count #replacing the previous value of pivot point with count
    i=start #defining two variable one from start and another from end
    j=end-1
    while(i<pivot and j>pivot):
        if(array[i]>array[pivot] and array[j]<=array[pivot]):
            temp = array[i] #Creating a while loop to shift number less than or equal to pivot on its left and greater than that on its right
            array[i] = array[j]
            array[j] = temp
            i+=1
            j-=1
        elif(array[j]>array[pivot]):
            j-=1
        elif(array[i]<=array[pivot]):
            i+=1
    QuickSort(array,start,pivot) #Calling the function for the left part of pivot
    QuickSort(array,pivot+1,end) #Calling the function for the right part of pivot

def Mergesort(array,start,end):
    size=end-start #size is defined
    if(size<=1): #if size of list is less than or equal to 1 return
        return
    else:
        mid=(start+end)//2  #defined a mid which is having value equal to (start+end)/2 floor division

        Mergesort(array,start,mid) #Calling the function for the left half part
        Mergesort(array,mid,end) #Calling the function for the right half part
        result=[0]*size #created a new list of the size equal to the size of input list
        i=start #Starting variable defined
        j=mid #another variable with value of mid is defined
        count=0
        # While loop is created for sorting the elements across the array if the starting index is less than mid and ending index is less than end index
        while(i<mid and j<end):
            if(array[i]<=array[j]):
                result[count]=array[i]
                i+=1
            elif(array[i]>=array[j]):
                result[count]=array[j]
                j+=1
            count+=1
        if(i==mid and j<end):#If the starting point is equal to mid but the end point is not equal to end of list
            while(j<end):
                result[count]=array[j]
                j+=1
                count+=1
        if (j == end and i < mid): #If the starting point is not equal to mid but the ending index is at end of the list
            while (i < mid):
                result[count] = array[i]
                i+=1
                count+=1

        for i in range(size): #Replacing the elements of the original list with the new list
            array[i+start]=result[i]
print("Question 4")
list1=list(map(int,input("Enter The Numbers:\n").split()))
print("List Entered By User:",list1) #Printing the input list
Mergesort(list1,0,len(list1)) #Using Merge Sort to sort the list
print("Sorted List Using Merge Sort:",list1)
QuickSort(list1,0,len(list1)) #Using Quick Sort to sort the list
print("Sorted List Using Quick Sort:",list1)

#Ques 5
#Using Merge Sort to Sort The list
def Mergesort(array,start,end):
    size=end-start
    if(size<=1):
        return
    else:
        mid=(start+end)//2

        Mergesort(array,start,mid)
        Mergesort(array,mid,end)
        result=[0]*size
        i=start
        j=mid
        count=0
        while(i<mid and j<end):
            if(array[i]<=array[j]):
                result[count]=array[i]
                i+=1
            elif(array[i]>=array[j]):
                result[count]=array[j]
                j+=1
            count+=1
        if(i==mid and j<end):
            while(j<end):
                result[count]=array[j]
                j+=1
                count+=1
        if (j == end and i < mid):
            while (i < mid):
                result[count] = array[i]
                i+=1
                count+=1

        for i in range(size):
            array[i+start]=result[i]

#BinarySearch Function
def Binarysearch(list,number):
    start=0
    end=len(list)
    indicator=False
    while(start<=end):
        mid=(start+end)//2
        if(list[mid]==number):
            indicator=True
            break
        elif(list[mid]>number):
            end=mid-1
        elif(list[mid]<number):
            start=mid+1
    return indicator

print("Question 5")
#Taking Input of list from User and converting it into list directly
list_user=list(map(int,input("Enter The Numbers:\n").split()))
print("List Entered By User:",list_user)
#Sorting the list using Merge Sort
Mergesort(list_user,0,len(list_user))
print("Sorted List:",list_user)
#Taking Input from user to check the number
number_check=int(input("Enter The Number You Want To Check:\n"))

#Printing the result, if the number present in the list entered by user using binary search
print("If the Number is Present:",Binarysearch(list_user,number_check))
#Counting the number of times the number has appeared in list
if(Binarysearch(list_user,number_check)==True):
     print("Number of times the number entered by user appeared:",list_user.count(number_check))

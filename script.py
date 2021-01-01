import threading 
import math
from threading import*
import time
import collections
d={} # as json file
def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") 
    else:
        if key.isalpha():
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("Error: Memory limit exceeded!! ")
        else:
            print("Error: Invalind key_name!! key_name must contain only alphabets and no special characters and numbers allowed")


            
def read(key):
    if key not in d:
        print("Error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("Error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri



def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key deleted successfully")
            else:
                print("Error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key deleted successfully")



def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("Error: given key does not exist in database. Please enter a valid key") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("Error: time-to-live of",key,"has expired") 
    else:
        if key not in d:
            print("Error: given key does not exist in database. Please enter a valid key") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
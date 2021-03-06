
import csv
import time 
import sys
import re
from classes import *
s = time.time()

def display(results):
    print "="*20
    print "Meanings for",results["key"]
    print "="*20

    print results["key"], "~",results["pos"]
    i = 1
    for value in results["values"]:
        print str(i)+".",value
        i += 1 

def getMeanings(dicto,args):
    for arg in args:
        results,exact = dicto.getValue(arg)
        if results == None or len(results) < 1:
            print "No results Found"

        if exact:
            display(results)
        else:
            for result in results:
                display(result)

dicto = Dictionary("resources/eng2te.csv")

getMeanings(dicto,tuple(sys.argv[1:]))

print "Fetched Results in",time.time() - s ,"Seconds"

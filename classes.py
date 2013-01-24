
import csv
import re

class Dictionary:
    def __init__(self,loadfile):
        self.words = {}
        try:
            with open(loadfile) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    self.words[row[0]] = [row[1]," ".join(row[2:-1])]
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)

    def getValue(self,arg,re_search = True):
        if arg.title() in self.words:
            return self.getResults(arg.title()),True
        elif re_search:
            results = []
            for key in self.words.keys():
                if re.search(arg,key):
                   results.append(self.getResults(key))
        return results,False

    
    def getResults(self,arg):
        rdict = {}
        rdict["key"] = arg
        rdict["pos"] = self.words[arg][0]
        results = self.words[arg][1].replace("*",arg+" ")
        lines = results.split(".")
        rdict["values"] = []
        for line in lines:
            if line not in ["\n",""]:
                rdict["values"].append(line.strip(" \n\t\r"))
        
        return rdict

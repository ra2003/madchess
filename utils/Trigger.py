import re
import json

class Trigger:
    def __init__(self, module):
        self.module = module

        with open(module, 'r') as f:
            data = f.read()

        rgx = json.loads(data)

        self.web = {}

        for i in rgx.keys():
            self.web[i] = re.compile(*rgx[i])
            
    def match(self, data):
        for i in self.web.keys():
            matched = self.web[i].match(data)
            
            if matched != None:
                return (i, matched)

        return matched
    
    def matchall(self, data):
        for i in self.web.keys():
            matched = self.web[i].match(data)
        
            if matched != None:
                yield((i, matched))
   
    def search(self, data):
        for i in self.web.keys():
            matched = self.web[i].search(data)
            
            if matched != None:
                return (i, matched)

    def searchall(self, data):
         for i in self.web.keys():
            matched = self.web[i].search(data)
            
            if matched != None:
                yield(i, matched)

    
    def find(self, data, mins, maxs):
        for i in self.web.keys():
            found = self.web[i].findall(data)
            
            if found != None:
                if len(found) >= mins and len(found) <= maxs:
                    return (i, found)

   
    def findall(self, data, mins, maxs):
        for i in self.web.keys():
            found = self.web[i].findall(data)
            
            if found != None:
                if len(found) >= mins and len(found) <= maxs:
                    yield(i, found)


    def finditer(self, data, mins, maxs):
        for i in self.web.keys():
            found = self.web[i].finditer(data)
            
            if found != None:
                if len(found) >= mins and len(found) <= maxs:
                    return found

    def finditerall(self, data, mins, maxs):
        pass
    
    

     


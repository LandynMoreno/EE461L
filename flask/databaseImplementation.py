from pymongo import MongoClient

class database:

    def _init__(self):
        myclient = MongoClient("mongodb+srv://tester:helloworld@cluster0.wsoqa.mongodb.net/project?retryWrites=true&w=majority")
        self.client = myclient
        self.__db = myclient.ProjectUsers

    def createdocuments(self, name, description, ids):
        exist = "project already exists"
        dne = "project does not exist"
        if (self.__db.Projects.find_one({"ids":ids}) != None):
            return exist
        else:
            project = {
                "name": name,
                "description": description,
                "ids": ids,
                "hardware": 0
            }
        self.__db.Projects.insert_one(project)
        #maybe i should check if it successfully gets inserted?
        if (self.__db.Projects.find_one({"ids":ids}) != None):
            return exist
        else:
            return dne

    def getproject(self, ids):
        exist = "project already exists"
        dne = "project does not exist"
        if (self.__db.Projects.find_one({"ids": ids}) != None):
            check =  self.__db.Projects.find_one({"ids":ids})
            return check
        else:
            return dne

    def deleteProject(self, ids):
        exist = "project already exists"
        dne = "project does not exist"
        if (self.__db.Projects.find_one({"ids": ids}) != None):
            self.__db.Projects.delete_one({"ids": ids})
            return 0
        else:
            return dne

    def list(self):
        for project in self.__db.Projects.find():
            #might be wrong, maybe have to print out a list? instead of each project
            print(project)

        return 0

    def createhw(self, name, capacity):
        exist = "project already exists"
        dne = "project does not exist"
        if(self.__db.hwcollection.find_one({"name": name}) != None):
            return exist

        hw = {"name": name,
              "capacity": capacity,
              "availability": capacity
              }

        self.__db.hwcollection.insert_one(hw)

        if (self.__db.hwcollection.find_one({"name":name}) != None):
            return exist
        else:
            return dne

    def gethw(self, name):
        dne = "project does not exist"
        if(self.__db.hwcollection.find_one({"name":name}) != None):
            check = self.__db.hwcollection.find_one({"name":name})
            return check
        else:
            return dne

    def checkout(self, qty, names, ids):
        invalidinput = "invalid input"

        if(self.gethw(names) != None or self.getproject(ids) != None): #check if both of the inputs are valid

            checkouts = self.gethw(names)
            checkproj = self.getproject(ids) #assigns both of the projects to variables

            if(qty < 0): #no non negative qty's
                return invalidinput

            availability = checkouts["availability"] #assign variables to availability and project hw amount
            hw = checkproj["hardware"]

            if(qty <= availability): #check if qty wanted to check out is less total available
                changevalue = {"$set": {"availability": availability - qty}} #
                changevalue2 = {"$set": {"hardware": qty + hw}}

                self .__db.hwcollection.update_one({"name":names}, changevalue)
                self.__db.Projects.update_one({"ids": ids}, changevalue2)
                return 0
            else: #if not, take everything out and leave 0 left
                changevalue = {"$set": {"availability": 0}}
                changevalue2 = {"$set": {"hardware": availability + hw}}

                self.__db.hwcollection.update_one({"name":names}, changevalue)
                self.__db.Projects.update_one({"ids": ids}, changevalue2)
                return 0

    def checkin(self, qty, names, ids):
        invalidinput = "invalid input"
        if (self.gethw(names) != None or self.getproject(ids) != None):
            checkouts = self.gethw(names)
            checkproj = self.getproject(ids)
            if (qty < 0):
                return invalidinput

            availability = checkouts["availability"]
            capacity = checkouts["capacity"]
            hw = checkproj["hardware"]

            if(qty <= hw):
                if(qty<= capacity - availability):
                    checkinvalue = {"$set": {"availability": availability + qty}}
                    changevalue2 = {"$set": {"hardware": hw - qty}}
                    self.__db.hwcollection.update_one({"name":names}, checkinvalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0
                else:
                    checkinvalue = {"$set": {"availability": capacity}}
                    changevalue2 = {"$set": {"hardware": hw - (capacity - qty)}}
                    self.__db.hwcollection.update_one({"name":names}, checkinvalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0

    def hwlist(self):
        for hw in self.__db.hwcollection.find():
            #might be wrong, maybe have to print out a list? instead of each project
            print(hw)

        return 0

#need to add in project resources function, made most of the functions for it
    def mainfunc(self, name, ids, input, qty):
        nothing = "nonexistent project or hwset"
        invalid = "invalid"
        hw = self.gethw(name)
        proj = self.getproject(ids)
        if(hw == None or proj == None):
            return nothing
        if (input == "in"):
            self.checkin(self, qty, name, ids)
        else:
            self.checkout(self, qty, name, ids)


    def endconnection(self):
        self.client.close()

from pymongo import MongoClient

class database:

    def _init__(self):
        myclient = MongoClient("mongodb+srv://plp635:epic_k1d*@cluster0.invpm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.client = myclient
        self.__db = myclient.ProjectUsers

    def createdocuments(self, name, description, id):
        exist = "project already exists"
        dne = "project does not exist"
        if (self.__db.Projects.find_one({"id":id}) != None):
            return exist
        else:
            project = {
                "name" : name,
                "description" : description,
                "id": id,
                "hardware": 0
            }
        self.__db.Projects.insert_one(project)
        #maybe i should check if it successfully gets inserted?
        if (self.__db.Projects.find_one({"id":id}) != None):
            return exist
        else:
            return dne

    def getproject(self, id):
        exist = "project already exists"
        dne = "project does not exist"
        if (self.__db.Projects.find_one({"id": id}) != None):
            check =  self.__db.Projects.find_one({"id":id})
            return check
        else:
            return dne

    def deleteProject(self, id):
        exist = "project already exists"
        dne = "project does not exist"
        if (self.__db.Projects.find_one({"id": id}) != None):
            self.__db.Projects.delete_one({"id": id})
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

        def checkout(self, qty, name, id,):
            invalidinput = "invalid input"

            if(self.gethw(name) != None or self.getproject(id) != None): #check if both of the inputs are valid

                checkout = self.gethw(name)
                checkproj = self.getproject(id) #assigns both of the projects to variables

                if(qty < 0): #no non negative qty's
                    return invalidinput

                availability = checkout["availability"] #assign variables to availability and project hw amount
                hw = checkproj["hardware"]

                if(qty <= availability): #check if qty wanted to check out is less total available
                    changevalue = {"$set": {"availability": availability - qty}} #
                    changevalue2 = {"$set": {"hardware": qty + hw}}

                    self.__db.hwcollection.update_one({"name":name}, changevalue)
                    self.__db.Projects.update_one({"id": id}, changevalue2)
                    return 0
                else: #if not, take everything out and leave 0 left
                    changevalue = {"$set": {"availability": 0}}
                    changevalue2 = {"$set": {"hardware": availability + hw}}

                    self.__db.hwcollection.update_one({"name":name}, changevalue)
                    self.__db.Projects.update_one({"id": id}, changevalue2)
                    return 0

        def checkin(self,qty, name, id):
            invalidinput = "invalid input"
            if (self.gethw(name) != None or self.getproject(id) != None):
                checkout = self.gethw(name)
                checkproj = self.getproject(id)
                if (qty < 0):
                    return invalidinput

                availability = checkout["availability"]
                capacity = checkout["capacity"]
                hw = checkproj["hardware"]

                if(qty <= hw):
                    if(qty<= capacity - availability):
                        checkinvalue = {"$set": {"availability": availability + qty}}
                        changevalue2 = {"$set": {"hardware": hw - qty}}
                        self.__db.hwcollection.update_one({"name":name}, checkinvalue)
                        self.__db.Projects.update_one({"id": id}, changevalue2)
                        return 0
                    else:
                        checkinvalue = {"$set": {"availability": capacity}}
                        changevalue2 = {"$set": {"hardware": hw - (capacity - qty)}}
                        self.__db.hwcollection.update_one({"name":name}, checkinvalue)
                        self.__db.Projects.update_one({"id": id}, changevalue2)
                        return 0

    def hwlist(self):
        for hw in self.__db.hwcollection.find():
            #might be wrong, maybe have to print out a list? instead of each project
            print(hw)

        return 0

#need to add in project resources function, made most of the functions for it
    def mainfunc(self, name, id, input, qty):
        nothing = "nonexistent project or hwset"
        invalid = "invalid"
        hw = self.gethw(name)
        proj = self.getproject(id)
        if(hw == None or proj == None):
            return nothing
        if (input == "in"):
            checkin(self, qty, name, id)
        else:
            checkout(self, qty, name, id)






    def endconnection(self):
        self.client.close()
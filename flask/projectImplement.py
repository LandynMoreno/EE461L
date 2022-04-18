from pymongo import MongoClient


class projectMan:
    def __init__(self):
        myClient = MongoClient("mongodb+srv://tester:helloworld@cluster0.wsoqa.mongodb.net/project?retryWrites=true&w=majority")
        self.client = myClient
        self.__db = myClient.project
    
    def getIdsStr(self, isHw):
        strToReturn = ""
        for proj in self.__db.Projects.find({},{ "_id": 0, "ids": 1, "isHw": 1}):
            if(proj['isHw'] == 0):
                strToReturn = strToReturn + proj["ids"] +", "
        
        return strToReturn
    
    def createProj(self, isHw, name, descript, ids):
        if self.__db.Projects.find_one({"ids": ids}) is not None:
            return "project already exists"
        else:
            project = {
                "isHw": isHw,
                "ids": ids,
                "name": name,
                "description": descript,
                "projectshw1": 0,
                "projectshw2": 0
            }
            self.__db.Projects.insert_one(project)


        if self.__db.Projects.find_one({"ids": ids}) is not None:
            return "Project Successfully Created"
        else:
            return "Project Creation was Unsuccessful"
        
    def checkExistence(self, ids):
        if self.__db.Projects.find_one({"ids": ids}) is not None:
            return "approved"
        else:
            return "No such project found"

    def getStatus(self, ids):
        if self.__db.Projects.find_one({"isHw": 1}) is not None:
            total = self.__db.Projects.find_one({"isHw": 1})
            capac1 = total['capac1']
            avail1 = total['avail1']
            capac2 = total['capac2']
            avail2 = total['avail2']
            currentProj = self.getproject(ids)
            currenthw1 = currentProj['projectshw1']
            currenthw2 = currentProj['projectshw2']
            name = currentProj['name']
            description = currentProj['description']
            info = {
                "capac1": capac1,
                "avail1": avail1,
                "capac2": capac2,
                "avail2": avail2,
                "currenthw1": currenthw1,
                "currenthw2": currenthw2,
                "name": name,
                "description": description,
                "message": "approved"
            }
            return info

        else:
            info = {
                "message": "no project database initialized"
            }
            return info

    def getproject(self, ids):
        if self.__db.Projects.find_one({"ids": ids}) is not None:
            check = self.__db.Projects.find_one({"ids": ids})
            return check
        else:
            return "project does not exist"

    def checkin(self, qty, ids, hwsetname):
        if(self.getproject(ids) is not None):
            curproj = self.getproject(ids)
            total = self.__db.Projects.find_one({"isHw": 1})
            availability1 =  total['avail1']
            usercheckoutnum1 = curproj['projectshw1']
            availability2 = total['avail2']
            usercheckoutnum2 = curproj['projectshw2']
            if(qty<0):
                return -1
            if hwsetname == "hwset1":
                if(qty<=usercheckoutnum1):
                    checkinvalue = {"$set": {"avail1": availability1+qty}}
                    bumpUser = {"$set":{'projectshw1': usercheckoutnum1-qty}}
                    self.__db.Projects.update_one({"ids": ids}, bumpUser)
                    self.__db.Projects.update_one({"isHw":1}, checkinvalue)
                    return 0
                else:
                    checkinvalue = {"$set": {"avail1": availability1+usercheckoutnum1}}
                    bumpUser = {"$set":{'projectshw1': 0}}
                    self.__db.Projects.update_one({"ids": ids}, bumpUser)
                    self.__db.Projects.update_one({"isHw":1}, checkinvalue)
                    return 0
            else:
                if(qty<=usercheckoutnum2):
                    checkinvalue = {"$set": {"avail2": availability2+qty}}
                    bumpUser = {"$set":{'projectshw2': usercheckoutnum2-qty}}
                    self.__db.Projects.update_one({"ids": ids}, bumpUser)
                    self.__db.Projects.update_one({"isHw":1}, checkinvalue)
                    return 0
                else:
                    checkinvalue = {"$set": {"avail2": availability2+usercheckoutnum2}}
                    bumpUser = {"$set":{'projectshw2': 0}}
                    self.__db.Projects.update_one({"ids": ids}, bumpUser)
                    self.__db.Projects.update_one({"isHw":1}, checkinvalue)
                    return 0

                #add else for if its too big and also fr hwset2
        return -1

    def checkout(self, qty, ids, hwsetname):
        if self.getproject(ids) is not None:
            curproj = self.getproject(ids)
            total = self.__db.Projects.find_one({"isHw": 1})
            availability1 =  total['avail1']
            usercheckoutnum1 = curproj['projectshw1']
            availability2 = total['avail2']
            usercheckoutnum2 = curproj['projectshw2']
            if(qty<0):
                return -1
            if hwsetname == "hwset1":          
                if(qty<=availability1):
                    checkoutvalue = {"$set": {"avail1": availability1-qty}}
                    bumpUser = {"$set":{'projectshw1': usercheckoutnum1+qty}}
                    self.__db.Projects.update_one({"ids": ids}, bumpUser)
                    self.__db.Projects.update_one({"isHw":1}, checkoutvalue)
                    return 0
                else:
                    checkoutvalue = {"$set": {"avail1": 0}}
                    bumpUser = {"$set":{'projectshw1': usercheckoutnum1+availability1}}
                    self.__db.Projects.update_one({"ids": ids}, bumpUser)
                    self.__db.Projects.update_one({"isHw":1}, checkoutvalue)
                    return 0
            else:
                if(qty<=availability2):
                    checkoutvalue = {"$set": {"avail2": availability2-qty}}
                    bumpUser = {"$set":{'projectshw2': usercheckoutnum2+qty}}
                    self.__db.Projects.update_one({"ids": ids}, bumpUser)
                    self.__db.Projects.update_one({"isHw":1}, checkoutvalue)
                    return 0
                else:
                    checkoutvalue = {"$set": {"avail2": 0}}
                    bumpUser = {"$set":{'projectshw2': usercheckoutnum2+availability2}}
                    self.__db.Projects.update_one({"ids": ids}, bumpUser)
                    self.__db.Projects.update_one({"isHw":1}, checkoutvalue)
                    return 0

        else:
            return -1
            #add else for if its too big and also fr hwset2
    

                


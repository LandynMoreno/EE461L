from pymongo import MongoClient

class database:

    def __init__(self):
        myClient = MongoClient(
            "mongodb+srv://tester:helloworld@cluster0.wsoqa.mongodb.net/project?retryWrites=true&w=majority")
        self.client = myClient
        self.__db = myClient.project

    def createdocuments(self, name, description, ids, capacity, username):
        if self.__db.Projects.find_one({"ids": ids}) is not None:
            return "project already exists"
        else:
            project = {
                "name": name,
                "description": description,
                "ids": ids,
                "hardware": 0,
                "hardwareSets": {
                    "hwset1": {
                        "capacity": capacity,
                        "availability": capacity
                    },

                    "hwset2": {
                        "capacity2": capacity,
                        "availability2": capacity
                    },
                },
                "users":{
                    username: ({"hwset1":0, "hwset2":0})

                    # username: {
                    #     "hwset1": 0,
                    #     "hwset2": 0 }
                    
                }
            }
        self.__db.Projects.insert_one(project)

        # check if it successfully gets inserted
        if self.__db.Projects.find_one({"ids": ids}) is not None:
            return "Project Successfully Created"
        else:
            return "Project Creation was Unsuccessful"
            
    def checkExists(self, ids, username):
        if self.__db.Projects.find_one({"ids": ids}) is not None:
            project = self.getproject(ids)
            userList = project['users']
            found = False
            for key in userList:
                if key == username:
                    found = True
            if(not found):
                userList[username] = ({"hwset1":0, "hwset2":0})
                changevalue = {"$set": {"users": userList}}

                self.__db.Projects.update_one({"ids": ids}, changevalue)

            return "approved"
            #insert username into the db here

        else:
            return "No such project found"

    def getproject(self, ids):
        if self.__db.Projects.find_one({"ids": ids}) is not None:
            check = self.__db.Projects.find_one({"ids": ids})
            return check
        else:
            return "project does not exist"

    def deleteProject(self, ids):
        if self.__db.Projects.find_one({"ids": ids}) is not None:
            self.__db.Projects.delete_one({"ids": ids})
            return "Project has been successfully deleted"
        else:
            return "project does not exist"

    def list(self):
        for project in self.__db.Projects.find():
            # might be wrong, maybe have to print out a list? instead of each project
            print(project)

        return 0



    def checkout(self, qty, ids, hwsetname):
        invalidinput = "invalid input"

        if self.getproject(ids) is not None:  # check if the project exists

            checkproj = self.getproject(ids)  # assigns both of the projects to variables

            if (qty < 0):  # no non negative qty's
                return invalidinput
            if hwsetname == "hwset1":
                hardwareSets = checkproj['hardwareSets']
                hwset1 = hardwareSets['hwset1']
                availability = hwset1['availability']  # assign variables to availability and project hw amount
                hw = checkproj["hardware"]
                if qty <= availability:  # check if qty wanted to check out is less total available
                    changevalue = {"$set": {"hardwareSets.hwset1.availability": availability - qty}}  #
                    changevalue2 = {"$set": {"hardware": qty + hw}}

                    self.__db.Projects.update_one({"ids": ids}, changevalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0
                else:  # if not, take everything out and leave 0 left
                    changevalue = {"$set": {"hardwareSets.hwset1.availability": 0}}
                    changevalue2 = {"$set": {"hardware": availability + hw}}

                    self.__db.Projects.update_one({"ids": ids}, changevalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0
            else:
                hardwareSets = checkproj['hardwareSets']
                hwset2 = hardwareSets['hwset2']
                availability = hwset2['availability2']  # assign variables to availability and project hw amount
                hw = checkproj["hardware"]
                if qty <= availability:  # check if qty wanted to check out is less total available
                    changevalue = {"$set": {"hardwareSets.hwset2.availability2": availability - qty}}  #
                    changevalue2 = {"$set": {"hardware": qty + hw}}

                    self.__db.Projects.update_one({"ids": ids}, changevalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0
                else:  # if not, take everything out and leave 0 left
                    changevalue = {"$set": {"hardwareSets.hwset2.availability2": 0}}
                    changevalue2 = {"$set": {"hardware": availability + hw}}

                    self.__db.Projects.update_one({"ids": ids}, changevalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0

    def checkin(self, qty, ids, hwsetname):
        invalidinput = "invalid input"
        if self.getproject(ids) is not None:

            checkproj = self.getproject(ids)
            if (qty < 0):
                return invalidinput
            if hwsetname == "hwset1":
                hardwareSets = checkproj['hardwareSets']
                hwset1 = hardwareSets['hwset1']
                availability = hwset1['availability']  # assign variables to availability and project hw amount
                hw = checkproj["hardware"]
                capacity = hwset1['capacity']

                if (qty <= hw):
                    if qty <= capacity - availability:
                        checkinvalue = {"$set": {"hardwareSets.hwset1.availability": availability + qty}}
                        changevalue2 = {"$set": {"hardware": hw - qty}}
                        self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                        self.__db.Projects.update_one({"ids": ids}, changevalue2)
                        return 0
                    else:
                        checkinvalue = {"$set": {"hardwareSets.hwset1.availability": capacity}}
                        changevalue2 = {"$set": {"hardware": hw - (capacity - availability)}}
                        self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                        self.__db.Projects.update_one({"ids": ids}, changevalue2)
                        return 0
                else:
                    if qty <= capacity - availability:
                        checkinvalue = {"$set": {"hardwareSets.hwset1.availability": availability + hw}}
                        changevalue2 = {"$set": {"hardware": 0}}
                        self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                        self.__db.Projects.update_one({"ids": ids}, changevalue2)
                        return 0
                    else:
                        checkinvalue = {"$set": {"hardwareSets.hwset1.availability": capacity}}
                        changevalue2 = {"$set": {"hardware": hw - (capacity - availability)}}
                        self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                        self.__db.Projects.update_one({"ids": ids}, changevalue2)
                        return 0

            else:
                hardwareSets1 = checkproj['hardwareSets']
                hwset2 = hardwareSets1['hwset2']
                availability = hwset2['availability2']  # assign variables to availability and project hw amount
                hw = checkproj["hardware"]
                capacity = hwset2['capacity2']
                if (qty <= hw):
                    if qty <= capacity - availability:
                        checkinvalue = {"$set": {"hardwareSets.hwset2.availability2": availability + qty}}
                        changevalue2 = {"$set": {"hardware": hw - qty}}
                        self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                        self.__db.Projects.update_one({"ids": ids}, changevalue2)
                        return 0
                    else:
                        checkinvalue = {"$set": {"hardwareSets.hwset2.availability2": capacity}}
                        changevalue2 = {"$set": {"hardware": hw - (capacity - qty)}}
                        self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                        self.__db.Projects.update_one({"ids": ids}, changevalue2)
                        return 0

    # need to add in project resources function, made most of the functions for it
    def mainfunc(self, ids, input, qty, hwsetname, capacity):
        nothing = "nonexistent project or hwset"
        invalid = "invalid"

        proj = self.getproject(ids)
        if (proj == None):
            return nothing
        if (input == "in"):
            self.checkin(qty, ids, hwsetname, capacity)
        else:
            self.checkout(qty, hwsetname, ids)

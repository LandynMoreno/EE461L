from pymongo import MongoClient


class database:

    def __init__(self):
        myClient = MongoClient(
            "mongodb+srv://tester:helloworld@cluster0.wsoqa.mongodb.net/project?retryWrites=true&w=majority")
        self.client = myClient
        self.__db = myClient.project

    def getdata(self, ids, username):
        try:
            checkproj = self.getproject(ids)
            hardwareSets = checkproj['hardwareSets']
            hwset1 = hardwareSets['hwset1']
            availability1 = hwset1['availability']
            capacity1 = hwset1['capacity']
            hwset2 = hardwareSets['hwset2']
            availability2 = hwset2['availability2']
            capacity2 = hwset2['capacity2']
            desc = checkproj['description']
            nam = checkproj['name']
            message = "approved"
        except:
            message = "Some error occured"

        #add user info later, user checked out amt

        return {
            "avail1": availability1,
            "capac1": capacity1,
            "avail2": availability2,
            "capac2": capacity2,
            "name": nam,
            "description": desc,
            "message": message

        }

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
                "users": {
                    username: ({"hwset1": 0, "hwset2": 0})

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
            if (not found):
                userList[username] = ({"hwset1": 0, "hwset2": 0})
                changevalue = {"$set": {"users": userList}}

                self.__db.Projects.update_one({"ids": ids}, changevalue)

            return "approved"
            # insert username into the db here

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

    def gethwnumbers(self, ids, username, hwsetname):
        if self.getproject(ids) is not None:
            if hwsetname == "hwset1":
                project = self.getproject(ids)
                userList = project['users']
                for key in userList:
                    if key == username:
                        usercheckout = userList[username]
                usercheckoutnum = int(usercheckout['hwset1'])
                #print(username + " has " + str(usercheckoutnum) + " in hwset1")
                return(str(usercheckoutnum))

            else:
                project = self.getproject(ids)
                userList = project['users']
                for key in userList:
                    if key == username:
                        usercheckout = userList[username]
                usercheckoutnum = int(usercheckout['hwset2'])
                #print(username + " has " + str(usercheckoutnum) + " in hwset2")
                return(str(usercheckoutnum))


    def checkout(self, qty, ids, hwsetname, username):
        invalidinput = "invalid input"

        if self.getproject(ids) is not None:  # check if the project exists

            checkproj = self.getproject(ids)  # assigns both of the projects to variables

            if (qty < 0):  # no non negative qty's
                return -1
            if hwsetname == "hwset1":
                hardwareSets = checkproj['hardwareSets']
                hwset1 = hardwareSets['hwset1']
                availability = hwset1['availability']  # assign variables to availability and project hw amount
                hw = checkproj["hardware"]
                checkout = checkproj['users']
                project = self.getproject(ids)
                userList = project['users']
                for key in userList:
                    if key == username:
                        usercheckout = userList[username]
                concat = "users." + username + ".hwset1"
                usercheckoutnum = int(usercheckout['hwset1'])
                if qty <= availability:  # check if qty wanted to check out is less total available
                    changevalue = {"$set": {"hardwareSets.hwset1.availability": availability - qty}}  #
                    changevalue2 = {"$set": {"hardware": qty + hw}}

                    changevalue3 = {"$set":{concat: usercheckoutnum + qty}}

                    self.__db.Projects.update_one({"ids": ids}, changevalue3)
                    self.__db.Projects.update_one({"ids": ids}, changevalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0
                else:  # if not, take everything out and leave 0 left
                    changevalue = {"$set": {"hardwareSets.hwset1.availability": 0}}
                    changevalue2 = {"$set": {"hardware": availability + hw}}
                    changevalue3 = {"$set": {concat: availability + usercheckoutnum}}

                    self.__db.Projects.update_one({"ids": ids}, changevalue3)
                    self.__db.Projects.update_one({"ids": ids}, changevalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0
            else:
                hardwareSets = checkproj['hardwareSets']
                hwset2 = hardwareSets['hwset2']
                availability = hwset2['availability2']  # assign variables to availability and project hw amount
                hw = checkproj["hardware"]
                checkout = checkproj['users']
                project = self.getproject(ids)
                userList = project['users']
                for key in userList:
                    if key == username:
                        usercheckout = userList[username]
                concat = "users." + username + ".hwset2"
                usercheckoutnum = int(usercheckout['hwset2'])
                if qty <= availability:  # check if qty wanted to check out is less total available
                    changevalue = {"$set": {"hardwareSets.hwset2.availability2": availability - qty}}  #
                    changevalue2 = {"$set": {"hardware": qty + hw}}
                    changevalue3 = {"$set":{concat: qty + usercheckoutnum}}

                    self.__db.Projects.update_one({"ids": ids}, changevalue3)
                    self.__db.Projects.update_one({"ids": ids}, changevalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0
                else:  # if not, take everything out and leave 0 left
                    changevalue = {"$set": {"hardwareSets.hwset2.availability2": 0}}
                    changevalue2 = {"$set": {"hardware": availability + hw}}
                    changevalue3 = {"$set":{concat: availability + usercheckoutnum}}

                    self.__db.Projects.update_one({"ids": ids}, changevalue3)
                    self.__db.Projects.update_one({"ids": ids}, changevalue)
                    self.__db.Projects.update_one({"ids": ids}, changevalue2)
                    return 0
        else:
            return -1

    def checkin(self, qty, ids, hwsetname, username):
        invalidinput = "invalid input"
        if self.getproject(ids) is not None:

            checkproj = self.getproject(ids)
            if (qty < 0):
                return -1
            if hwsetname == "hwset1":
                hardwareSets = checkproj['hardwareSets']
                hwset1 = hardwareSets['hwset1']
                availability = hwset1['availability']  # assign variables to availability and project hw amount
                hw = checkproj["hardware"]
                capacity = hwset1['capacity']
                project = self.getproject(ids)
                userList = project['users']
                for key in userList:
                    if key == username:
                        usercheckout = userList[username]

                usercheckoutnum = int(usercheckout['hwset1'])
                concat = "users." + username + ".hwset1"
                if(qty<= usercheckoutnum):
                    checkinvalue = {"$set": {"hardwareSets.hwset1.availability": availability + qty}}
                    #changevalue2 = {"$set": {"hardware": hw - qty}}
                    changevalue3 = {"$set":{concat: usercheckoutnum - qty}}
                    self.__db.Projects.update_one({"ids": ids}, changevalue3)
                    self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                    return 0
                else:
                    checkinvalue = {"$set": {"hardwareSets.hwset1.availability": availability + usercheckoutnum}}
                    changevalue3 = {"$set":{concat: 0}}
                    self.__db.Projects.update_one({"ids": ids}, changevalue3)
                    self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                    return 0




                # if (qty <= hw):
                #     if qty <= capacity - availability:
                #         checkinvalue = {"$set": {"hardwareSets.hwset1.availability": availability + qty}}
                #         changevalue2 = {"$set": {"hardware": hw - qty}}
                #         changevalue3 = {"$set":{concat: usercheckoutnum - qty}}

                #         self.__db.Projects.update_one({"ids": ids}, changevalue3)
                #         self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                #         self.__db.Projects.update_one({"ids": ids}, changevalue2)
                #         return 0
                #     else:
                #         checkinvalue = {"$set": {"hardwareSets.hwset1.availability": capacity}}
                #         changevalue2 = {"$set": {"hardware": hw - (capacity - availability)}}
                #         changevalue3 = {"$set":{concat: usercheckoutnum - (capacity - availability)}}

                #         self.__db.Projects.update_one({"ids": ids}, changevalue3)
                #         self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                #         self.__db.Projects.update_one({"ids": ids}, changevalue2)
                #         return 0
                # else:
                #     if qty <= capacity - availability:
                #         checkinvalue = {"$set": {"hardwareSets.hwset1.availability": availability + hw}}
                #         changevalue2 = {"$set": {"hardware": 0}}
                #         changevalue3 = {"$set":{concat: 0}}

                #         self.__db.Projects.update_one({"ids": ids}, changevalue3)
                #         self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                #         self.__db.Projects.update_one({"ids": ids}, changevalue2)
                #         return 0
                #     else:
                #         checkinvalue = {"$set": {"hardwareSets.hwset1.availability": capacity}}
                #         changevalue2 = {"$set": {"hardware": hw - (capacity - availability)}}
                #         changevalue3 = {"$set":{concat: usercheckoutnum - (capacity - availability)}}

                #         self.__db.Projects.update_one({"ids": ids}, changevalue3)
                #         self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                #         self.__db.Projects.update_one({"ids": ids}, changevalue2)
                #         return 0

            else:
                hardwareSets1 = checkproj['hardwareSets']
                hwset2 = hardwareSets1['hwset2']
                availability = hwset2['availability2']  # assign variables to availability and project hw amount
                hw = checkproj["hardware"]
                capacity = hwset2['capacity2']
                project = self.getproject(ids)
                userList = project['users']
                for key in userList:
                    if key == username:
                        usercheckout = userList[username]
                concat = "users." + username + ".hwset2"
                usercheckoutnum = int(usercheckout['hwset2'])
                if(qty<= usercheckoutnum):
                    checkinvalue = {"$set": {"hardwareSets.hwset2.availability2": availability + qty}}
                    changevalue3 = {"$set":{concat: usercheckoutnum - qty}}
                    self.__db.Projects.update_one({"ids": ids}, changevalue3)
                    self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                    return 0
                else:
                    checkinvalue = {"$set": {"hardwareSets.hwset2.availability2": availability + usercheckoutnum}}
                    changevalue3 = {"$set":{concat: 0}}
                    self.__db.Projects.update_one({"ids": ids}, changevalue3)
                    self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                    return 0


                # if (qty <= hw):
                #     if qty <= capacity - availability:
                #         checkinvalue = {"$set": {"hardwareSets.hwset2.availability2": availability + qty}}
                #         changevalue2 = {"$set": {"hardware": hw - qty}}
                #         changevalue3 = {"$set":{concat: usercheckoutnum - qty}}

                #         self.__db.Projects.update_one({"ids": ids}, changevalue3)
                #         self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                #         self.__db.Projects.update_one({"ids": ids}, changevalue2)
                #         return 0
                #     else:
                #         checkinvalue = {"$set": {"hardwareSets.hwset2.availability2": capacity}}
                #         changevalue2 = {"$set": {"hardware": hw - (capacity - qty)}}
                #         changevalue3 = {"$set":{concat: usercheckoutnum - (capacity - availability)}}

                #         self.__db.Projects.update_one({"ids": ids}, changevalue3)

                #         self.__db.Projects.update_one({"ids": ids}, checkinvalue)
                #         self.__db.Projects.update_one({"ids": ids}, changevalue2)
                #         return 0

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
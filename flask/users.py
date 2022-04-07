from pymongo import MongoClient
import ssl
import sys


class Users:
    client = MongoClient("mongodb+srv://tester:helloworld@cluster0.wsoqa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")    
    db = client.project
    collec = db.users 

    def __init__(self):
        self.capc = 200


    def addUser(self, uname, pword):
        self.__username = uname
        self.__password= pword
    




# from pymongo import MongoClient
# import ssl
# import sys


# class Users:

#     def __init__(self):
#         self.capc = 200

#     def addUser(self, uname, pword):
#         client = MongoClient(
#             "mongodb+srv://tester:<password>@cluster0.wsoqa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#         db = client.project
#         collec = db.users

#         newDoc = {
#             "username": uname,
#             "password": pword,
#         }

#         collec.insert_one(newDoc)

#         client.close()

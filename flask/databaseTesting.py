import databaseImplementation


def mainsss():
    db = databaseImplementation.database()

    # Creating and testing project functions

    # checkout
    # checkin

    projectID = "plp635"

    print("Creating a new project with ID: " + projectID)
    print(db.createdocuments("phil", "project for 461 testing", projectID, 250) + "\n")

    print("Trying to create another Project with the same ID, (ID = " + projectID + ")")
    print(db.createdocuments("phil", "project for 461 testing", projectID, 250) + "\n")

    print("Checking if project " + projectID + " exists")
    print(db.getproject(projectID))
    print()

    print("Listing all Projects that exist: ")
    db.list()
    print()

    print("Deleting Project with ID: " + projectID)
    print(db.deleteProject(projectID) + "\n")

    print("Trying to get the project that just got deleted, (ID = " + projectID + ")")
    print(db.getproject(projectID) + "\n")

    print("Trying to delete the project that just got deleted, (ID = " + projectID + ")")
    print(db.deleteProject(projectID) + "\n")

    # checkin and checkout testing here

    projectID = "KING123"

    print("Creating a new project with ID: " + projectID)
    print(db.createdocuments("phil", "project for 461 testing", projectID, 250) + "\n")

    print("Checking if project " + projectID + " exists")
    print(db.getproject(projectID))
    print()

    print("Checking out 50 units from hardwareset1")
    db.checkout(50, projectID, "hwset1")
    print(db.getproject(projectID))
    print()

    print("Checking out 150 units from hardwareset2")
    db.checkout(150, projectID, "hwset2")
    print(db.getproject(projectID))
    print()

    print("Checking in 30 units to hardwareset1")
    db.checkin(30, projectID, "hwset1")
    print(db.getproject(projectID))
    print()

    print("Checking in 150 units to hardwareset2")
    db.checkin(150, projectID, "hwset2")
    print(db.getproject(projectID))
    print()

    print("Checking in 30 units to hardwareset1")
    db.checkin(30, projectID, "hwset1")
    print(db.getproject(projectID))
    print()

    print("Checking in 0 units to hardwareset2")
    db.checkin(0, projectID, "hwset2")
    print(db.getproject(projectID))
    print()

    print("Checking out 0 units to hardwareset2")
    db.checkout(0, projectID, "hwset2")
    print(db.getproject(projectID))
    print()

    print("Checking in -1 units to hardwareset2")
    db.checkin(-1, projectID, "hwset2")
    print(db.getproject(projectID))
    print()

    print("Checking out -1 units to hardwareset2")
    db.checkout(-1, projectID, "hwset2")
    print(db.getproject(projectID))
    print()

    print("Checking out 300 units from hardwareset1")
    db.checkout(300, projectID, "hwset1")
    print(db.getproject(projectID))
    print()

    print("Checking out 250 units from hardwareset2")
    db.checkout(250, projectID, "hwset2")
    print(db.getproject(projectID))
    print()


mainsss()

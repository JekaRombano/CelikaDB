import json
import os
import random
from .celikaFileManagement import celikaFileManagementSystem
import sys
from datetime import datetime

# INFORMATION OF THE CODEBASE
"""
--------------------------------
 INFORMATION CODEBASE REFERENCE 
--------------------------------
Version : 1.00
Date Started : September 29 2026
Time Started : 8:34 PM
Last Updated : September 29 2026
"""
# PURPOSE OF THE CODE
"""
Celika DB 

Celika DB will serve as the foundation of the planned Celika DB Web Database. 
It will function as the core database library used by the web-based system, 
providing the necessary functionality for storing, managing, and accessing data.

Celika DB is designed to support both local and cloud-based operations. 
It can run locally on a user's computer, allowing the database to operate without relying entirely on external cloud services. 
At the same time, it can be integrated with the Celika DB Web Database to provide web-based access and functionality.
The main goal of Celika DB is to provide a flexible database system that can operate locally while also supporting cloud-based and web applications.
"""
groupIdentity = 0
fs = celikaFileManagementSystem()

class celikaDB:
    def __init__(self):
        # Temporary Database will be respobsible for storing the 
        # data for the mean time. Think of it as the RAM of the DATABASE
        self.temporaryDatabase = []
        # groupIdentity is for indexing purposes which can serve as the adresss
        self.groupIdentity = 0
        # start at 0 and increment for every function called.
        # this will store the title and index, so that we need to call a group we only use a reference : title
        self.titleIdentityMemory = {}
        # the state will dictate wether to print or raise the problem.
        self.state = True



   
    fs.initiallize()




    # create family is a function that will input a dictionary in the temporary database.
    # think of it as a group where the data can be stored
    def createGroup(self, **kwargs):

        title = kwargs.get("title")

        """
            NOTE : THIS PART WAS FIXED BY AI caused im getting brain fucked already.
            So essentially, this part of code will check if the title is already there to avoid
            duplication in the input out system. 

            The createGroup function creates a new group in the database
            It first gets the title and checks if the title already exists in the database
            If the title already exists the function will not create another group
            If the title is new the function gives the group a new identity and creates the group
            It then saves the title and identity in titleIdentityMemory and adds the new group to the temporary database
            When CelikaDB starts again it loads the saved data and rebuilds titleIdentityMemory so the program knows which groups already exist
            This prevents duplicate groups and allows CelikaDB to continue using the existing data

        """


        if not title:
            return False

        # Check if the group already exists
        for group in self.temporaryDatabase:
            if group.get("groupTitle") == title:
                return False

        # Create a new identity
        self.groupIdentity += 1

        # Create the group
        templateGroup = {
            "groupTitle": title,
            "identity": self.groupIdentity
        }

        # Register title and identity
        self.titleIdentityMemory[title] = self.groupIdentity

        # Add group to temporary database
        self.temporaryDatabase.append(templateGroup)

        return True

    # this allows you to add data inside a group allowing the user
    # customize the group depending on their indetity.
    def insertChildren(self, **kwargs):
        # in initalization of the function, first try the intialization of variable identity
        try:
            """
            The idea of identity using the group title makes the searching easier.
            the identity is stored in the titleIdentityMemory storage with key : title and value : index.
            thus when the title is called in the titleIdentityMemory it will display the index of that group.
            """
            identity = self.titleIdentityMemory[kwargs.get("call")] - 1

        # if KeyError arise print/raise this error.
        except KeyError:
            # changing the state allows the system not to drop the database
            # thus, allowing the error to takeover
            self.state = False
            print(f"UnknownTitle: The title '{kwargs.get('call')}' does not exist.")
            return
        
        # check if it's template and dictionary as type
        if kwargs.get("template") and type(kwargs.get("template")) == dict and kwargs["call"] != "":
            for item in kwargs.get("template"):
                """
                This code just get the key from the template and keys to 
                make it very organize. 
                """
                self.temporaryDatabase[identity][item] = kwargs.get("template")[item] 

    def removeChildren(self, **kwargs):
        """
            FLOW OF THE REMOVE DATA : 
        
            Remove chilcdren will remove a group from the temporary database.
            The code works by first using the title for getting the index the index of each chidlren
            is stored in the titleIndentityMemory.      
        
            The flow is we first remove the group from the temporaryDatabase
            strictly also remove the key and value from the titleIdentity.
        
            After successfully removing it
        
            we would update specifically identity by first attaining the length of the 
            temporaryDatabase which is starting from 0 to the last. Why 0? In my identity
            I incremented 1 so that the data will be in user friendly. then for example 
            there are 3 group, I removed 1 , the length will be 0 to 1. After that we are gonna
        
            use that to call each group so group[0] and group[1] this is already the update list
            from each group get the identity variable use the index 0 and 1 and just add 1 to it so
            the new identiy will be 1, 2
        
            if I removed 2 groups from a 4 group, position 2, 3 the flow will be 
            original = 0 to 3
            orginal_position_identiy = 1, 2, 3, 4
            updated = 0, 1
            postion_updated_identity , 1, 4
            get all the updated group
            group 1, group 4
            group_identity = 1, 4
            get the index of the total total database : 0 to 1 because the updated list has two groups only.
            identity 0 : group 1 , indetity 1 :  group 4 update it 
            identity += 1
            group 1 : will have the identity of 1
            group4 : will have the identity of 2
                    
        """

        def removeFunctionSystem():
            if kwargs.get("title"):
                title = kwargs.get("title")
                index = self.titleIdentityMemory[title] - 1


                del self.temporaryDatabase[index]
                del self.titleIdentityMemory[title]

                for i in range(len(self.temporaryDatabase)):
                    self.titleIdentityMemory[self.temporaryDatabase[i]["groupTitle"]] = i + 1
                    self.temporaryDatabase[i]["identity"] = i + 1


        if type(kwargs["verify"]) == bool:
                """
                    This system uses a boolean value to determine whether verification is required
                    before removing a group from the temporary database.
                
                    If the boolean value is set to True, the system will generate and display a
                    one-time verification code. The user must enter the correct verification code
                    before the removal process is allowed to continue. If the entered code does
                    not match the generated verification code, the removal process will be
                    cancelled and the group will remain unchanged.
                
                    If the boolean value is set to False, the system will proceed directly with
                    the removal process without requesting a verification code or displaying a
                    warning.
                
                    This allows the caller to choose between a protected removal process and an
                    immediate removal process depending on the value provided.
                """

                if kwargs["verify"] == True:

                    verificationCode = random.randint(1000, 9000)

                    print(
                        f"This group will be removed: "
                        f"{self.temporaryDatabase[self.titleIdentityMemory[kwargs.get('title')] - 1]}"
                    )

                    print(f"This is a one-time verification code: {verificationCode}")

                    verificationInput = input("VerifyCode: ")

                    if verificationInput == str(verificationCode):
                        removeFunctionSystem()

                else:
                    removeFunctionSystem()

    def updateChildren(self, **kwargs):
        """
        .updateChildren allows the database to update the value of an already existing
        key. This allows users to modify the stored value as many times as needed
        without creating a new key or affecting other existing data.
        """

        title = kwargs.get("title")
        key = kwargs.get("key")
        value = kwargs.get("value")

        index = self.titleIdentityMemory[title] - 1
        self.temporaryDatabase[index][key] = value

    def search(self, **kwargs):
        """
            very self explnatory. 

            This code allows the user to search the temporary database using a **title, identity, or key-value pair**.
            If a title is provided, the system uses `titleIdentityMemory` to find the corresponding group and return it from `temporaryDatabase`.
            If an identity is provided, the system converts it to an integer, subtracts `1` for zero-based indexing, and returns the corresponding group.
            If both a key and value are provided, the system loops through the database and searches for a group where the specified key contains the given value.
            Once a matching group is found, the system immediately returns that group.

        """
        # this allow the user to search via title
        if kwargs.get("title"):
            return self.temporaryDatabase[self.titleIdentityMemory[kwargs.get("title")] - 1]
        # this allow the user to search via identity
        if kwargs.get("identity"):
            return self.temporaryDatabase[int(kwargs.get("identity")) -1]
        # this allow the user to search via key and value
        if kwargs.get("key") and kwargs.get("value"):
            for _ in range(0, len(self.temporaryDatabase)):
                if self.temporaryDatabase[_][kwargs.get("key")] == kwargs.get("value"):
                    return self.temporaryDatabase[_]

    def getChildren(self, **kwargs):
        """
            get function
            Essentially you provide the title for index management
            and then you also provide the data you need by key and the system 
            is gonna output the data.
        
        """
        if kwargs.get("key") and kwargs.get("title"):
            identity = self.temporaryDatabase[self.titleIdentityMemory[kwargs.get("title")] - 1][kwargs.get("key")]
            return identity

                
    # THIS ALLOW THE DATABASE TO SEARCH ALL THE KEYS PER GROUP
    def showAllKeys(self):
        array_keys = []
        for _ in range(0, len(self.temporaryDatabase)):
            # put it in a array so that one ouput may be attain
            array_keys.append(list(self.temporaryDatabase[_].keys()))

        return array_keys
    # THIS ALLOW THE DATABASE TO SEARCH ALL THE VALUES PER GROUP
    def showAllValue(self):
            array_keys = []
            for _ in range(0, len(self.temporaryDatabase)):
                # put it in a array so that one ouput may be attain
                array_keys.append(list(self.temporaryDatabase[_].values()))
    
            return array_keys

    def database(self):
        return self.temporaryDatabase

    def connect(self):
        self.temporaryDatabase = json.loads(fs.readData())

        self.titleIdentityMemory = {}

        for group in self.temporaryDatabase:
            title = group.get("groupTitle")
            identity = group.get("identity")

            self.titleIdentityMemory[title] = identity

        if self.temporaryDatabase:
            self.groupIdentity = max(
                group["identity"]
                for group in self.temporaryDatabase
            )
        else:
            self.groupIdentity = 0
        
    # This will only show the temporary Database if it is true else false
    def showDatabase(self, state=bool):
        # show the state when it's true else let the errors take in.
        if self.state == True:
            print(json.dumps(json.loads(fs.readData()), indent=2))
        else : 
            return 0


    def listen(self):
        fs.writeData(content=self.temporaryDatabase)
        fs.writeIndex(content=self.titleIdentityMemory)
        fs.writeLOG()

    def drop(self):
        fs.clear()
        
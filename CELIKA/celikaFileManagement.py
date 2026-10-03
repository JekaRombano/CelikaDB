import os
import sys
import json
from datetime import datetime

"""
--------------------------------------------
INFORMATION
--------------------------------------------
DATE CODED : 10/03/26
VERSION : 1.2
DATE LAST UPDATED : 10/03/26
"""

"""

// PROJECT MANAGEMENT SYSTEM
ALGORTIHM DEISGN : INITIALIZATION FUNCTION

PROJECT_DIRECTORY/
├── DATA/
│   └── filename.json
├── INDEX/
│   └── index.json
└── LOG/
    └── LOG.json
"""

# FILE MANIPULATION FUNCTIONS
"""
    This is a linux implementation function so that the developer can easily manage the file system with ease.
    The problem that I encounter last time is bad code management and review. Using this functions will make it more 
    easier for the developer and the next developer to read it.
"""
# print working directory
def pwd():
    print(os.getcwd())

# change directory
def cd(dir):
    os.chdir(dir)

# list directory
def ls(dir):
    os.listdir(dir)


class celikaFileManagementSystem():
    def __init__(self):
        self.currentDirectory = os.getcwd()
        self.currentWorkingFile = sys.argv[0]
        # from .py split the two words in to a list and get the base filename by calling 0
        self.systemDefaultProjectDirectory = str(self.currentWorkingFile).split(".")[0]
        self.systemDefaultFileName = str(self.currentWorkingFile).split(".")[0] + ".json"
        self.systemDefaultINDEXName = str(self.currentWorkingFile).split(".")[0] + "INDEX.json"
        self.systemDefaultLOGName = str(self.currentWorkingFile).split(".")[0] + "LOG.json"


    def initiallize(self):
        """
            1.) CHECK IF FOLDER EXIST
            2.) IF NOT : GO TO PROJECT CREATION
            3.) ELSE : CHECK IF FILES AND DIRECTORY ARE CORRUPTED
        """
        template_DATA = []
        template_INDEX = [{
                            "database" : "celika",
                            "version" : 1.2,
                            "type" : "INDEX"
                        }]
        template_LOG = [{
                        }]
        """
            FILE CHECKING

            The system will always go to each directory and check wheter the files needed for each directory will be there.
            If the system detects that there is no or missing files it will auto create it. The only problem is that all of
            the data will be erase but the file will be there.
        
        """


        project_directory_name = f"[{self.systemDefaultProjectDirectory.upper()}]_PROJECT_DIRECTORY"
        location_of_project_directory = f"{self.currentDirectory}/{project_directory_name}"
        FOLDERS = ["DATA", "INDEX", "LOG"]

        """
            CHECK IF THE FILE OF DATA.json IS THERE. If not it will automatically create the file.
        """
        if os.path.isdir(project_directory_name):
            
            cd(f"{location_of_project_directory}/{FOLDERS[0]}")
            if not os.path.isfile(self.systemDefaultFileName):
                print(f"FILE MISSING : {self.systemDefaultFileName}. CELIKA DB will auto create a file to supply the missing file. ")
                with open(self.systemDefaultFileName, "w") as Datafilename:
                    Datafilename.write(json.dumps(template_DATA, indent=2))
                    #Datafilename.close()

            
            cd(location_of_project_directory)

            """
                CHECK IF THE FILE OF INDEX.json IS THERE. If not it will automatically create the file.
            """

            cd(f"{location_of_project_directory}/{FOLDERS[1]}")
            if not os.path.isfile(self.systemDefaultINDEXName):
                print(f"FILE MISSING : {self.systemDefaultINDEXName}. CELIKA DB will auto create a file to supply the missing file. ")
                with open(self.systemDefaultFileName, "w") as DataINDEXname:
                        DataINDEXname.write(json.dumps(template_INDEX, indent=2))
                        #DataINDEXname.close()

            cd(location_of_project_directory)

            """
                CHECK IF THE FILE OF LOG.json IS THERE. If not it will automatically create the file.
            """

            cd(f"{location_of_project_directory}/{FOLDERS[2]}")
            if not os.path.isfile(self.systemDefaultLOGName):
                    print(f"FILE MISSING : {self.systemDefaultLOGName}. CELIKA DB will auto create a file to supply the missing file. ")
                    with open(self.systemDefaultLOGName, "w") as DataLOGname:
                        DataLOGname.write(json.dumps(template_INDEX, indent=2))
                        #DataLOGname.close()
                
        else : 
              #STEP 1 to 3
                     # THIS WILL CREATE THE PROJECT_DIRECTORY
                     os.mkdir(project_directory_name)
             
                     # STEP 4
                     # GO TO THE PROJECT DIRECTORY
                     
                     cd(location_of_project_directory)
             
                     # STEP 5
                     FOLDERS = ["DATA", "INDEX", "LOG"]
                     """
                         Essentially the name of the inside the array called FOLDERS will be created
                         inside the project_directory. Thus it will just get all the items of the FOLDERS
                         create them and will let it be.
                     """
                     for items in FOLDERS:
                         os.mkdir(items)
                         
                     #STEP 6
                     """
                         Write this templates on each file depending on the folders in their respective group.
                     """
                     """
                         HOW THIS WORKS : 
                         
                         OPEN THE LOCATION
                         CREATE THE FILE
                         WRITE THE TEMPLATES
                         CLOSE THE FILE
                         GO BACK TO BEFORE-LOCATION
                         REPEAT
                     
                     """
                     # FOR DATA DIRECTORY
                     cd(f"{location_of_project_directory}/{FOLDERS[0]}")
                     with open(self.systemDefaultFileName, "w") as Datafilename:
                         Datafilename.write(json.dumps(template_DATA, indent=2))
                         Datafilename.close()
             
                     cd(location_of_project_directory)
             
                     # FOR INDEX DIRECTORY
                     cd(f"{location_of_project_directory}/{FOLDERS[1]}")
                     with open(self.systemDefaultINDEXName, "w") as INDEXfilename:
                             INDEXfilename.write(json.dumps(template_INDEX, indent=2))
                             INDEXfilename.close()
             
                     cd(location_of_project_directory)
             
                     # FOR LOG DIRECTORY
                     cd(f"{location_of_project_directory}/{FOLDERS[2]}")
                     with open(self.systemDefaultLOGName, "w") as LOGfilename:
                             LOGfilename.write(json.dumps(template_LOG, indent=2))
                             LOGfilename.close()

                    
             
        """
        PROJECT CREATION
            1.) FROM THE CURRENT DIRECTORY 
            2.) CREATE A FOLDER NAME USING THIS FORMAT. 
            3.) FORMAT : [systemDefaultProjectDirectory]_PROJECT_DIRECTORY
            4.) GO TO LOCATION : [systemDefaultProjectDirectory]_PROJECT_DIRECTORY
            5.) CREATE THESE FOLDERS DATA, INDEX, LOG inside
            6.) GO TO DATA : create the file named filename.json
        """

       

    def writeData(self, **kwargs):
        """
            This function is responsible for storing CelikaDBs database content into its designated local storage file
            It determines the name and location of the project directory based on the systems default project directory
            The function then checks whether content has been provided through the content keyword argument
            If content is available it navigates to the projects DATA directory opens the systems default storage file in write mode converts the provided data into JSON format and writes the formatted data into the file
            This allows CelikaDB to permanently save its current database content to the local filesystem allowing the stored information to be accessed again when needed
                    
        """
        project_directory_name = f"[{self.systemDefaultProjectDirectory.upper()}]_PROJECT_DIRECTORY"
        location_of_project_directory = f"{self.currentDirectory}/{project_directory_name}"

        if kwargs.get("content"):
            cd(f"{location_of_project_directory}/DATA")
            with open(self.systemDefaultFileName, "w") as Datafilename:
                    Datafilename.write(json.dumps(kwargs.get("content"), indent=2))
                    #Datafilename.close()    

    def writeIndex(self, **kwargs):
        project_directory_name = f"[{self.systemDefaultProjectDirectory.upper()}]_PROJECT_DIRECTORY"
        location_of_project_directory = f"{self.currentDirectory}/{project_directory_name}"
         
        if kwargs.get("content"):
            cd(f"{location_of_project_directory}/INDEX")
            with open(self.systemDefaultINDEXName, "w") as Datafilename:
                             Datafilename.write(json.dumps(kwargs.get("content"), indent=2))
                             #Datafilename.close()    

    def writeLOG(self):
        project_directory_name = f"[{self.systemDefaultProjectDirectory.upper()}]_PROJECT_DIRECTORY"
        location_of_project_directory = f"{self.currentDirectory}/{project_directory_name}"
        log_path = os.path.join(location_of_project_directory, "LOG", self.systemDefaultLOGName)

        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        now = datetime.now()

        # your log template
        templateLog = [{
            "Database": "CELIKA DB",
            "VERSION CONTROL": 1.1,
            "FileName": self.systemDefaultLOGName,
            "DateCreated": now.strftime("%Y-%m-%d"),
            "TimeCreated": now.strftime("%H:%M:%S"),
            "Last Updated": now.strftime("%Y-%m-%d %H:%M:%S")
        }]

        # read the existing log (if it is valid, keep it so DateCreated/TimeCreated are preserved)
        try:
            with open(log_path, "r") as file:
                existingLog = json.load(file)

            if (
                isinstance(existingLog, list)
                and existingLog
                and isinstance(existingLog[0], dict)
                and "FileName" in existingLog[0]
                and "DateCreated" in existingLog[0]
            ):
                templateLog = existingLog
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # missing or corrupted: use the fresh template

        # update only the last updated timestamp
        templateLog[0]["Last Updated"] = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(log_path, "w") as file:
            json.dump(templateLog, file, indent=2)

    def readData(self):
        """
            This function is responsible for reading the stored database content from CelikaDBs local storage file
            It determines the name and location of the project directory using the systems default project directory
            The function then navigates to the projects DATA directory where the database storage file is located
            It opens the default storage file in read mode and reads its entire contents
            The stored content is then returned to the program so it can be accessed and processed by CelikaDB
        
        """
        project_directory_name = f"[{self.systemDefaultProjectDirectory.upper()}]_PROJECT_DIRECTORY"
        location_of_project_directory = f"{self.currentDirectory}/{project_directory_name}"

        cd(f"{location_of_project_directory}/DATA")
        with open(self.systemDefaultFileName, "r") as DataReadfilename:
            content = DataReadfilename.read()    
            return content
        
    def clear(self):
        import random

        verification_code = random.randint(1000, 9000)

        print(f"This is a verification code for clearing all the data: {verification_code}")

        verify = input("Verify: ")

        project_directory_name = f"[{self.systemDefaultProjectDirectory.upper()}]_PROJECT_DIRECTORY"
        location_of_project_directory = f"{self.currentDirectory}/{project_directory_name}"

        FOLDERS = ["DATA", "INDEX", "LOG"]

        try:

            if int(verify) == verification_code:

                # CLEAR DATA
                cd(f"{location_of_project_directory}/{FOLDERS[0]}")

                with open(self.systemDefaultFileName, "w") as Datafilename:
                    json.dump([], Datafilename, indent=2)

                # CLEAR INDEX
                cd(f"{location_of_project_directory}/{FOLDERS[1]}")

                with open(self.systemDefaultINDEXName, "w") as INDEXfilename:
                    json.dump([], INDEXfilename, indent=2)

                print("ALL DATA CLEARED")

            else:
                print("ABORT")

        except ValueError:
            print("ABORT")

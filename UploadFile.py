"""
UPLOAD FILE

ARGS: DB, the connection to the database is received 
RTRNS: NONE 

"""

class UploadFile: 
    def __init__(self, db) -> None:
        self.db = db
        self.file_name = None
    
    def set_filename(self) -> str:
        valid_filename = False
        while valid_filename == False:
            self.file_name = str(input("What is the name of the file you're trying to upload?"))
            if "." not in self.file_name :
                print("ERROR: Please specify the filetype")
            
            else :
                valid_filename == True
    
    def get_filename(self):
        return self.file_name
    
    
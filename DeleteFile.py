"""
DELETE FILE

ARGS: STORAGE CLIENT
RTRNS: ONLY A TRUE

DESC: Deletes a file from the bucket and returns a bool to help log it

"""

class DeleteFile: 
    def __init__(self, storage_client) -> None:
        self.storage = storage_client
        self.delete_filename = None

    def get_delete_filename(self): 
        self.delete_filename = str(input("What is the name of the file you would like to delete? "))
    
    
    def delete_file(self):
        self.storage.child(self.delete_filename).delete()
        return True
    
    def return_filename(self):
        return self.delete_filename

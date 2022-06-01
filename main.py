"""
MAIN:

ARGS: NONE
RTRNS: NONE

"""


from CreateUploadFolder import CreateUploadFolder


def main(): 
    create_folder = CreateUploadFolder()
    create_folder.get_desktop_filepath() 

if __name__ == "__main__":
    main()
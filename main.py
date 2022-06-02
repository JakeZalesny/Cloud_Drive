"""
MAIN:

ARGS: NONE
RTRNS: NONE

"""


from CreateDirectories import CreateDirectories
from Director import Director


def main(): 
    director = Director()
    director.direct()

if __name__ == "__main__":
    main()
import math
import copy

ForwardSelection():
    print("")

BackwardElim():

Angela():


def main():
    print ("Welcome to Angela Su\'s Feature Selection Algorithm.")
    # inputFile = input('What is file you want to use?') # read in data

    #OKAY ANGELA YOU JUST NEED TO USE YOUR BRAIN!!!
    #print ("Please enter total number of features:")
    numFeatures = int(input("Please enter total number of features:"))

    #change it so that get user input while asking for what algorithm to run
    #print ("Type the number of the algorthim you want to run.")
    #print ("1) Forward Selection")
    #print ("2) Backward Elimination")
    #print ("3) Angela Special Algorithm.")

    userAlg = "" #save inputs choices as strings? might be easier?
    #make sure an algorithm is selected, loop if not
    while (userAlg != "1" and userAlg != "2" and userAlg != "3"):
        userAlg = input("""Type the number of the algorthim you want to run.
                        1) Forward Selection
                        2) Backward Elimination
                        3) Angela Special Algorithm. \n""")
    
    print("Beginning search.")

    if(userAlg == "1"):
        ForwardSelection()
    elif(userAlg == "2"):
        BackwardElim()
    else:
        Angela()

if __name__ == '__main__':
    main()

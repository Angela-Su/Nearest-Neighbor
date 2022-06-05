import math
import copy

def normalize(instances, numInstances, numFeatures): #instances is the main data
    #x = (x-ave(x))/std(x)
    #normalized[i][j]

    #find the average, store in array
    ave = []
    for i in range(1, numFeatures + 1):
        ave.append((sum(row[i] for row in instances)) / numInstances)

    #find std, store in array
    std = []
    for i in range(1, numFeatures + 1):
        x = ((row[i] - ave[i-1]) for row in instances) #might have problem here
        difference = sum(x * x) / numInstances
        std.append(math.sqrt(difference))

    #return modified data
    for i in range(0, numInstances):
        for j in range(1, numFeatures + 1):
            instances[i][j] = (instances[i][j] - ave[j-1]) / std[j-1]
    
    return instances

def ForwardSelection(data, numInstances, numFeatures):
    print("forward select")

def BackwardElim(data, numInstances, numFeatures):
    print("back elim")

def Angela():
    print("special")

def main():
    print ("Welcome to Angela Su\'s Feature Selection Algorithm.")
    inputFile = input("Type in the name of the file to test : ") # read in data

    #open the file and read from it
    #https://www.w3schools.com/python/python_file_open.asp
    f = open(inputFile, "r")
    data = f.readline()
    numFeatures = len(data.split()) - 1

    #need to read all lines starting at the beginning of file
    f.seek(0)
    numInstances = sum(1 for line in f)
    f.seek(0)
    instances = [[] for i in range(numInstances)]
    for i in range(numInstances): #might have problems with the iterator
        instances[i] = [float(j) for j in f.readline().split()]
    
    #OKAY ANGELA YOU JUST NEED TO USE YOUR BRAIN!!!

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
    
    #print("Beginning search.")
    print("This dataset has %d features with %d instances." %(numFeatures, numInstances))
    print("Please wait while I normalize the data... DONE!\n") #normalize the data!!!

    normal = normalize(instances, numInstances, numFeatures)

    if(userAlg == "1"):
        ForwardSelection(data, numInstances, numFeatures)
    elif(userAlg == "2"):
        BackwardElim(data, numInstances, numFeatures)
    else:
        Angela()

if __name__ == '__main__':
    main()

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

def NearestNeighbor(instances, numInstances, outOne, feats):
    NN = 0
    NNdist = float('inf') #set to infinity
    numFeatures = len(feats)
    for i in range(0, numInstances):
        if(i == outOne):
            pass
        else:
            dist = 0
            for j in range(0, numFeatures):
                x = instances[i][feats[j]] - instances[outOne][feats[j]]
                xSquare = x * x
                dist = dist + xSquare
            dist = math.sqrt(dist)
            if(dist < NNdist):
                NNdist = dist
                NN = i

    return NN

def leaveOne(data, totalFeats, numInstances): #normal, totalFeats, numInstances
    #returns accuracy 
    tempAcc = 0.0
    for i in range(numInstances):
        outOne = i
        NN = NearestNeighbor(data, numInstances, outOne, totalFeats)
        if (data[NN][0] == data[outOne][0]) :
            tempAcc = tempAcc + 1
    
    return ((tempAcc / numInstances) * 100)

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
    totalFeats = []
    for i in range(1, numFeatures + 1):
        totalFeats.append(i)

    print("Running nearest neighbor with ", numFeatures, " features, using \'leaving-one-out\' evaluation, ")
    accuracy = leaveOne(normal, totalFeats, numInstances)
    print("I get an accuracy of ", accuracy, "%.")

    print("Beginning search. \n")
    if(userAlg == "1"):
        ForwardSelection(data, numInstances, numFeatures)
    elif(userAlg == "2"):
        BackwardElim(data, numInstances, numFeatures)
    else:
        Angela()

if __name__ == '__main__':
    main()

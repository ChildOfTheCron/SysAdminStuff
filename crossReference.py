#!/usr/local/bin/python

#TODO: Make new elements in B update into A. I'm so gosh darn tired.
# Why am I such a sleepy person?
def goCompare():
    print("Hello wordl")
    bucketA = { "pam":[60,"date1"],
            "john":[50,"date1"],
            "marge":[22,"date4"]
    }
    
    bucketB = { "pam":[65,"date1"],
            "steve":[55, "date3"],
            "marge":[22,"date4"]
    }
    
    names = []

    for x, val in bucketA.items():
        if x in bucketB.keys():
            #print("Found:", x)
            names.append(x)

        else:
            #print("Not Found", x)

    for name in names:
        #print(name)
        if bucketA.get(name) == bucketB.get(name): #Compare sublists
            print("Items are the same don't update")
        else:
            print("Items are not the same, update for: ", name)

    return "Done"

if __name__ == "__main__":
    print(goCompare())

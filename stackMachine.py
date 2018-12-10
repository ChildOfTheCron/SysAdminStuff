#!/usr/bin/python

class stackMachine ():

    # Pass in the initial string to parse
    def __init__(self, val):
        self.data = val

    # Declare some helper functions
    def sums(self, val1, val2):
        return int(val1) + int(val2)
    def subs(self, val1, val2):
        return int(val1) - int(val2)
    def multi(self, val1, val2):
        return int(val1) * int(val2)
    def div(self, val1, val2):
        return int(val1) / int(val2)

    # Parse and manipulate my StackMachine
    def parse(self):
        #print(self.data)
        
        myTmpList = list(self.data)
        
        myStack = []

        try:
            for x in myTmpList:
                if x.isdigit():
                    myStack.append(x)
                else:
                    tmpInt2 = myStack.pop(-1)
                    tmpInt1 = myStack.pop(-1)
                    if len(myStack) > 0: # Make sure the list is empty, if not we have passed in ints without using them.
                        raise Exception
                    else:
                        if x == "+":
                            tmpRes = self.sums(tmpInt2, tmpInt1)
                        if x == "-":
                            tmpRes = self.subs(tmpInt1, tmpInt2)
                        if x == "*":
                            tmpRes = self.multi(tmpInt1, tmpInt2)
                        if x == "/":
                            tmpRes = self.div(tmpInt1, tmpInt2)

                        myStack.append(str(tmpRes))
                        self.data = ''.join(myStack)
        except:
            self.data = "Error parsing command list to stack, please check input"

    def printParse(self):
        print(self.data)

if __name__ == '__main__':
    machine = stackMachine("52+2-5+2*5+2*2/3+")
    #machine2 = stackMachine("343+") # Broken string used to testing
    machine.parse()
    machine.printParse()

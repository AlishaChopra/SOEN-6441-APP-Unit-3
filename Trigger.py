'''
TITLE:MAIN CLASS TO CALL ALPHA AND LENGTH CALCULATION METHOD
CREATED:19-JUL-2017
'''
from calculation import *
from builtins import *

class Trigger:
    def ConfirmContinue(self):
        try:
            isContinue = int(input("Do you want to continue (1/0)?"))
            if (isContinue == 0 or isContinue==1):
                return isContinue
            else:
                raise ValueError
        except ValueError:
            print("incorrect value")
            return self.ConfirmContinue()

    def GetRadius(self):
        try:
            r = float(input("Enter Radius Of the Circle?"))
            if (r <= 0):
                raise ValueError
            return r
        except ValueError:
            print("Radius should be numeric and greater than 0")
            return self.GetRadius()

    def trigger_event(self):
        alpha_val = calculationFunc().cal_alpha()
        print("the value of alpha in radians is", alpha_val)
        while True:
            try:
                r = self.GetRadius()
                length = calculationFunc().cal_length(alpha_val, r)
                print("the length of the two segments X1X2 is", length)
                file_open = open("output.txt", "a")
                alpha_value = "the value of alpha is:" + str(alpha_val) + " Radians"
                file_open.write(alpha_value)
                file_open.write("\n")
                radius_val = "the value of radius entered is:" + str(r)
                file_open.write(radius_val)
                file_open.write("\n")
                length_value = "the value of length is:" + str(length)
                file_open.write(length_value)
                file_open.write("\n")
            except ValueError:
                print("Value error occurred. Please try again")

            isContinue = self.ConfirmContinue()
            if isContinue == 0:
                file_open.close()
                break

obj1=Trigger()
obj1.trigger_event()


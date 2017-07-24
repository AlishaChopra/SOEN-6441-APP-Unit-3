from calculation import calculationFunc
from Math_Cal import MathCalculations
class Trigger:

    def trigger_event(self):

        while True:
            alpha_val = calculationFunc().cal_alpha()
            print("the value of alpha in radians is", alpha_val)

            try:
                r = float(input("Enter the radius of the circle:"))
                if r<0:
                    raise Exception
                else:
                    length = calculationFunc().cal_length(alpha_val, r)
                    print("the length of the two segments X1X2 is", length)
            except Exception as e:
                print("The value entered for the radius should be greater than 0",e)
                isContinue = int(input("Do you want to continue (1/0)?"))
                if isContinue == 0:
                    break








obj1=Trigger()
obj1.trigger_event()


from mymath import *


class calculations:

    def cal_alpha(self):
        pi_cal=mymath.cal_pi(self)
        print(pi_cal)
        first=round((pi_cal/2),4)
        last=pi_cal
        mid=round((first+last)/2,4)
        while(first<=last):
            y1=round(mid-(pi_cal/2),4)
            y2=mymath.sin_cal(self,mid)
            if y1==y2:
                return round(mid,4)
                break
            elif y1<y2:
                first=mid+0.0001
            else:
                last=mid-0.0001
            mid=round((first+last)/2,4)

    def cal_length(self,alpha_val):
        radius=int(input("Enter the radius of the circle:"))
        cos_x=alpha_val/2;
        z=mymath.cos_cal(cos_x);
        length=2*radius*(1-z)
        return round(length,4)


obj2=calculations()
alpha_val=obj2.cal_alpha()
print("the value of alpha in radians is",alpha_val)
length=obj2.cal_length(alpha_val)
print("the length of the two segments X1X2 is",length)
from Math_Cal import MathCalculations

class calculationFunc():


 # Calculation for alpha

 def cal_alpha(self):
        pi_cal=MathCalculations().cal_pi()
        print(pi_cal)
        first=round((pi_cal/2),4)
        last=pi_cal
        mid=round((first+last)/2,4)
        while(first<=last):
            y1=round(mid-(pi_cal/2),4)
            y2=MathCalculations().sin_cal(mid)
            if y1==y2:
                return round(mid,4)
                break
            elif y1<y2:
                first=mid+0.0001
            else:
                last=mid-0.0001
            mid=round((first+last)/2,4)

 # Calculation for Length

 def cal_length(self,alpha_val,radius):
        cos_x=alpha_val/2;
        z=MathCalculations().cos_cal(cos_x);
        length=2*radius*(1-z)
        return round(length,4)









#Grade Calculator
phy_marks = int(input("Enter Physics marks:"))
eg_marks = int(input("Enter Enggn. Graphics marks:"))
pps_marks = int(input("Enter PPS marks:"))
bee_marks = int(input("Enter BEE marks:"))
maths_marks = int(input("Enter Maths marks:"))
if phy_marks < 40:
    print("You Fail in Physics ")
else :
    print("You Pass in Physics")
if eg_marks < 40:
    print("You Fail in Enggn. Graphics ")
else :
    print("You Pass in Enggn. Graphics") 
if pps_marks < 40:
    print("You Fail in PPS")
else :
    print("You Pass in PPS")
if bee_marks < 40:
    print("You Fail in BEE")
else :
    print("You Pass in BEE")
if maths_marks < 40:
    print("You Fail in Maths")
else :
    print("You Pass in Maths")
sum = (phy_marks + eg_marks + pps_marks + bee_marks + maths_marks)
agg = (sum / 500) * 100
print("Your Aggregate ",agg,"%")
if agg >= 75:
    print("Grade: Distintion")
elif 75 > agg >60 :
    print("Grade: First Division")
elif 60 > agg > 50 :
    print("Grade: Second Division")
elif 50 > agg > 40 : 
    print("Grade: Third Division")
else :
    print("You failed")
#Output:
#Enter Physics marks: 50
#Enter Enggn. Graphics marks: 60
#Enter PPS marks: 70
#Enter BEE marks: 80
#Enter Maths marks: 90
#You Pass in Physics
#You Pass in Enggn. Graphics
#You Pass in PPS
#You Pass in BEE
#You Pass in Maths
#Your Aggregate  70.0 %
#Grade: First Division
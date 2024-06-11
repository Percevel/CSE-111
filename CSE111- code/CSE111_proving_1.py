import math
def tvolume(w,a,d):
    ans = (math.pi *pow(w,2)* a *( w * a +2540* d ))/10000000
    return ans
cont = False
while cont == False:
    w = float(input("Enter the width of the tire in mm (ex 205): "))
    a = float(input("Enter the aspect ratio of the tire (ex 60): "))
    d = float(input("Enter the diameter of the tire in inches (ex 15): "))
    if w > 0 and a>0 and d>0:
        cont = True
    else:
        print("invalid number, please put a valid number")
print(f"The volume of your tire is {tvolume(w,a,d):.1f}")

import math
def tvolume(w,a,d):
    ans = (math.pi *pow(w,2)* a *( w * a +2540* d ))/10000000
    return ans
while True:
    w = input("Enter the width of the tire in mm (ex 205): ")
    if w.isalpha() == True:
        print(f"'{w}' is not a positive integer. Please enter a positive integer.")
        continue
    elif int(w) > 400:
        print(f"{w} is too large. Please enter a positive integer between 180 and 400")
        continue
    elif int(w) < 180:
        print(f"{w} is too small. Please enter a positive integer between 180 and 400")
    else:
        break

while True:
    a = input("Enter the aspect ratio of the tire (ex 60): ")
    if a.isalpha() == True:
        print(f"'{a}' is not a positive integer. Please enter a positive integer.")
        continue
    elif int(a) > 70:
        print(f"{a} is too large. Please enter a positive integer between 45 and 70")
        continue
    elif int(a) < 45:
        print(f"{a} is too small. Please enter a positive integer between 45 and 70")
    else:
        break
while True:
    d = input("Enter the diameter of the tire in inches (ex 15): ")
    if d.isalpha() == True:
        print(f"'{d}' is not a positive integer. Please enter a positive integer.")
        continue
    elif int(d) > 28:
        print(f"{d} is too large. Please enter a positive integer between 12 and 28")
        continue
    elif int(d) < 12:
        print(f"{d} is too small. Please enter a positive integer between 12 and 28")
    else:
        break
print(f"The approximate volume of your tire is {tvolume(int(w),int(a),int(d)):.1f} milliliters.")

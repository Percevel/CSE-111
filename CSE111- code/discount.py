import datetime

sub = float(input("Please enter the subtotal: "))
weekday = datetime.datetime.now().isoweekday()

if sub >50 and(weekday == 2 or weekday == 3):
    sub = sub- (sub* .1)

print(f"Total: {sub + (sub* .06)}")
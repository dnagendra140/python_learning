#conditional statements
""" 
if
if-else
if-elif-else
nested if
match case """
#if condition it is condition is true executed the code
age=20
if age>=18:
    print("eligibile for vote")#condition is true
#if else it is chocie bitween two condition
age=20
if age>=18:
    print("eligibile for vote")
else:
    print("not eligibile for vote")
#if elif-else its check multipile conditions
marks=75
if marks>=90:
    print("grade  is a")
elif marks>=70:
    print("grad  is b")
elif marks>=50:
    print("grad is c")
elif marks>=35:
    print("pass")
else:
    print("faill")
#nested if it is if statement another if statement
n="monday"
time=9.00
if n=="monday":
    if time==9.00:
        print("ringtone")
    else:
        print(" no ringtone")

else:
    print( "it is not a monday")


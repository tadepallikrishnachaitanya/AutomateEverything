data3 = int(input("Enter Age:"))

if data3 <0:
    print("Enter valid age")
elif data3 < 18: 
    print("Not eligible for Voting")
elif data3 >= 18 and data3 <65:
    print("You are an adult and allowed to vote")
else:
    print("You are happpy now")
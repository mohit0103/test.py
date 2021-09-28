Val=(input("Your name: "))
days=int(input("No of Days you were present:  "))
desig=input("What is your designation? ")
select_month=input("Enter the desired Month: ")
month = {"jan":31, "feb":29, "march":31, "apr":30, "may":31, "jun":30, 
       "jul":31, "aug":31, "sep":30, "oct":31, "nov":30, "dec":31}

fee = 0
if desig=="manager":
    if days <=month[select_month]:
        fee+=days * 2000
        over_time = int(input("how many days of overtime: "))
        if over_time >= 0:
            fee+=over_time*(2000/2)
            print(fee)
    else:
        print("Ivalid Choice")

elif desig=="teamleader":
    if days<32:
        fee+=days*1800
        over_time = int(input("how many days of overtime"))
        if over_time >= 0:
            fee+=over_time*(1800/2)
            print(fee)
    else:
        print("Ivalid Choice")

elif desig=="member":
    if days<32:
        fee+=days*1500
        over_time = int(input("how many days of overtime"))
        if over_time >= 0:
            fee+=over_time*(1500/2)
            print(fee)
    else:
        print("Invalid Choice")

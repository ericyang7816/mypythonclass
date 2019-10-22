myName=input("Please input your name(last,first):").strip()
myBirthday=input("Please input your birthday(mm//dd//yyyy):").strip()
myUserName=input("Please input your user name with 3chars:").strip()
myBook=input("Please input your book(title,publisher,year):").strip()

myLastName=myName.split(",")[0]
myFirstName=myName.split(",")[1]

birthMonth=int(myBirthday.split("/")[0])
birthDay=int(myBirthday.split("/")[1])
birthYear=int(myBirthday.split("/")[2])

isLeapYear=birthYear%4==0
isLeapYear=isLeapYear and birthYear%100!=0
isLeapYear=isLeapYear or birthYear%400==0

digits="0123456789"
alphas='abcdefghijklmnopqrstuvwxyz'
special="_"
isValid=myUserName[0] in alphas
isValid=isValid and(myUserName[1] in digits+alphas+special)
isValid=isValid and(myUserName[2] in digits+alphas)

print("My name:"+myFirstName+" "+myLastName)
print("My birthday:%02d/%02d/%4d"%(birthMonth,birthDay,birthYear))
print("My user name:"+myUserName)
print("My book:"+"\t".join(myBook.split(",")))
print("My birth year "+str(birthYear)+" is a leap year:"+str(isLeapYear))
print("My user name "+myUserName+" is Valid:"+str(isValid))

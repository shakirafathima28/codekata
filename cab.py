place = ["tambaram","adayar","ambathur"]
dist = [35,30,50]
price = [5,7,10,12]
print("Where you want to go?:\n 1.Tambaram,2.Adayar,3.Ambathur")
choice= int(input())
if choice == 1:
    kms = dist[0]
    print("The place you have choosed is:Tambaram")
elif choice == 2:
    kms = dist[1]
    print("The place you have choosed is:Adayar")
elif choice == 3:
    kms = dist[2]
    print("The place you have choosed is:Ambathur")
print("Which cab do you prefer?:\n 1.Nano, 2.Micro, 3.Mini, 4.Prime")
select = int (input())
if select == 1:
    rate = price[0]
    print("The cab you have selected is: Nano")
elif select == 2:
    rate = price[1]
    print("The cab you have selected is: Micro")
elif select == 3:
    rate = price[2]
    print("The cab you have selected is: Mini")
elif select == 4:
    rate = price[3]
    print("The cab you have selected is: Prime")
print("The estimated amount is ", kms * rate)

print("Do you confirm your booking? \n 1.Yes or 2.No")
conf = int(input())
if conf==1:
    print("Thanks For Booking")
elif conf==2:
    print("Better Luck Next Time")




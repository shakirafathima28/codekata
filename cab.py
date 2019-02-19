place = ["tambaram","adayar","ambathur"]
dist = [35,30,50]
price = [5,7,10,12]
print("Where you want to go:\n 1.Tambaram,2.Adayar,3.Ambathur")
choice= int(input())
if choice == 1:
    kms = dist[0]
elif choice == 2:
    kms = dist[1]
elif choice == 3:
    kms = dist[2]
print("Which do you prefer?:\n 1.Nano, 2.Micro, 3.Mini, 4.Prime")
select = int (input())
if select == 1:
    rate = price[0]
elif select == 2:
    rate = price[1]
elif select == 3:
    rate = price[2]
elif select == 4:
    rate = price[3]
print("The estimated amount is ", kms * rate)


money_input=int(input("Enter the money"))
coins={'10':0,'5':0,'2':0,'1':0}
if money_input%10==0:
    coins['10']=money_input//10
else:
    coins['10']=money_input//10
    money_input=money_input%10
    if money_input%5==0:
        coins['5']=money_input//5
    else:
        coins['5']=money_input//5
        money_input=money_input%5
        coins['1']=money_input
print(coins.items())
sum=0
for i in coins.values():
    sum+=i
print("The total number of coins needed are ",sum)


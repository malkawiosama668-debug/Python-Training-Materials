is_open=True
tekets=5
while tekets>0 and is_open :
    if tekets==0:
        print("the tekets is empity")
    
    name=input("enter your name: ")
    teket_num=int(input("enter how much tekets you want to purch= "))
    
    if teket_num<=0:
        print("error: cant git thats number of tekets")
    elif teket_num>tekets:
        print("thats no {teket_num} is aveylable")
    elif teket_num>0 and teket_num<=tekets:
        print(f"the seller name is {name} and they selled {teket_num} of tekets ")
        tekets-=teket_num

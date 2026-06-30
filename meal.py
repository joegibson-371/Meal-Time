def main():
    time=input("What time is it?  ")
    hours=convert(time)
    match hours:
        case hours if 7<= hours <=8:
          print("breakfast time")
        case hours if 12<= hours <=13:
          print("lunch time")
        case hours if 18<= hours <=19:
          print("dinner time")
        
          

 

    


def convert(time):
    T=time.strip().split(":")
    hours=int(T[0])+float(int(T[1])/60)
    return(hours)



main()
def main():
    time=input("What time is it?  ")
    hours=am_pm_convert(time)
    match hours:
        case hours if 7<= hours <=8:
          print("breakfast time")
        case hours if 12<= hours <=13:
          print("lunch time")
        case hours if 18<= hours <=19:
          print("dinner time")
        
          
#Define the function that converts a string typed in the form xx:xx or x:xx
#into a float wich represents the number of hours.
def convert(time):
    T=time.strip().split(":")
    hours=int(T[0])+float(int(T[1])/60)
    return(hours)

# here we define another function to convert from 12 to 24 hour time to allow users 
#to input xx:xx am or xx:xx pm
def am_pm_convert(time):
   time=time.strip()
   if time[-2]=="a":
      time=time[:-2]
      return convert(time)
   elif time[-2]=="p":
      time=time[:-2]
      return (convert(time) +12)
   else:
      return (convert(time))



main()
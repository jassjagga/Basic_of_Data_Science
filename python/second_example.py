indian=["samosa","daal","naan"]
chinses=["egg role", "pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish Name: ")

if dish in indian:
    print("indian")
elif dish in chinses:
    print("chineses")
elif dish in italian:
    print("italian")
else:
    print("Sorry! i don't know Thanks")

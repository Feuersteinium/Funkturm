## MONTHLY FILE GEN
## DATE PLOTTER


## VARIABLES
## ------------------------------------------

month = input("What month is it? \n >> " )
year = input("What year is it? \n  >> ")

## ------------------------------------------


## CONVERTER
year = str(year)
month = int(month)

print("[CONVERSIONS] DONE!")




## EVERY MONTH-NUMBER LOWER THAN 10 WILL BE WRITTEN WITH AN 0 IN FRONT.
if month < 10:
    monthfinal = "0" + str(month)
    print("[MONTH PLOTTER] Month " + str(month) + " is lower than 10! Added a decimal in front of " + str(month))
else:
    monthfinal = str(month)


print("[MONTH PLOTTER] DONE!")
print("[OBSIDIAN LINK FORMATTER] Formatting link! Programm will add a few empty lines for better copying \n \n \n \n \n \n \n")

## THE FINAL PLOTTER
## THIS PROGRAMM WILL GENERATE THE OUTPUT, WHICH CAN BE COPYED IN OBSIDIAN LATER!

for x in range(1,32):
    ## THIS WILL CHECK IF IT NEED TO ADD A 0
    ## IF IT DOESNT, DAYFINAL WILL BE REWRITTEN TO STRING
    if x < 10:
        dayfinal = str(0) + str(x)
    else: 
        dayfinal = str(x)
    
    print("[[" + dayfinal + "-" + monthfinal + "-" + year + "]]")


print("\n \n \n \n \n \n \n[OBSIDIAN LINK FORMATTER] Everything done! Exiting...")

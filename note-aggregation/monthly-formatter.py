## MONTHLY FILE GEN
## DATE PLOTTER


## VARIABLES
## ------------------------------------------

year = input("What year is it? \n  >> ")
monthd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthm = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

## ------------------------------------------


## CONVERTER
year = str(year)

print("[CONVERSIONS] DONE!")



def is_leap_year():
    if int(year) % 4 == 0:
        print("Year is a leap year. Continiuing with a 29 day February :D")
        monthd[1] = 29

is_leap_year()

## EVERY MONTH-NUMBER LOWER THAN 10 WILL BE WRITTEN WITH AN 0 IN FRONT.


print("[MONTH PLOTTER] DONE!")
print("[OBSIDIAN LINK FORMATTER] Formatting link! Programm will add a few empty lines for better copying \n \n \n \n \n \n \n")

## THE FINAL PLOTTER
## THIS PROGRAMM WILL GENERATE THE OUTPUT, WHICH CAN BE COPYED IN OBSIDIAN LATER!


def yearmap():

    f = open(str(year) + ".md", "a")
    runner = 1

    for element in monthd:
        f.write("## " + monthm[runner -1] + "\n")

        if runner < 10:
            monthfinal = "0" + str(runner)
        else:
            monthfinal = str(runner)
        runner += 1

        # We cant start at 0 as usual, as the first day of the month would be day 0
        for x in range(1,element +1):

            ## THIS WILL CHECK IF IT NEED TO ADD A 0
            ## IF IT DOESNT, DAYFINAL WILL BE REWRITTEN TO STRING
            if x < 10:
                dayfinal = str(0) + str(x)
            else: 
                dayfinal = str(x)
    
            f.write("[[" + dayfinal + "-" + monthfinal + "-" + year + "]]" + "\n")
    f.close()


print("\n \n \n \n \n \n \n[OBSIDIAN LINK FORMATTER] Everything done! Exiting...")


yearmap()
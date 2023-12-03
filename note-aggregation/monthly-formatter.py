## MONTHLY FILE GEN
## DATE PLOTTER

## Constants

monthm = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

## Functions

def input_year():
    try:
        return(int(input("What year is it? \n  >> ")))
    except ValueError:
        print("The given year isnt a valid integer, exiting...")
        exit()

## This function takes a year as an input and will output a list with the lenght of each month in days. Important for leap years

def generate_month_lenght(year):
    monthd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
               monthd[1] = 29
    return(monthd)

## Parameters
## year = year
## mlist == month list (List with the lenght of each month)


def yearmap(year, mlist):

    # Open markdown file with the name of the year
    f = open(str(year) + ".md", "a")

    # Setting runner variable to 1 (representing January)
    runner = 1

    # Looping through each item of the month list, in order to generate a Obsidian style link for every day.
    for element in mlist:
        # Heading
        f.write("## " + monthm[runner -1] + "\n")

        # 0 in front of the digit?
        if runner < 10:
            monthfinal = "0" + str(runner)
        else:
            monthfinal = str(runner)
        runner += 1

        # We can't start at 0 as usual, as the first day of the month would be day 0.(starting at 1 and ending at n+1 instead of starting at 0 and ending at n.)
        for x in range(1,element +1):

            ## THIS WILL CHECK IF IT NEED TO ADD A 0
            ## IF IT DOESNT, DAYFINAL WILL BE REWRITTEN TO STRING
            if x < 10:
                dayfinal = str(0) + str(x)
            else: 
                dayfinal = str(x)
    
            f.write("[[" + dayfinal + "-" + monthfinal + "-" + str(year) + "]]" + "\n")
    f.close()


## Run everything :D

yr = input_year()
yearmap(yr, generate_month_lenght(yr))

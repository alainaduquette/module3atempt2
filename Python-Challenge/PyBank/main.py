import csv
#open CSV
with open("C:\\Users\\alain\\Documents\\Bootcamp\\Python Challenge\\Python-Challenge\\PyBank\\Resources\\budget_data.csv", "r") as file:
    #set header and tell system to read
    header=file.readline() 
    #set the name of the reader
    my_reader = csv.reader(file, delimiter=",")
    #set the below variables to "0" to eventually have them add up
    total = 0
    month_counter = 0
    sum = 0
    #create a blank dictionary to add the data to
    changedict={}
    
    #set a for loop to go through every row of data. The first if statement is saying if this is the first month set the temp to the pofit
    for date,profit in my_reader:
        if (month_counter == 0):
            temp = int(profit)
       #the else will complete the rest of the for loops through the rows to generate the rest of the dictionary 
        else:
            changedict[date] = int(profit) - temp
            temp = int(profit)
        #adding a tick to the month counter
        month_counter = month_counter + 1

        total = total + int(profit)

#the below is to be printed out
print("Financial Analysis")
print("")
print("----------------------------")
print("")
print("Total Months: " + str(month_counter))
print("Total: " + str(total))
##print("Average Change: " + str(int(changedict) / int(len(changedict))))
print("Greatest Increase in Profits: " + max(changedict, key=changedict.get), max(changedict.values()))
print("Greatest Decrease in Profits: " + min(changedict, key=changedict.get), min(changedict.values()))

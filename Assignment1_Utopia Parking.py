 #Utopia Parking app, records customers check in time, compares it to check out time. 
#Calculates a total parking time then calculates a total balance based off this.
#Then payments are input until remaining balance is zero.
#Loop to the main menu
while True:
    print("""\nWelcome to Utopia Parking
Menu:
1. View Rates
2. Check in and Check out
3. Exit""")
#Get a menu selection and validate input to ensure the number 1, 2, or 3 is entered 
    selection = (input('\nSelect an option: '))
    if selection == '1':
        print ("""\nOur rates are as follows:
0 - 1 hour  \t$19
1 - 2 hours \t$29
2 - 3 hours \t$79
3 - 24 hours\t$89""")
        input("\nPress ENTER to return to the main menu: ")
        
#If selection is 2, input the check in/check out hours, minutes, and calculate the total time then display it in hours and minutes
    elif selection == '2':
        print('\nCheck in time')
        check_in_hour = (input('     hour (0-23): '))
        check_in_min = (input('     minute (0-59): ')) 
        
        print('\nCheck out time')
        check_out_hour = (input('     hour (0-23): '))       
        check_out_min = (input('     minute (0-59): '))

#Validate input of check in hours/minutes and check out hours/minutes to ensure a number that is within range is entered.
        valid = False 
        while True:
            in_hour = ""        #will store any numeric character 
            count = 0           #keep count of how many characters are input
            for x in check_in_hour:
                if "0" <= x <= "9":
                    in_hour += x
                    count += 1
                else:
                    count = 99  #if condition for x not met this will trigger invalid inputs failing validation
                    break
            if count == 1 and "0" <= in_hour <= "9":  # Single-digit numbers (0-9)
                valid = True
                break
            elif count == 2 and "00" <= in_hour <= "23":  # Two-digit numbers (10-23)
                valid = True
                break
            else:
                print('\n** Invalid check-in time. Please try again.\n')
                break
        if not valid:   #loop back to main menu if validation fails
            continue    
         
#Repeat validation as above on next input           
        valid = False
        while True:                 
            in_min = ""
            count = 0
            for x in check_in_min:
                if "0" <= x <= "9":
                    in_min += x
                    count += 1
                else:
                    count = 99
                    break
            if count == 1 and "0" <= in_min <= "9":  
                valid = True
                break
            elif count == 2 and "00" <= in_min <= "59":  
                valid = True
                break
            else:
                print('\n** Invalid check-in time. Please try again.\n')
                break
        if not valid:
            continue  

#Repeat validation as above on next input
        valid = False
        while True:
            out_hour = ""
            count = 0
            for x in check_out_hour:
                if "0" <= x <= "9":
                    out_hour += x
                    count += 1
                else:
                    count = 99
                    break
            if count == 1 and "0" <= out_hour <= "9":  
                valid = True
                break
            elif count == 2 and "00" <= out_hour <= "23":  
                valid = True
                break
            else:
                print('\n** Invalid check-out time. Please try again.\n')
                break
        if not valid:
            continue

#Repeat validation as above on next input
        valid = False
        while True:
            out_min = ""
            count = 0
            for x in check_out_min:
                if "0" <= x <= "9":
                    out_min += x
                    count += 1
                else:
                    count = 99
                    break
            if count == 1 and "0" <= out_min <= "9": 
                valid = True
                break
            elif count == 2 and "00" <= out_min <= "59": 
                valid = True
                break
            else:
                print('\n** Invalid check-out time. Please try again.\n')
                break
        if not valid:
            continue   
        
        
        #convert inputs to int for calculations
        in_hour = int(in_hour)
        in_min = int(in_min)
        out_hour = int(out_hour)
        out_min = int(out_min)


        

#Convert check in and check out times to minutes to enable calculation of total time
        total_in_min = (in_hour * 60 + in_min)
        total_out_min = (out_hour * 60 + out_min)
        if total_in_min > total_out_min:
            total_out_min += 1440  #add 24 hours (in minutes) to check out hour to take into account stays that check in pre midnight and check out post midnight

       
#Calculate total time and check that total time not = 0
        tot_time = (total_out_min) - (total_in_min)
        if tot_time == 0:
            print('\n** Invalid check-out time. Please try again.\n')
            continue
#Calculate total hours component
        tot_hours = tot_time // 60
#Calculate total minutes component, so that i can display hours and minutes seperately as shown in example
        tot_min = tot_time % 60
              
#Display the total hours and total minutes as per example
        print(f'\n** Total parking time: {tot_hours} hours and {tot_min} minutes')
       
#Calculate the total amount due using multi-way decision structure
        if tot_time > 0 and tot_time <= 59:
            total_due = 19
            print (f'** Total Due: ${total_due}')
        elif tot_time >= 60 and tot_time <= 119:
            total_due = 29
            print (f'** Total Due: ${total_due}')
        elif tot_time >= 120 and tot_time <= 179:
            total_due = 79
            print (f'** Total Due: ${total_due}')
        else:
            total_due = 89
            print (f'** Total Due: ${total_due}')
        
#Take payment, utilising an accumulator to decrease from the total due until remaining balance = $0
#Utilise accumulator "collected" to keep running total on how much cash collected.
#Initialise variable for remaining balance to the same as total due calculated above
#Initialise amount collected variable to $0
        remain_bal = total_due
        collected = 0
#Get user to input their money, validate the input, update total collected
        while remain_bal > 0:
            tendered = (input('   Insert cash amount (1, 2, 5, 10, 20, 50, 100 only): '))
            if (tendered == '1' or tendered == '2' or tendered == '5' or tendered == '10' or
                tendered == '20' or tendered == '50' or tendered == '100'):
                tendered = int(tendered)
            else:
                print('\nYou must enter a valid amount.\n')
                continue
            collected += tendered
            print(f'** Total collected: ${collected}')
#Calculate remaining balance by deducting amount tendered until remaining balance is zero
            remain_bal -= tendered
#Calculate change, if total collected exceeds remaining balance
            if remain_bal < 0:
                change = remain_bal * -1
                print(f'** Change due: ${change}')
                input('\n** Please collect your change. Press Enter when done: ')
            else:    
                print(f'** Remaining balance: ${remain_bal}')
    
        print('\nThanks for parking with us!\n')
        break
#If they press 3, thank them and break out of program
    elif selection == '3':
        print('\nThank you for using Utopia Parking!\n')
        break
#Else any other number sends them back to main menu, thereby validating the inital input
    else:
        print('\n** Invalid option. Please try again.\n')


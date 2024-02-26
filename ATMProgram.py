''' 
Python Program inspired from ATM machines. I have created this ATM program which works similar to the conditions of the ATM which we use in our real life . This program has been made after so many trails as well as failures but at last it worked 
'''
# Program by Zidaan
from time import sleep
import pyttsx3
engine = pyttsx3.init()
import os
# Accepting Input
engine.say("Welcome to ATM of The Enamored Bank ")
engine.runAndWait()
print("Welcome to ATM of The Enamored Bank ")
# Accepting inputs.
engine.say("Please enter the total money in your Bank Account : ")
engine.runAndWait()
amount = float(input("Total Money in your Bank Account : "))
engine.say("Please decide your 4 digit ATM pin")
engine.runAndWait()
pin = int(input("Decide the ATM pin : "))
# Only 4 digits allowed loop begins :
if (len(str(pin)) == 4):
  # ATM Interactive Mode :
  os.system("cls")
  engine.say("Dear customer your ATM pin has been registered and is hidden for security reasons \n Please dont share it with an unknown person")
  engine.runAndWait()
  while (1):
    engine.say("Enter 0 to Logout or Exit from program.")  
    engine.runAndWait()
    print("Enter 0 -> Logout or Exit from program.")
    engine.say("Enter 1 to View Balance.")
    engine.runAndWait()
    print("Enter 1 -> View Balance")
    engine.say("Enter 2 to  Withdraw Cash ")
    engine.runAndWait()
    print("Enter 2 -> Withdraw Cash")
    engine.say("Enter 3 to deposit cash.")
    engine.runAndWait()
    print("Enter 3 -> Cash Deposit")
    engine.say("Enter 4 to change your ATM pin")
    engine.runAndWait()
    print("Enter 4 -> Change Pin")
    engine.say("Dear customer enter any number to proceed")
    engine.runAndWait()
    choice = int(input("Enter any number to proceed...."))
    print("\n\n")
# User's Choice :
    if (choice == 0):
        print("Logging Out ...")
        sleep(2)
        engine.say("You have been logged out. Thank you !! for using our ATM")
        engine.runAndWait()
        print("You have been logged out. Thank you !! for using our ATM")
        break
# ATM Working Mode Enabled 
    elif choice in (1, 2, 3, 4):
        trails = 3
        while (trails != 0):
            engine.say("Please enter your 4-digit PIN")
            engine.runAndWait()
            guess = int(input("Please enter your 4-digit PIN : "))

            if (guess == pin):
                engine.say("Access Granted !!!")
                engine.runAndWait()
                print("Access Granted !!!")
# Loop of Access Granted :
                if choice == 1:
                    engine.say("Fetching Account Details...")
                    engine.runAndWait()
                    print("Fetching Account Details...")
                    sleep(1.5)
                    engine.say("Your current balance is Rs",amount)
                    engine.runAndWait()
                    print("Your current balance is Rs",amount)
                    break
                elif choice == 2:
                    engine.say("Cash withdrawl mode....")
                    engine.runAndWait()
                    print("Cash withdrawl mode....")
                    sleep(1.5)
# Cash Withdrawl Functionality
                    while (1):
                        engine.say("Enter the amount you wish to withdraw : ")
                        engine.runAndWait()
                        withdraw= float(
                            input("Enter the amount you wish to withdraw : "))

                        if (withdraw > amount):
                            engine.say("Insufficient Balance !!! Please enter a lower amount!")
                            engine.runAndWait()
                            print("Insufficient Balance !!!")
                            print("Please enter a lower amount!")
                            continue

                        else:
                            print("Withdrawing Rs.", withdraw)
                            engine.say("Are you sure . \n Click Y to proceed and N to cancel")
                            engine.runAndWait()
                            confirm = input("Are you sure ? (Y/N)")
                            if confirm in ('Y', 'y'):
                                amount = amount - withdraw
                                engine.say("Cash withdrawn successfully !!!")
                                engine.runAndWait()
                                print("Sucessfully withdrawn : Rs", withdraw)
                                engine.say("Here is your updated balance !!!")
                                engine.runAndWait()
                                print("Balance Amount : Rs",amount )
                                break

                            else:
                                print("Cancelling transaction...")
                                sleep(1)
                                engine.say("Transaction Cancelled!\n\n")
                                engine.runAndWait()
                                print("Transaction Cancelled!\n\n")
                                break

                    break
# Cash Deposit Functionality
                elif (choice == 3):
                    engine.say("Loading Cash Deposit...")
                    engine.runAndWait()
                    print("Loading Cash Deposit...")
                    sleep(1.5)
                    engine.say("Enter the amount you wish to deposit ")
                    engine.runAndWait()

                    deposit = float(
                        input("Enter the amount you wish to deposit > "))
                    print("Depositing Rs.", deposit)
                    engine.say("Are you sure . \n Click Y to proceed and N to cancel")
                    engine.runAndWait()
                    confirm = input("Are you sure ? (Y/N) ")
                    if confirm in ('Y', 'y'):
                        amount = amount + deposit
                        engine.say("Amount deposited sucessfully !!!")
                        engine.runAndWait()
                        print("Amount deposited : Rs.", deposit)
                        engine.say("Here is your updated balance !!!")
                        engine.runAndWait()
                        print("Updated balance : Rs",amount)
                    else:
                        print("Cancelling transaction...")
                        sleep(1)
                        engine.say("Last Transaction Cancelled !!!")
                        engine.runAndWait()
                        print("Last Transaction Cancelled !!!")

                    break
# Pin Change Functionality
                elif (choice == 4):
                    engine.say("Loading PIN Change...")
                    engine.runAndWait()
                    print("Loading PIN Change...")
                    sleep(1.5)
                    engine.say("Enter your new PIN > ")
                    engine.runAndWait()

                    new = int(input("Enter your new PIN > "))
                    if (len(str(new))== 4):

                     print("Changing PIN to : ",new)
                     engine.say("Are you sure . \n Click Y to proceed and N to cancel")
                     engine.runAndWait()
                     confirm = input("Are you sure ? (Y/N) ")
                     if confirm in ('Y', 'y'):
                         pin = new
                         engine.say("PIN changed successfully! \n\n")
                         engine.runAndWait()
                         print("PIN changed successfully! \n\n")
                     else:
                         print("Cancelling PIN change...")
                         sleep(1)
                         engine.say("Process Cancelled!\n\n")
                         engine.runAndWait()
                         print("Process Cancelled!\n\n")
                         break
                    else:
                        engine.say("Sorry your ATM pin must be of 4 digits only")
                        engine.runAndWait()
                        print("Sorry your ATM pin must be of 4 digits only")
                        sleep(1)
                        engine.say("Redirecting to pin change ")
                        engine.runAndWait()
                        print("Redirecting to pin change ")
                        sleep(1.5)
                        continue

                    break
# For Pin Mismatch :
            else:
                trails = trails - 1
                engine.say("Access Denied !!! Incorrect pin")
                engine.runAndWait()
                print("Access Denied !!! Incorrect pin \n Number of tries left -",trails)
                sleep(1)
# Logging Out Functionality
        else:
            engine.say("Exiting...")
            engine.runAndWait()
            print("Exiting...")
            sleep(2)
            engine.say("You have been logged out. Thank you !!! ")
            engine.runAndWait()
            print("You have been logged out. Thank you !!! ")
            break
# Invalid Input
    else:
        engine.say("Sorry !!! Invalid input! ")
        engine.runAndWait()
        print("Sorry !!! Invalid input!")
        continue
# Enď of Functionalities
# First if termination
else:
 engine.say("Sorry only 4 digits pin is acceptable \n Data Deleted !!! \n Please restart the program ")   
 engine.runAndWait()
 print("Sorry only 4 digits pin is acceptable")
 print("Data Deleted !!!")
 print("Please restart the program")
 exit()
# End of Program

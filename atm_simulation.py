def main():
    atm_pin = 1912
    answer = "yes"
    total = 5000
    user_pin = int(input("Enter your pin for transaction : "))
    if user_pin == atm_pin:
        print(f"Your Balance is ₹ {total} ")
        while answer == "yes":
            user_choice = input("Do you want to deposit , withdrawn or check the balance?  ").lower().strip()
            if user_choice == "deposit":
                deposit = int(input("Enter the amount you want to deposit:"))
                total = total + deposit
                print(f"{deposit} ₹ is deposited from your account and your current balance is :₹ {total}")
            elif user_choice == "withdrawn":
                withdrawn = int(input("Enter the amount you want to withdrawn:"))
                if withdrawn > total:
                    print("You cannot withdrawn the amount above your total balance")
                else:
                    total = total - withdrawn
                    print(f"{withdrawn} ₹ is withdrawl from your account and your current balance is :{total}₹")
            elif user_choice == "check balance":
                print(f"Your current balance is : ₹ {total}")
            else:
                print("Please select valid option !!!!")
            answer = input("Do you want to do another transaction or not ? ").lower().strip()
            if answer == "no":
                break
        print("THANKS FOR USING ATM 😃")
        
main()   
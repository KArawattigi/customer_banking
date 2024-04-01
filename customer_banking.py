# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

#prompt string is printed to standard output  
#data_type this is the data type for the input that the user is expectedto enter  
def get_valid_user_input(prompt, data_type):
    while True:
        input_value = input(prompt)
        try:
            # Try to convert the user input to the specified data type
            # this code may raise an exception
            input_value = data_type(input_value)
            return input_value
        except ValueError:
            # If the conversion fails, print an error message and prompt again
            print("#Error 001 : Invalid input. Please enter a valid ", data_type.__name__)
    

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = get_valid_user_input("Enter the initial balance for the Saving Account :",float)
    savings_interest = get_valid_user_input("Enter the interest rate (apr) for the Saving Account :",float)
    savings_maturity = get_valid_user_input("Enter the number of months for the Saving Account :",int)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated savings account balance is: {updated_savings_balance: ,.2f}")
    print(f"You earned {interest_earned:,.2f} in interest for the period of {savings_maturity} months at {float(savings_interest): .4f}% apr")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    
    cd_balance = get_valid_user_input("Enter the initial balance for the CD Account :",float)
    cd_interest = get_valid_user_input("Enter the interest rate (apr) for the CD Account :",float)
    cd_maturity = get_valid_user_input("Enter the number of months for the CD Account :",int)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated CD account balance is: {updated_cd_balance: ,.2f}")
    print(f"You earned {interest_earned:,.2f} in interest for the period of {cd_maturity} months at {float(cd_interest): .4f}% apr")

if __name__ == "__main__":
    # Call the main function.
    main()


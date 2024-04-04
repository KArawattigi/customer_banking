# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account



# prompt : string is printed to standard output promptingthe user for an input  
# data_type : this is the data type for the input that the user is expected to enter 
# get_user_input frunction converts the userinput to the expected datatype   
def get_user_input(prompt, data_type):
    while True:
        input_value = input(prompt)
        try:
            # default input value to 0 if escape sequence is entered  
            input_value = 0 if input_value=="~~N" else input_value
            # Try to convert the user input to the specified data type
            # if an exception occurs it means the datatype is invalid 
            input_value = data_type(input_value)
            return input_value
        except ValueError:
            # print the error message and prompt the user again
            print(f"#Error 001 : Invalid input. Please enter a valid {data_type.__name__} ")
            print("Enter ~~N to Exit input value will default to 0")



# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = get_user_input("Enter the initial balance for the Saving Account :",float)
    savings_interest = get_user_input("Enter the interest rate (apr) for the Saving Account :",float)
    savings_maturity = get_user_input("Enter the number of months for the Saving Account :",int)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated savings account balance is: {updated_savings_balance: ,.2f}")
    print(f"You earned {interest_earned:,.2f} in interest for the period of {savings_maturity} months at {float(savings_interest): .4f}% apr")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    
    cd_balance = get_user_input("Enter the initial balance for the CD Account :",float)
    cd_interest = get_user_input("Enter the interest rate (apr) for the CD Account :",float)
    cd_maturity = get_user_input("Enter the number of months for the CD Account :",int)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated CD account balance is: {updated_cd_balance: ,.2f}")
    print(f"You earned {interest_earned:,.2f} in interest for the period of {cd_maturity} months at {float(cd_interest): .4f}% apr")

if __name__ == "__main__":
    # Call the main function.
    main()


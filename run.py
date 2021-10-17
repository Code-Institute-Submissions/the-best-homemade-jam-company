import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_best_homemade_jam_company')

def get_sales_figures():
    """
    Get jam sales data imputed by the user.
    Run a while loop requesting the jam sales util recive a valid string.
    A valid string must contain ten numbers separated by commas.
    """
    while True:
        print("Welcome, to type your jam sales")
        print("-Follow this example: 2,4,6,8,10,12,14,18,20")
        print("-Insert ten numbers;")
        print("-Separate the numbers by commas.\n")

        numbers_str = input("Please insert your jam sales numbers here:")
        """
        print(f"You insert {numbers_str}.")
        """
    
        jam_sales = numbers_str.split(",")
        validate_numbers(jam_sales)

def validate_numbers(values):
    print(values)
    """
    In the try, all string values are converted into integers.
    The ValueError raise message appears if the user didn't type 10 values or if the strings cannot be converted into integers.
    """
    try:
        if len(values) != 10:
            raise ValueError(
                f"You need to provide 10 values. You have type {len(values)}"
            )
    except ValueError as e:
        print(f"Sorry, but you insert invalid data. {e}, please try again.\n")
    
get_sales_figures()
        


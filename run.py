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
        print(jam_sales)

get_sales_figures()
        


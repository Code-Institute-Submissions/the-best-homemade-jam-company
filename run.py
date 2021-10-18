import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
        print("to type your jam sales,")
        print("follow this example: 2,4,6,8,10,12,14,18,20")
        print("-Insert ten numbers;")
        print("-Separate the numbers by commas.\n")

        numbers_str = input("Please insert your jam sales numbers here:")
        """
        print(f"You insert {numbers_str}.")
        """
        jam_sales = numbers_str.split(",")

        if validate_numbers(jam_sales):
            print("You insert valid information!")
            break

    return jam_sales


def validate_numbers(values):
    print(values)
    """
    In the try, all string values are converted into integers.
    The ValueError raise message appears if the user didn't type 10 values
    or if the strings cannot be converted into integers.
    """
    try:
        [int(value) for value in values]
        if len(values) != 10:
            raise ValueError(
                f"You need to provide 10 values. You have type {len(values)}"
            )
    except ValueError as e:
        print(f"Sorry, but you insert invalid data. {e}, please try again.\n")
        return False

    return True   


def update_sales(numbers):
    """
    Update sales worksheet.
    Add new row with the user imput values.
    """
    print("Adding new sales data...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(numbers)
    print("New sales data added. Worksheet updated.\n")


def update_surplus(numbers):
    """
    Update surplus worksheet.
    Add new row with the user imput values.
    """
    print("Adding new surplus data...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(numbers)
    print("New surplus data added. Worksheet updated.\n")


def surplus_numbers(sales_row):
    """
    Calculate surplus values.
    Take the stock values and subtract the number of jam sold.

    Positive surplus means jam jars from that day's stock that were not sold.
    Negative surplus means jam jars that were not available that day
    because that day's stock was all sold out,
    so it was booked and taken from the next day's stock.
    """
    print("Extracting surplus values...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(f"row(stock) {stock_row}")
    print(f"row(sales) {stock_row}")

    surplus_values = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_values.append(surplus)
    pprint(surplus_values)

    return surplus_values


def main():
    """
    Run all functions
    """
    numbers = get_sales_figures()
    sales_numbers = [int(num) for num in numbers]
    update_sales(sales_numbers)
    add_new_surplus_numbers = surplus_numbers(sales_numbers)
    update_surplus(add_new_surplus_numbers)


print("Welcome to The Best Homemade Jam Company Data Automation,")           
main()

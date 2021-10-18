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
    Get jam sales data imputed by the user
    Run a while loop requesting the jam sales util recive a valid string
    A valid string must contain ten numbers separated by commas.
    """

    while True:
        print("to type your jam sales,")
        print("follow this example: 2,4,6,8,10,12,14,18,20")
        print("-Insert ten numbers;")
        print("-Separate the numbers by commas.\n")

        numbers_str = input("Please insert your jam sales numbers here:")
        jam_sales = numbers_str.split(",")

        if validate_numbers(jam_sales):
            print("You insert valid information!")
            break

    return jam_sales


def validate_numbers(values):
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


def update_worksheet(row_numbers, worksheet):
    """
    Insert a list of integers into a worksheet with the values given
    Update the worksheet.
    """
    print(f"Adding new {worksheet} data\n")
    update_worksheet_numbers = SHEET.worksheet(worksheet)
    update_worksheet_numbers.append_row(row_numbers)
    print(f"New {worksheet} data added. {worksheet} worksheet updated.\n")


def collect_last_5_entries():
    """
    Collects the 5 last entries for each jam flavour from sales worksheet
    Returns data as a list of lists
    """
    sales = SHEET.worksheet("sales")

    columns = []
    for ind in range(1, 10):
        column = sales.col_values(ind)
        columns.append(column[-4:])

    return columns


def new_stock_numbers(numbers):
    """
    Add 10% to calculate the average stock.
    """
    print("Calculating stock values...\n")
    add_new_stock_numbers = []

    for column in numbers:
        int_column = [int(num) for num in column]
        
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        add_new_stock_numbers.append(round(stock_num))

    return add_new_stock_numbers


def main():
    """
    Run all functions.
    """
    numbers = get_sales_figures()
    jam_sales = [int(num) for num in numbers]
    update_worksheet(jam_sales, "sales")

    sales_columns = collect_last_5_entries()
    stock_numbers = new_stock_numbers(sales_columns)
    update_worksheet(stock_numbers, "stock")
    

print("Welcome to The Best Homemade Jam Company Data Automation,")
main()
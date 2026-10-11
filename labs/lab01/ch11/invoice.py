# Starting file for Lab 1 Chapter 11 invoice.py program
# James Kim, 10/10/2026, DEV128 Fall2026

from datetime import datetime, timedelta, date

# Input for invoice date
def get_invoice_date():
    while True:
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")    
        try:
            dt = datetime.strptime(invoice_date_str, "%m/%d/%Y").date()
            # Validate date is either current date or in the past
            if dt > date.today():
                print("Invoice must be today's date or earlier.")
            else:
                return dt
        # Validate the date format is correct
        except ValueError:
            print("Invalid date format. Enter date in MM/DD/YYYY format. Try again")

def main():
    print("The Invoice Due Date program")
    print()

    # Loops again if user continues
    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        # Prints days overdue if overdue
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        # Prints days left
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        while True:
            again = input("Continue? (y/n): ").lower()
            # Validates correct input
            if again in ["y", "n"]:
                break
            print("Invalid choice. Please enter y or n.")
        
    print("Bye!")      

if __name__ == "__main__":
    main()

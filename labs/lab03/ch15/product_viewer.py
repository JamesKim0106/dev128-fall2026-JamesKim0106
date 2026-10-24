# Starting file for Lab 3 - product_viewer.py
# James Kim, DEV 128, Lab 3, 10/24/2026

# import the classes from objects.py
from objects import Product, Media, Book, Movie, Album

# function to display the list of products
def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.getDescription()}")
    print()

# function to display the details of a product
def show_product(product):
    w=18
    print("PRODUCT DATA")
    print(f"{'Name:':{w}}{product.name}")
    if isinstance(product, Book):
        print(f"{'Author:':{w}}{product.author}")
    if isinstance(product, Movie):
        print(f"{'Year:':{w}}{product.year}")
    if isinstance(product, Album):
        print(f"{'Artist:':{w}}{product.artist}")
    # Check if product is an instance of Media or its subclasses and displays the format if true.
    if isinstance(product, Media):
        print(f"{'Format:':{w}}{product.format}")
    # Displays the price and discounted price of the product
    print(f"{'Price:':{w}}{product.price:.2f}") 
    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    print()

# main function to run the program
def main():
    print("The Product Viewer program")
    print()
    
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Book("The Big Short", 15.95, 34, "Paperback", "Michael Lewis"),
                Movie("The Holy Grail", 14.99, 68, "DVD", 1975),
                Album("Nightmare", 9.99, 10, "CD", "Avenged Sevenfold")) # added an Album product to the products tuple
    show_products(products)

    choice = "y"
    while choice.lower() == "y":
        # Prompt the user to enter a product number and validate the input
        while True: # loop until a valid product number is entered
            try:
                number = int(input("Enter product number: "))
                if number < 1 or number > len(products): # check if the number is out of range
                    print("Invalid product number. Please try again.")
                else:
                    break # exit the loop if a valid product number is entered
            except ValueError: # catch the ValueError exception if the input is not an integer
                print("Invalid input. Please enter a number.")

        product = products[number-1]
        show_product(product)

        choice = input("View another product? (y/n): ")
        while choice.lower() not in ("y", "n"): # loop until a valid choice is entered
                print("Invalid choice. Please enter 'y' or 'n'.")
                choice = input("View another product? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()

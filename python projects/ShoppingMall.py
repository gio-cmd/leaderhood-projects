cart = []
total_price = 0

visit_or_not = input("Hello! Do you want to visit the Shopping Mall? (Yes/No): ")
if visit_or_not.lower() != "yes":
    print("Goodbye then!")
    quit()

print("Welcome To Our Shopping Mall")

def format_with_bullet_point(items):
    for i, item in enumerate(items):
        print(f"{i}. {item}")

def add_to_cart(section_items):
    choices = input("Enter the numbers of the items you want to add to the cart (separated by commas): ")
    selected_items = []

    if ',' not in choices:
        choices = [choices] 
    else:
        choices = choices.split(',')

    for choice in choices:
        choice = choice.strip()
        if choice.isdigit() and 0 <= int(choice) < len(section_items):
            choice = int(choice)
            selected_item = list(section_items.keys())[choice]
            print(f"You selected: {selected_item}")
            add_or_back = input("Do you want to 'Add to Cart' or 'Back'? (Type 'add' or 'back'): ").lower()
            if add_or_back == 'add':
                cart.append(selected_item)
                selected_items.append(selected_item)
                print(f"{selected_item} added to cart.")
            elif add_or_back == 'back':
                print(f"{selected_item} not added to cart.")
            else:
                print("Invalid option. Item not added to cart.")
        else:
            print(f"Invalid choice '{choice}'. Ignored.")

    return selected_items

# CLOTHING
print("In the clothing section, we have various items you can choose:")
clothing_items = {
    "Christmas family matching outfit": 20.99,
    "Investor fashion T-shirt": 15.99,
    "Fort Polk North Louisiana Classic Established T-Shirt": 12.99,
    "Men shaper vest": 18.99,
    "Detroit jacket": 29.99,
    "₿oss Fashion Hoodie": 24.99,
    "White eagle T-shirt": 14.99,
    "Grey striped hoodie": 22.99,
    "Sweater with GOA logo": 19.99,
    "Nike Air Force 1 white": 89.99
}

print("Clothing:")
format_with_bullet_point(clothing_items)
selected_clothing = add_to_cart(clothing_items)
total_price += sum(clothing_items[item] for item in selected_clothing)

# ENTERTAINMENT
print("In the entertainment section we offer many items that could make your day happier!:")
entertainment_items = {
    "Ioshi 75'' Media Console": 299.99,
    "Iphone 15": 1299.99,
    "PlayStation 5": 499.99,
    "Custom build PC": 899.99,
    "Mobile Vinyl Record Player": 79.99,
    "Harry potter movie collection": 59.99,
    "trampoline": 129.99,
    "slide": 89.99,
    "sledge": 49.99,
    "skate": 39.99
}

print("Entertainment:")
format_with_bullet_point(entertainment_items)
selected_entertainment = add_to_cart(entertainment_items)
total_price += sum(entertainment_items[item] for item in selected_entertainment)

# BOOKSTORE
print("In the bookstore section we have many interesting books which will help you financially and socially:")
bookstore_items = {
    "Rich dad poor dad": 12.99,
    "How full is your bucket": 9.99,
    "How to win and influence people": 14.99,
    "Atomic habits": 19.99,
    "The psychology of money": 16.99,
    "Getting to yes": 11.99,
    "Learn lucid dreaming": 17.99,
    "All parts of harry potter": 49.99,
    "Life skills 101": 10.99,
    "How to talk to anybody": 13.99
}

print("Books:")
format_with_bullet_point(bookstore_items)
selected_book = add_to_cart(bookstore_items)
total_price += sum(bookstore_items[item] for item in selected_book)

# FITNESS
print("In the fitness section we offer many items to help you stay fit:")
fitness_items = {
    "Commercial GYM bench": 199.99,
    "Commercial GYM incline bench": 249.99,
    "Weighted plates": 49.99,
    "Weighted dumbbells": 39.99,
    "Boxing gloves": 29.99,
    "Treadmill": 499.99,
    "trampoline": 129.99,
    "Leg press": 299.99,
    "Leg extension": 179.99,
    "Wall-mounted pull-up bar": 49.99
}

print("Fitness:")
format_with_bullet_point(fitness_items)
selected_fitness = add_to_cart(fitness_items)
total_price += sum(fitness_items[item] for item in selected_fitness)



print("\nItems in your cart:")
format_with_bullet_point(cart)
print(f"Total Price: ${total_price:.2f}")

print("pay\n")

pay = float(input("amount: "))

if pay < total_price:
    print("You dont have enough money")
elif pay == total_price:
    print("Thanks for paying")
else:
    print("Thanks for the tip :)")
# Holiday planner: This program is used to calculate the cost of a holiday based on user inputs. 
# Print a welcome message.
print("Welcome to the Holiday Planner!")
# Provide instructions for the user to follow when using the program.
print("*" * 70)
print("This program will help you plan your next holiday.")
print("You can choose your desired destination from a list of available cities. ")
print("Please follow the prompts to enter your travel details.")
print("*" * 70)
# Define a list of cities that the user can choose from when inputting their travel plans.
cities = ["Paris", "Cairo", "Tokyo"]
# Define the flight prices for each city
city_prices = {
    "Cairo": 350,
    "Paris": 250,
    "Tokyo": 550
}

def input_validation():
    """
    Validates the user input for the city name, number of hotel nights, and rental days.

    Returns:
    - city_flight (str): the chosen city to fly to.
    - hotel_nights (int): the number of hotel nights.
    - rental_days (int): the number of rental days for the car.
    """
    # Validate user input for city name:
    while True:
        try:
            city_flight = input(f"\nEnter the city you intend to fly to {cities}: ").capitalize()
            if city_flight in cities:
               break
            else: 
                raise NameError
                
        except NameError:
            print("Please choose one of the cities provided")

    # Validate user input for number of nights to stay in a hotel:       
    while True:
        try:
            hotel_nights = int(input("\nEnter the number of nights you will be staying at a hotel: "))
            break

        except ValueError:
            print("Please enter a valid number. Only digit input is valid for number of nights.")

    # Validate user input for number of days to hire a car: 
    while True:
        try:
            rental_days = int(input("\nEnter the number of days that you will be hiring a car for: "))
            break
        except ValueError:
            print("Please enter a valid number. Only digit input is valid for number of rental days.")

    return city_flight, hotel_nights, rental_days  
    

city_flight, hotel_nights, rental_days  = input_validation()

# Define the hotel cost 
def hotel_cost ():
    """
    Calculates the cost of the hotel stay based on the number of hotel nights.

    Returns:
    - cost (int): the total cost of the hotel stay.
    """
    night_price = 100
    return hotel_nights * night_price


# Define the plane cost 
def plane_cost(): 
    """
    Calculates the cost of the flight based on the chosen city to fly to.

    Returns:
    - cost (int): the total cost of the flight.
    """    
    return  city_prices[city_flight]


# Define the car rental days
def car_rental ():
    """
    Calculates the cost of the car rental based on the number of rental days.
     Returns:
    - cost (int): the total cost of car rental.
    """   
    car_daily_cost =  30 
    return car_daily_cost * rental_days


def holiday_cost():
    """
    Calculate the total cost of a holiday, including hotel, plane, and car rental fees.

    This function relies on the `hotel_cost`, `plane_cost`, and `car_rental` functions
    to calculate the individual costs of each element of the holiday. It then adds these
    costs together to obtain the total cost of the holiday.

    Returns:
        total cost (int): the total cost of the holiday.

    Example:
        >>> holiday_cost()
        1410
    """
    total_cost = hotel_cost() + plane_cost() + car_rental()
    return total_cost

# Print the details of the holiday cost, including individual costs for plane, hotel, and car rental.
# The `*` character is used to create a line separator, and the `f` string is used to format the cost
# values obtained from the `plane_cost`, `hotel_cost`, and `car_rental` functions.
print()
print("*" * 70)
print(f"Your Total holiday cost will be: {holiday_cost()}") 
print("    Details:") 
print(f"\tPlane cost: {plane_cost()}") 
print(f"\tHotel cost: {hotel_cost ()}") 
print(f"\tCar cost: {car_rental ()}") 
print("*" * 70)

def length_converter():
    print("\n--- Length Converter ---")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Centimeter to Meter")
    print("4. Meter to Centimeter")

    choice = int(input("Enter choice: "))

    if choice == 1:
        m = float(input("Enter value in meters: "))
        print("Kilometers:", m / 1000)

    elif choice == 2:
        km = float(input("Enter value in kilometers: "))
        print("Meters:", km * 1000)

    elif choice == 3:
        cm = float(input("Enter value in centimeters: "))
        print("Meters:", cm / 100)

    elif choice == 4:
        m = float(input("Enter value in meters: "))
        print("Centimeters:", m * 100)

    else:
        print("Invalid choice!")


def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Gram to Kilogram")
    print("2. Kilogram to Gram")
    print("3. Pound to Kilogram")
    print("4. Kilogram to Pound")

    choice = int(input("Enter choice: "))

    if choice == 1:
        g = float(input("Enter grams: "))
        print("Kilograms:", g / 1000)

    elif choice == 2:
        kg = float(input("Enter kilograms: "))
        print("Grams:", kg * 1000)

    elif choice == 3:
        lb = float(input("Enter pounds: "))
        print("Kilograms:", lb * 0.453592)

    elif choice == 4:
        kg = float(input("Enter kilograms: "))
        print("Pounds:", kg / 0.453592)

    else:
        print("Invalid choice!")


def time_converter():
    print("\n--- Time Converter ---")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    print("3. Minutes to Hours")
    print("4. Hours to Minutes")

    choice = int(input("Enter choice: "))

    if choice == 1:
        sec = float(input("Enter seconds: "))
        print("Minutes:", sec / 60)

    elif choice == 2:
        mins = float(input("Enter minutes: "))
        print("Seconds:", mins * 60)

    elif choice == 3:
        mins = float(input("Enter minutes: "))
        print("Hours:", mins / 60)

    elif choice == 4:
        hrs = float(input("Enter hours: "))
        print("Minutes:", hrs * 60)

    else:
        print("Invalid choice!")


# Main Program
while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Length")
    print("2. Weight")
    print("3. Time")
    print("4. Exit")

    option = int(input("Choose type: "))

    if option == 1:
        length_converter()
    elif option == 2:
        weight_converter()
    elif option == 3:
        time_converter()
    elif option == 4:
        print("Exiting Program...")
        break
    else:
        print("Invalid Option! Try again.")

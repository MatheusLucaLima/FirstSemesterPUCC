"""
This is a project created as an example of an airplane system.
It was made by a team of 5 students for a colage project. 
Although this version was developed only by me, it is based on the original project. 
"""

import mysql.connector

#Change it to work properly
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="************",
    database="airplane_system",
    buffered=True
    )

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        flight_number INT PRIMARY KEY UNIQUE,
        origin VARCHAR(100),
        destination VARCHAR(100),       
        scale_number INT,
        price FLOAT,
        seats_available INT,
        passengers TEXT
    )
               """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS passengers (
        cpf INT PRIMARY KEY UNIQUE,
        name VARCHAR(150),
        telephone VARCHAR(20),
        age INT,
        flights TEXT
    )
               """)


def register_flight (dicionary_flights, list_flights_available):
    while True:
        flight_number = int (input("Enter the flight number: "))
        try:
            if flight_number in dicionary_flights:
                print("Flight number already exists.")
            else:
                origin = input("Enter the origin: ")
                destination = input("Enter the destination: ")
                scale_number = int(input("Enter the number of scales: "))
                price = float(input("Enter the price: "))
                seats_available = int(input("Enter the number of seats available: "))
                list_passengers = []
                flight_info = [origin, destination, scale_number, price, seats_available, list_passengers]
                dicionary_flights[flight_number] = flight_info
                list_flights_available.append(flight_number)
                cursor.execute("INSERT INTO flights (flight_number, origin, destination, scale_number, price, seats_available, passengers) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                               (flight_number, origin, destination, scale_number, price, seats_available, str(list_passengers)))
                connection.commit()
                print("Flight registered successfully.")
                break
        except ValueError:
            print("Invalid input. Please try again.")

def register_passenger(dicionary_passengers, cpf):
    while True:
        if cpf in dicionary_passengers:
            print("Passenger already registered.")
        else:
            name = input("Enter the passenger's name: ")
            telephone = input("Enter the passenger's telephone number: ")
            age = int(input("Enter the passenger's age: "))
            list_flights = []
            dicionary_passengers[cpf] = [name, telephone, age, list_flights]
            cursor.execute("INSERT INTO passengers (cpf, name, telephone, age, flights) VALUES (%s, %s, %s, %s, %s)",
                           (cpf, name, telephone, age, str(list_flights)))
            connection.commit()
            print("Passenger registered successfully.")
        break
        
def book_ticket(dicionary_passengers, dicionary_flights, list_flights_available):
    while True:
        cpf = int(input("Enter the passenger's CPF: "))
        if cpf not in dicionary_passengers:
            register_passenger(dicionary_passengers, cpf)
        if cpf in dicionary_passengers:
            for flight in dicionary_flights.keys():
                print(f"Flight {flight}: {dicionary_flights[flight]}")
            flight_number = int(input("Enter the flight number: "))
            if flight_number in dicionary_flights and flight_number in list_flights_available:
                if dicionary_flights[flight_number][4] > 0:
                    if dicionary_passengers[cpf][2] < 18:
                        print("Passenger is underage and cannot book a ticket.")
                        break
                    else:
                        dicionary_flights[flight_number][4] -= 1
                        dicionary_flights[flight_number][5].append(cpf)
                        dicionary_passengers[cpf][3].append(flight_number)
                        cursor.execute("UPDATE flights SET seats_available = %s, passengers = %s WHERE flight_number = %s",
                                       (dicionary_flights[flight_number][4], str(dicionary_flights[flight_number][5]), flight_number))
                        cursor.execute("UPDATE passengers SET flights = %s WHERE cpf = %s",
                                       (str(dicionary_passengers[cpf][3]), cpf))
                        connection.commit()
                        print(f"Flight {flight_number} booked for passenger {dicionary_passengers[cpf][0].upper()}.")
                        if dicionary_flights[flight_number][4] == 0:
                            list_flights_available.remove(flight_number)
                        print("Ticket booked successfully.")
                else:
                    print("No seats available for this flight.")
            else:
                print("Flight not found or not available.")
        break




def cancel_ticket(dicionary_passengers, dicionary_flights, list_flights_available):
    while True:
        cpf = int(input("Enter the passenger's CPF: "))
        if cpf in dicionary_passengers:
            for flight in dicionary_flights.keys():
                print(f"Flight {flight}: {dicionary_flights[flight]}")
            flight_number = int(input("Enter the flight number to cancel: "))
            if flight_number in dicionary_flights and flight_number in list_flights_available:
                if cpf in dicionary_flights[flight_number][5]:
                    dicionary_flights[flight_number][4] += 1
                    dicionary_flights[flight_number][5].remove(cpf)
                    dicionary_passengers[cpf][3].remove(flight_number)
                    print(f"Flight {flight_number} cancelled for passenger {dicionary_passengers[cpf][0].upper()}.")
                    cursor.execute("UPDATE flights SET seats_available = %s, passengers = %s WHERE flight_number = %s",
                                      (dicionary_flights[flight_number][4], str(dicionary_flights[flight_number][5]), flight_number))
                    cursor.execute("UPDATE passengers SET flights = %s WHERE cpf = %s",
                                   (str(dicionary_passengers[cpf][3]), cpf))
                    connection.commit()
                    if dicionary_flights[flight_number][4] == 1:
                        list_flights_available.append(flight_number)
                    print("Ticket cancelled successfully.")
                else:
                    print("Passenger does not have a ticket for this flight.")
            else:
                print("Flight not found or not available.")
        else:
            print("Passenger not registered.")
        break



def flight_consult(dictionary_flights, list_flights_available):
    choice =int(input("How would you like to consult a flight: type 1 to consult by number, type 2 to consult by origin, or type 3 to consult by destination: "))
    if choice == 1:
        for flight_number in list_flights_available:
            print(f"Flight {flight_number}")
        flight_number = int(input("Enter the flight number: "))
        if flight_number in dictionary_flights:
            print(f"Flight {flight_number}: {dictionary_flights[flight_number]}")
        else:
            print("Flight not found.")
    elif choice == 2:
        origin = input("Enter the origin: ")
        if origin in dictionary_flights.get(flight_number, [])[0]:
            print(f"Flights from {origin}:")
            for flight_number, flight_info in dictionary_flights.items():
                if flight_info[0] == origin:
                    print(f"Flight {flight_number}: {flight_info}")
        else:
            print("No flights found for this origin.")
    elif choice == 3:
        destination = input("Enter the destination: ")
        if destination in dictionary_flights.get(flight_number, [])[1]:
            print(f"Flights to {destination}:")
            for flight_number, flight_info in dictionary_flights.items():
                if flight_info[1] == destination:
                    print(f"Flight {flight_number}: {flight_info}")
        else:
            print("No flights found for this destination.")
    else:
        print("Invalid choice.")


def flight_minor_scale(dicionary_flights):
    print("To find the flight with the minor scale, please enter the origin and destination.")
    origin = input("Enter the origin: ")
    destination = input("Enter the destination: ")
    if origin and destination in dicionary_flights.get(flight_number, [])[0:2]:
        min_scale = 10000  # A large number to ensure any valid scale will be smaller
        flight_with_min_scale = None
        for flight_number, flight_info in dicionary_flights.items():
            if flight_info[0] == origin and flight_info[1] == destination:
                if flight_info[2] < min_scale:
                    min_scale = flight_info[2]
                    flight_with_min_scale = flight_number
        if flight_with_min_scale is not None:
            print(f"Flight with the minor scale from {origin} to {destination} is {flight_with_min_scale} with {min_scale} scales.")
        else:
            print("No flights found with the specified origin and destination.")



def passager_flight(dicionary_flights, dicionary_passengers):
    choice = int(input("How would you like to see the passengers of a flight: type 1 to see the passengers by flight number, or type 2 to see the passages bought by a passenger: "))
    if choice == 1:
        if not dicionary_flights:
            print("No flights registered.")
            return
        for flight_number in dicionary_flights.keys():
            print(f"Flight {flight_number}")
        flight_number = int(input("Enter the flight number: "))
        if flight_number in dicionary_flights:
            passengers = dicionary_flights[flight_number][5]
            if passengers:
                for i in dicionary_flights[flight_number][5]:
                    print(f"Passenger CPF: {i}, Name: {dicionary_passengers[i][0]}, Telephone: {dicionary_passengers[i][1]}, Age: {dicionary_passengers[i][2]}")
            else:
                print("No passengers booked for this flight.")
        else:
            print("Flight not found.")
    elif choice == 2:
        cpf = int(input("Enter the passenger's CPF: "))
        if cpf in dicionary_passengers:
            flights = dicionary_passengers[cpf][3]
            if flights:
                print(f"Flights booked by passenger {dicionary_passengers[cpf][0]} (CPF: {cpf}):")
                for flight_number in flights:
                    print(f"Flight Number: {flight_number}, Origin: {dicionary_flights[flight_number][0]}, Destination: {dicionary_flights[flight_number][1]}")
            else:
                print("No flights booked by this passenger.")
        else:
            print("Passenger not registered.")
    else:
        print("Invalid choice.")

        



def main():
    print("Welcome to the Airplane System!")
    dicionary_passengers = {} # Dictionary to store passengers, It contains the passenger's CPF (brazilian ID), name and telephone number.
    dicionary_flights = {} #Dictionary to store flights, It contains the flight's number, origin, destination, scale's number, price and number of seats available.
    list_flights_available = []
    cursor.execute("SELECT * FROM flights")
    dicionary_flights = {row[0]: [row[1], row[2], row[3], row[4], row[5], eval(row[6])] for row in cursor.fetchall()}
    cursor.execute("SELECT * FROM passengers")
    dicionary_passengers = {row[0]: [row[1], row[2], row[3], eval(row[4])] for row in cursor.fetchall()}
    list_flights_available = list(dicionary_flights.keys()) 

    while True:
        print("\n"*2)
        print("-" * 50)
        print("\nMenu:")
        print("0. Exit")
        print("1. Register Flight")
        print("2. Register Passenger")
        print("3. Book Ticket")
        print("4. Cancel Ticket")
        print("5. Consult Flight")
        print("6. Check Flight With Minor Scale")
        print("7. Check Passengers of a Flight")
        choice = int (input("Enter your choice: "))
        print("\n"*2)
        print("-" * 50)
        if choice == 1:
            register_flight(dicionary_flights, list_flights_available)
        elif choice == 2:
            cpf = int(input("Enter the passenger's CPF: "))
            register_passenger(dicionary_passengers, cpf)
        elif choice == 3:
            book_ticket(dicionary_passengers, dicionary_flights, list_flights_available)
        elif choice == 4:
            cancel_ticket(dicionary_passengers, dicionary_flights, list_flights_available)
        elif choice == 5:
            flight_consult(dicionary_flights, list_flights_available)
        elif choice == 6:
            flight_minor_scale(dicionary_flights)
        elif choice == 7:
            passager_flight(dicionary_flights, dicionary_passengers)    
        elif choice == 0:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
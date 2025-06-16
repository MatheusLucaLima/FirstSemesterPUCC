"""
This program monitors personal sustainability.
It was the final project for the first semester of the
Software Engineering course at the PUC-CAMPINAS University.
It was developed by a group of 6 students, but this version was
developed only by myself. 
"""

import mysql.connector

#change it to use properly
conecxtion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="****",
    database="sustainability_monitoring_system"
)

cursor = conecxtion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        date DATE NOT NULL,
        water_consumption FLOAT NOT NULL,
        energy_consumption FLOAT NOT NULL,
        waste_production FLOAT NOT NULL,
        transport VARCHAR(50) NOT NULL        
        )
               """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sustainability_scores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        water_sustainability VARCHAR(20) NOT NULL,
        energy_sustainability VARCHAR(20) NOT NULL,
        waste_sustainability VARCHAR(20) NOT NULL,
        transport_sustainability VARCHAR(50) NOT NULL,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES user_data(id)
    )
               """)


#Questions of sustainability:
def get_name():
    name = input("What is your name? ")
    return name

#current date
def question1():
    day = input("1.Witch day is today? (Year/Mouth/Day) ")
    return day

#water consumption
def question2(water_liters=None):
    if water_liters is None:
        water_liters = float(input("2.How many liters of water did you use today? "))
    water_sustainability = None
    if water_liters < 150:
        water_sustainability = "High Sustainability"
    elif water_liters < 200:
        water_sustainability = "Moderate Sustainability"
    else:
        water_sustainability = "Low Sustainability"
    return water_sustainability, water_liters


#energy consumption
def question3(energy_kwh=None):
    if energy_kwh is None:
        energy_kwh = float(input("3.How many kWh of energy did you use today? "))
    energy_sustainability = None
    if energy_kwh < 5:
        energy_sustainability = "High Sustainability"
    elif energy_kwh < 10:
        energy_sustainability = "Moderate Sustainability"
    else:
        energy_sustainability = "Low Sustainability"
    return energy_sustainability, energy_kwh


#waste production
def question4(waste_kg=None):
    if waste_kg is None:
        waste_kg = float(input("4.How many percent of waste did you produce today? "))
    waste_sustainability = None
    if waste_kg < 20:
        waste_sustainability = "High Sustainability"
    elif waste_kg < 50:
        waste_sustainability = "Moderate Sustainability"
    else:
        waste_sustainability = "Low Sustainability"
    return waste_sustainability, waste_kg


def try_except_one_two(transport):
    while True:
        try:
            value = int(input(f"Please, if you have used {transport.upper()} type 1 if you haven't used it today type 2: "))
            if value == 1 or value == 2:
                return value
            else:
                print("Please, type 1 for yes and 2 for no.")
        except ValueError:
            print("Invalid input. Please enter a number.")


#kind of transportation
def question5():
    print("5.Have you used this kind of transportation today? ")
    public_transport = try_except_one_two("public transportation")
    bycicle =  try_except_one_two("bycicle")
    walking =  try_except_one_two("walking")
    oil_car =  try_except_one_two("oil car")
    electric_car =   try_except_one_two("electric car")
    transport_sustainability = None
    if public_transport == 2 and bycicle == 2 and walking == 2 and electric_car == 2 and oil_car == 2:
        transport_sustainability = "High Sustainability"
    if (public_transport == 1 or bycicle == 1 or walking == 1 or electric_car == 1) and oil_car == 2:
        transport_sustainability = "High Sustainability"
    elif (public_transport == 1 or bycicle == 1 or walking == 1 or electric_car == 1) and oil_car == 1:
        transport_sustainability = "Moderate Sustainability"
    else:
        transport_sustainability = "Low Sustainability"
    return transport_sustainability


def save_data():
    name = get_name()
    date = question1()
    water_sustainability, water_liters = question2()
    energy_sustainability, energy_kwh = question3()
    waste_sustainability, waste_kg = question4()
    transport_sustainability = question5()
    cursor.execute("""
        INSERT INTO user_data (name, date, water_consumption, energy_consumption, waste_production, transport)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, date, water_liters, energy_kwh, waste_kg, transport_sustainability))
    conecxtion.commit()
    print("Data saved successfully!")

    cursor.execute("""
        INSERT INTO sustainability_scores (water_sustainability, energy_sustainability, waste_sustainability, transport_sustainability, user_id)
        VALUES (%s, %s, %s, %s, LAST_INSERT_ID())
    """, (water_sustainability, energy_sustainability, waste_sustainability, transport_sustainability))
    conecxtion.commit()
    print("Sustainability scores saved successfully!")        



def change_data():
    name = input("Enter the name of the user whose data you want to change: ")
    cursor.execute("SELECT * FROM user_data WHERE name = %s", (name,))
    choise = int(input("What do you want to change? \n 1.Name \n 2.Date \n 3.Water consumption \n 4.Energy consumption \n 5.Waste production \n 6.Public transport \n Please, type your choice: "))
    if choise == 1:
        new_name = input("Enter the new name: ")
        cursor.execute("UPDATE user_data SET name = %s WHERE name = %s", (new_name, name))
    elif choise == 2:
        new_date = input("Enter the new date (YYYY-MM-DD): ")
        cursor.execute("UPDATE user_data SET date = %s WHERE name = %s", (new_date, name))  
    elif choise == 3:
        new_water_consumption = float(input("Enter the new water consumption in liters: "))
        cursor.execute("UPDATE user_data SET water_consumption = %s WHERE name = %s", (new_water_consumption, name))
        water_sustainability, water_liters = question2(new_water_consumption)
        cursor.execute("UPDATE sustainability_scores SET water_sustainability = %s WHERE user_id = (SELECT id FROM user_data WHERE name = %s)", (water_sustainability, name))
    elif choise == 4:
        new_energy_consumption = float(input("Enter the new energy consumption in kWh: "))
        cursor.execute("UPDATE user_data SET energy_consumption = %s WHERE name = %s", (new_energy_consumption, name))
        energy_sustainability, energy_kwh = question3(new_energy_consumption)
        cursor.execute("UPDATE sustainability_scores SET energy_sustainability = %s WHERE user_id = (SELECT id FROM user_data WHERE name = %s)", (energy_sustainability, name))        
    elif choise == 5:
        new_waste_production = float(input("Enter the new waste production in kg: "))
        cursor.execute("UPDATE user_data SET waste_production = %s WHERE name = %s", (new_waste_production, name))
        waste_sustainability, waste_kg = question4(new_waste_production)
        cursor.execute("UPDATE sustainability_scores SET waste_sustainability = %s WHERE user_id = (SELECT id FROM user_data WHERE name = %s)", (waste_sustainability, name))  
    elif choise == 6:
        transport_sustainability = question5()
        cursor.execute("UPDATE user_data SET transport = %s WHERE name = %s", (transport_sustainability, name))
        cursor.execute("UPDATE sustainability_scores SET transport_sustainability = %s WHERE user_id = (SELECT id FROM user_data WHERE name = %s)", (transport_sustainability, name))
    else:
        print("Invalid choice. Please try again.")
    conecxtion.commit()


def delete_data():
    name = input("Enter the name of the user whose data you want to delete: ")
    cursor.execute("DELETE FROM user_data WHERE name = %s", (name,))
    cursor.execute("DELETE FROM sustainability_scores WHERE user_id = (SELECT id FROM user_data WHERE name = %s)", (name,))
    conecxtion.commit()
    print(f"Data for {name} deleted successfully!")


def show_users_data():
    cursor.execute("SELECT name as Name, date as Date, water_consumption as Water, energy_consumption as Energy, waste_production as Waste, transport as Transport FROM user_data")
    for row in cursor.fetchall():
        print(row)


def show_sustainability_scores():
    cursor.execute("SELECT water_sustainability as Water, energy_sustainability as Energy, waste_sustainability as Waste, transport_sustainability as Transport FROM sustainability_scores")
    for row in cursor.fetchall():
        print(row)


def main():
    while True:
        print("\n"*2)
        print("-" * 50)
        print("Welcome to the Personal Sustainability Monitoring System!")
        print("Type 1: Create a new user")
        print("Type 2: Change user data")
        print("Type 3: Delete user data")
        print("Type 4: Show users data")
        print("Type 5: Show sustainability scores")
        print("Type 6: Exit")
        choice = input("Please, type your choice: ")
        if choice == "1":
            print("\n"*2)
            print("-" * 50)
            print("\n"*2)
            save_data()
        elif choice == "2":
            print("\n"*2)
            print("-" * 50)
            print("\n"*2)
            change_data()
        elif choice == "3":
            print("\n"*2)
            print("-" * 50)
            print("\n"*2)
            delete_data()
        elif choice == "4":
            print("\n"*2)
            print("-" * 50)
            print("\n"*2)
            show_users_data()
        elif choice == "5":
            print("\n"*2)
            print("-" * 50)
            print("\n"*2)
            show_sustainability_scores()
        elif choice == "6":
            print("Closing the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if  __name__ == "__main__":
    main()
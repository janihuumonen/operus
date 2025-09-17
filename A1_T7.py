print("Calculate fuel consumption.")
Feed = input("Enter travel distance(kilometers): ")
Distance = int(Feed)
Feed = input("Enter fuel usage(liters): ")
FuelUsage = int(Feed)
Consumption = 100 * FuelUsage / Distance
Consumption = int(Consumption) # floor
print(f"Fuel consumption is {Consumption} l per 100 km")


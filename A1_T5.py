print("Calculate the area of a wall.")
Feed = input("Enter the width in meters: ")
Width = int(float(Feed)) # truncate
Feed = input("Enter the height in meters: ")
Height = int(float(Feed)) # truncate
print(f"Width is {Width} m and height is {Height} m.")
Area = Width * Height
print(f"The wall will be {Area} square meters.")

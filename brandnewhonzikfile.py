import random
waterLevel = 0
contin = True
while contin == True:
    riseWater = input("Would you like to rise the water? y or n\n")

    if "y" in riseWater:
        waterLevel += random.randint(0,10)
    else:
        waterLevel -= random.randint(0,3)
    print(f"The water level is {waterLevel}")

    would = input("Would you like to continue? y or n\n")
    if "y" in would:
        contin = True
    else:
        contin = False

# cars represent total number of available cars
cars = 100

# spacaInACar represents free space in a car for passengers apart from driver.
spaceInACar = 4

# Total number of drivers.
drivers = 30

# Total number of passengers
passengers = 90

# cars not being used due to lack of drivers.
carsNotDriven = cars - drivers

# cars that are being used or driven.
carsDriven = drivers

# This variable represents total available seats for passengers.
carpoolCapacity = carsDriven * spaceInACar

# Average number of passengers per carsDriven.
averagePassengersPerCar = passengers / carsDriven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", carsNotDriven, "empty cars today."
print "We have", passengers, "to carpool today."
print "We need to put about", averagePassengersPerCar, "in each car."

print "Hey %s there." % "you."

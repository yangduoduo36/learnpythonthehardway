cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available." # 100
print "There are only", drivers, "drivers available." # 30
print "There will be", cars_not_driven, "empty cars today." # 70
print "We can transport", carpool_capacity, "people today." # 120.0
print "We have", passengers, "to carpool today." #90
print "We need to put about", average_passengers_per_car, "in each car." # 90/30 = 3
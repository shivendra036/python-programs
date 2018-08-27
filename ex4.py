#total cars
cars=100
#space in cars
space_in_a_car=4
#total no. of drivers
drivers=30
#total no. of passangers
passangers=90
#cars not driven
cars_not_driven=cars-drivers
#cars driven
cars_driven=drivers
#total carpool capacity
carpool_capacity=cars_driven*space_in_a_car
#average passangers per car
average_passangers_per_car=passangers/cars_driven


print "there are",cars,drivers,"cars available."
print "there are only",drivers,"drivers available."
print "there will be",cars_not_driven,"empty cars today."
print "we can transport",carpool_capacity,"people today."
print "we have",passangers,"to carpool today."
print "we have to put",average_passangers_per_car,"in each car."

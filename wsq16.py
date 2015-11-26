def file(cars):
    counter = 0
    acity = 0
    ahw = 0
    mprice = 0
    for line in cars:
        if (counter % 2 == 0):
            x = float (line[52:54])
            acity += x
            y = float (line[55:57])
            ahw += y
            z = float (line[42:46])
            mprice += z
        counter += 1
        w = counter/2

        cityaverage = acity/w
        highwayaverage = ahw/w
        priceaverage = mprice/w
        return (cityaverage, highwayaverage, priceaverage)
cars = open("93cars.dat.txt")
(cityaverage, highwayaverage, priceaverage) = file(cars)
print ("average gas mileage in city is: ", cityaverage)
print ("average gas mileage on highway is: ", highwayaverage)
print ("average midrange price of the vehicles in the set is: ", priceaverage)

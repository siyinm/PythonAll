def main():
    cars = ["Ford", "Volvo", "BMW"]
    cars.append("car1")
    cars.append("car1")
    cars.pop(1)
    #cars.remove("car1")
    nofcar1=cars.count("car1")
    print(cars)
    print(nofcar1)
    print(cars.index("car1"))
    recar=cars.reverse()
    print(recar)
    pass

#The list's remove() method only removes the first occurrence of the specified value.

if __name__=='__main__':
    main()

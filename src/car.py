class Car(object):
    def run(self):
        print("run")


class ToyotaCar(Car):
    pass


class TesraCar(Car):
    def auto_run(self):
        print("auto run")


car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

Tesra_car = TesraCar()
Tesra_car.run()
Tesra_car.auto_run()

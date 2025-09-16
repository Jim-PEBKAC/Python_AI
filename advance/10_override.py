class Car:
    def start(self):
        print('시동이 걸린다.')

    def run(self):
        print('차가 시속 50km로 달린다.')

    def stop(self):
        print('차가 멈춘다.')

class MyCar(Car):
    def start(self):
        print('시동이 켜진다')

new = MyCar()
new.start()
new.run()
new.stop()

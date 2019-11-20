
class Tools(object):

    def __init__(self, name):
        self.name = name

    def driver(self):
        print('{} is driving'.format(self.name))


class AirPlane(Tools):
    def fly(self):
        print('{} is flying'.format(self.name))


class Bus(Tools):
    def driving(self):
        print('{} is driving'.format(self.name))


class Barge(Tools):
    def diving(self):
        print('{} is diving'.format(self.name))


if __name__ == '__main__':

    tools = Tools('tool collections')
    tools.driver()

    airplane = AirPlane('aireplane one')
    airplane.fly()
    airplane.driver()

    bus = Bus('443 bus')
    bus.driving()
    bus.driver()

    barge = Barge('barge one')
    barge.diving()
    barge.driver()
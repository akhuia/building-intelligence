class Human:
    def __init__(self):
        self.energy = 100
        self.knowledge = 0

    def study(self):
        self.energy -= 15
        self.knowledge += 8

    def sleep(self):
        self.energy += 20

    def __str__(self):
        return f"Energy: {self.energy}, Knowledge: {self.knowledge}"

me = Human()

print("Initial")
print(me)

print("\nStudying...")
me.study()
print(me)

print("\nSleeping...")
me.sleep()
print(me)







class LightSwitch:
    def __init__(self):
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on

    def state(self):
        return "ON" if self.is_on else "OFF"

switch = LightSwitch()

print(f"Current state: {switch.state()}")

switch.toggle()
print(f"Current state: {switch.state()}")

switch.toggle()
print(f"Current state: {switch.state()}")

    


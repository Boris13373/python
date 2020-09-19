class Road:
    def __init__(self, len, wid):
        self._len = len
        self._wid = wid

    def get(self):
        return f"{self._len} m * {self._wid} m * 25 kg * 5 cm = {(self._len * self._wid * 25 * 5) / 1000} T"
road1 = Road(5000, 20)
print(road1.get())
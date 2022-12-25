import time
import numpy as np


class Serial:
    def __init__(self, n: int) -> None:
        self.__x: list[float] = []
        self.__y: list[float] = []

        self.data: list[float] = []
        self.cur_voltage_value: float = 5.45
        self.time_period = 2

        self.__generate_data(n=n)

    def __generate_data(self, n: int) -> None:
        for i in range(0, n):
            self.__x.append(i / 1000)
            self.__y.append(0.5 + 0.5 * np.sin(50 * i / 1000))

    def update(self) -> None:
        cur_time: float = time.time()

        self.__x, self.__y = [], []

        indexes: list[int] = []
        for i in range(len(self.data)):
            if cur_time - self.data[i][0] < self.time_period:
                self.__x.append(i / len(self.data))
                self.__y.append(self.data[i][1])
            else:
                indexes.append(i)

        for index in reversed(indexes):
            self.data.pop(index)

    def get_x(self) -> list[float]:
        return self.__x

    def get_y(self) -> list[float]:
        return self.__y

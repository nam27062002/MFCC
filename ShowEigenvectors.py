import matplotlib.pyplot as plt
import Training
class Process:
    def __init__(self,data) -> None:
        self.data = data
    def show(self):
        figure, axis = plt.subplots(2,3)   
        axis[0][0].plot(self.data[0].T)
        axis[0][0].set_title("Vector đặc trưng của nguyên âm A")

        axis[0][1].plot(self.data[1].T)
        axis[0][1].set_title("Vector đặc trưng của nguyên âm E")

        axis[0][2].plot(self.data[2].T)
        axis[0][2].set_title("Vector đặc trưng của nguyên âm I")

        axis[1][0].plot(self.data[3].T)
        axis[1][0].set_title("Vector đặc trưng của nguyên âm O")

        axis[1][1].plot(self.data[4].T)
        axis[1][1].set_title("Vector đặc trưng của nguyên âm U")
        plt.show()
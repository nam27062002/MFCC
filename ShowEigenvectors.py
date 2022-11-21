import matplotlib.pyplot as plt
import Training
class Process:
    def __init__(self,data) -> None:
        self.data = data
    def show(self):
        figure, axis = plt.subplots(2,3)   
        for i in range(5):
            axis[0][0].plot(self.data[i]) 
        axis[0][0].set_title("Vector đặc trưng")
        axis[0][1].plot(self.data[0])
        axis[0][1].set_title("Vector đặc trưng của nguyên âm A")

        axis[0][2].plot(self.data[1])
        axis[0][2].set_title("Vector đặc trưng của nguyên âm E")

        axis[1][0].plot(self.data[2])
        axis[1][0].set_title("Vector đặc trưng của nguyên âm I")

        axis[1][1].plot(self.data[3])
        axis[1][1].set_title("Vector đặc trưng của nguyên âm O")

        axis[1][2].plot(self.data[4])
        axis[1][2].set_title("Vector đặc trưng của nguyên âm U")
        plt.show()
# import thư viện
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write
import librosa
import time
from python_speech_features import mfcc
import scipy.io.wavfile as wav
# class xử lí âm thanh
class Process:
    def __init__(self,url,N_MFCC) -> None: # hàm khởi tạo với tham số truyền vào là url voice cần xử lí
        self.F, self.audio = wavfile.read(url)  # F là tần số và audio là tín hiệu
        self.dentaTime = 0.01 # thời gian chia khoảng tín hiệu
        self.E_MAX = 3000000 # năng lượng tối đa khoảng lặng có thể đạt được trong dentaTime s
        self.SpeechSignal = self.setSpeechSignal() # tín hiệu tiếng nói
        self.StableSignal = self.setStableSignal() # tín hiệu ổn định trong tín hiệu tiếng nói 
        self.N_MFCC = N_MFCC
        self.VectorMFCC = self.setVectorMFCC() # vector MFCC
    # trả về tín hiệu gốc
    def getOriginSignal(self) -> list: 
        x = np.arange(len(self.audio))/self.F 
        y = self.audio
        return [x,y]
    
    # trả về tín hiệu lời nói
    def getSpeechSignal(self) -> list: 
        x = np.arange(len(self.SpeechSignal))/self.F 
        y = self.SpeechSignal
        return [x,y]

    # trả về tín hiệu ổn định
    def getStableSignal(self) -> list: 
        x = np.arange(len(self.StableSignal))/self.F 
        y = self.StableSignal
        

        return [x,y]
    
    # hàm tính năng lương tín hiệu
    def signalEnergy(self,arr) -> float: 
        E = 0
        for i in arr:
            E += pow(i,2)
        return E

    # Đầu vào là 1 tín hiệu âm thanh. Trả về tín hiệu chỉ chứa tiếng nói
    def setSpeechSignal(self) -> list:
        # chia tín hiệu thành những tín hiệu nhỏ hơn và lưu ở list arr 
        arr = [] 
        for i in range(len(self.audio)):
            if i%int(self.dentaTime * self.F) == 0:
                arr.append([]) # thêm list con vào arr sau mỗi dentaTime s
            arr[-1].append(self.audio[i]) 
        # tính năng lượng ở mỗi phần tử trong mảng vừa được tạo 
        Energy = []
        for i in arr:
            Energy.append(abs(self.signalEnergy(i)))
        # chỉ chọn những phần tử có năng lượng lớn hơn E_MAX (không phải khoảng lặng)
        ARR = []
        for i in range(len(Energy)):
            if (Energy[i] > self.E_MAX).any():
                ARR.append(arr[i])
        # chuyển ARR từ 2d sang 1d
        x = []
        for i in ARR:
            for j in i:
                x.append(j)
        # trả về tín hiệu tiếng nói
        return x
        
    # đánh dấu vùng ổn định (chia tín hiệu tiếng nói vừa thu được thành 3 phần và lấy phần ở giữa)
    def setStableSignal(self) -> list:
        x = len(self.SpeechSignal)
        arr = []
        for i in range(int(x/3),int(x/3) + 1813,1):
            arr.append(self.SpeechSignal[i])      
        # lưu âm thanh ở vùng ổn định
        m = np.max(np.abs(arr))
        sigf32 = (arr/m).astype(np.float32)
        write('sound.wav', self.F, np.asarray(sigf32))
        return arr

    # vector mfcc
    def setVectorMFCC(self):
        y, sr = librosa.load("sound.wav")
        mfcc = librosa.feature.mfcc(y, sr, n_mfcc=self.N_MFCC)
        return mfcc

    def getvecto(self):
        (rate,sig) = wav.read("sound.wav")
        return mfcc(sig,rate)
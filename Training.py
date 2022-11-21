import SpeechAndSilence
import numpy as np
from dtw import dtw
from python_speech_features import mfcc
class Process:
    def __init__(self,N_MFCC = 13) -> None:
        self.F = 0
        self.N_MFCC = N_MFCC
        self.vowels = ["a","e","i","o","u"]
        self.eigenvectors = self.Training()
    def getEigenvectors(self):
        arr = []
        for i in self.eigenvectors:
            arr.append(np.asarray(i))
        return arr
    def compare(self,url):
        audio = SpeechAndSilence.Process(url,self.N_MFCC)
        eigenvector = audio.VectorMFCC
        standardDeviations = []
        for i in self.eigenvectors:
            standardDeviations.append(self.distanceTwoVector(eigenvector,i))
        min = 1000000000
        index = -1
        for i in range(len(standardDeviations)):
            if standardDeviations[i] < min:
                min = standardDeviations[i]
                index = i
        return [self.vowels[index],f"Dự đoán đây là nguyên âm /{self.vowels[index]}/"]
    def distanceTwoVector(self,vec1,vec2):
        # [[1],[2],[3]]
        s = 0
        for i in range(len(vec1)):
            s += pow(vec1[i][0] - vec2[i][0],2)
        return s
    def Training(self):
        eigenvectors = [] # các vector đặc trưng
        check = True
        for vowel in self.vowels: 
            eigenvector = [] # vector đặc trưng của 1 nguyên âm
            for index in range(1,22):
                url = f"Training/{index}/{vowel}.wav" # url sound (Test/1/a.wav)
                Audio = SpeechAndSilence.Process(url,self.N_MFCC) 
                self.F = Audio.F
                eigenvector.append(Audio.VectorMFCC)
            average = []
            for i in range(len(eigenvector[0])):
                s = 0 
                for j in range(len(eigenvector)):
                    s += eigenvector[j][i]
                average.append(s/len(eigenvector))
            eigenvectors.append(average)
        return eigenvectors

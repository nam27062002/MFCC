from python_speech_features import mfcc
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
(rate,sig) = wav.read("Test/1/a.wav")
print(type(rate))
mfcc_feat = mfcc(sig,rate)
print(type(mfcc_feat))
plt.plot(mfcc_feat)
plt.show()
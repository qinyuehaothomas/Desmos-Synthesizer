# Desmos Synthesizer
## *Synthesizer which allows different sound profile on desmos*
this page acts as "how to use" page and holds the script for some conversion \

# How to use?
Welp, idk how to Fourier Transform using python, so anyone that knows pls help me...
1. Use Audacity to get Fourier Transform *(of your sound profile)* 
    1. load audio, select "Analyse", "Plot Spectrogram", "Export". It will create a txt file.\

1. Put the .txt file into the same folder as python script, and modify the **FILE_NAME** varibale in the script.\

1. Copy the output from console of the programme, **paste after**
**f=** (*relative frequency*) and **v=** (*relative volume*) of Desmos file
1. Input some melody into M array\
For your convinence, you can just type "A1" for A minor, then it will become $A_1$ in desmos.

1. have fun with music!

# Dev Log
## 1. just brute force find peak.
missing extremeling important high-frequency wave with lower amplitude,\
while getting shit tonneof noises.\
Improve algrithm or do fft properly with python

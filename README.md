# Desmos Synthesizer
## *Synthesizer which allows different sound profile on desmos*
this page acts as "how to use" page and holds the script for some conversion \

# How to use?
Welp, idk how to Fourier Transform using python, so anyone that knows pls help me...
1. Use Audacity to get Fourier Transform *(of your sound profile)* 
    1. Load audio
    1. Select a large section of audio(that sound similar)
    1. Select "Analyse"
    1. "Plot Spectrogram"
    1. **size select around 8192**
    1. "Export"
    1. It will create a txt file.

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
Improve algrithm or do fft properly with python\
Yea.. actually i managed to do it, just sound kinda shitty, maybe that's the max capacity it have...\
Tried Other Instument, totally indistinguishable......\
### Solutions (More like ideas)
Why synthesiser piano sound so damn good!?!?
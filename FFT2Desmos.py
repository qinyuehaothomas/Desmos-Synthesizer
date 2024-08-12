from os import path
import os
def current_folder(file_name):
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    return path.join(d, file_name)

FILE_NAME="ViolinA4.txt"
PEAK_COUNT=10 # how many "sine" function you want
with open(current_folder(FILE_NAME),"r") as f:
    data=[i[:-1].split("\t") for i in f.readlines()][1:]

L=list(map(lambda x: [float(x[0]),float(x[1])], data))
peak=[]

# actually threshold should be exponetial...
# peak-finding!!!!!!!!!!
THRESHOLD=20
for i in range(10,len(L)-THRESHOLD):
    if( L[i][1]> L[i-THRESHOLD][1] and  L[i][1]> L[i+THRESHOLD][1] ):
        peak.append(L[i]+[L[i][1]-L[i-THRESHOLD][1]])

peak.sort(key= lambda x:x[2],reverse=True)
MAX_DB=peak[0][1]
MIN_DB=peak[-1][1]
peak=peak[:min(len(peak)-1,PEAK_COUNT)]
print()
print("f=",[round(i[0],5) for i in peak])
print()
print("v=",[round( (i[1]-MIN_DB)/(MAX_DB-MIN_DB) ,8) for i in peak])
print()
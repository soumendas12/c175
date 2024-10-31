import matplotlib.pyplot as plt
import psutil as p
diction={}
for process in p.process_iter():
    diction[process.name()]=p.cpu_percent()
percent=[]
name=[]
name.append(str(max(diction,key=diction.get)))
percent.append(max(diction.values()))
name.append(min(diction,key=diction.get))
percent.append(min(diction.values()))
print(name,percent)
plt.figure(figsize=(9,9))
plt.xlabel("Min-Max CPU Consumption")
plt.ylabel("Usage")
plt.bar(name,percent,width=0.6,color=("blue","black"))
plt.show()
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import numpy as np
ip_delay = [5,15,25,35,45,55,65,75,85,95]
throughput2 = [27,46,38,63,142,144,107,127,200,235]
throughput4 = [65,72,125,141,182,161,354,315,289,313]
throughput8 = [126 ,104,204,304,393,397,406,794,585,794]
throughput16 = [258,236,431,562,683,1090,1172,1316,1353,1689]
plt.figure(figsize=(15,10), dpi=80)
plt.plot( ip_delay, throughput2,marker='o',label='2 threads')
plt.plot(ip_delay,throughput4,marker='+',linestyle='--',color='r',label='4 threads')
plt.plot(ip_delay,throughput8,marker='x',linestyle='-.',color='g',label='8 threads')
plt.plot(ip_delay,throughput16,marker='s',linestyle=':',color='y',label='16 threads')
plt.legend()
plt.xlabel('mean inter process delay time (ms)')
plt.xticks(np.arange(0,130, 10))
plt.ylabel('throughput(ms)')
plt.savefig('system_load.pdf',format='pdf')
plt.show()
plt.close()
no_cores = [2,4,8,16]
execution_time = [242,407,585,1689]
plt1.figure(figsize=(15,10),dpi=80)
plt1.plot(no_cores,execution_time,marker='s',label='exec time(ms)')
plt1.legend()
plt1.xlabel('number of threads')
plt1.ylabel('execution time(ms)')
plt1.savefig('degree_of_contention.pdf',format='pdf')
plt1.show()
plt1.close()

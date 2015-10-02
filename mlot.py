import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import numpy as np
ip_delay = [10,20,30,40,50,60,70,80,90,100]
throughput2 = [0.01459,0.014405,0.0144534,0.0143839,0.01424846,0.0139104,0.0137645,0.013884598,0.013391,0.013260]
throughput4 = [0.01460,0.0145284,0.0145029,0.01443,0.01426,0.013982,0.0138803,0.0137655,0.013576,0.012912]
throughput8 = [0.0139,0.013859,0.0138,0.0139103,0.0137599,0.013562,0.013322,0.013488,0.013296,0.0131952]
plt.figure(figsize=(15,15), dpi=80)
plt.plot(ip_delay,throughput2,marker='s',linestyle='--',color='y',label='2 threads')
plt.plot( ip_delay, throughput4,marker='o',label='4 threads ')
plt.plot(ip_delay,throughput8,marker='+',linestyle='--',color='r',label='8 theads')

plt.legend()
plt.xlabel('mean inter-request delay time')
plt.ylabel('throughput(1000requests /ms)')
plt.savefig('system_load.pdf',format='pdf')
plt.savefig('system_load')
plt.show()
plt.close()
no_cores = [2,4,8]
execution_time = [131.475,125.87,137.495]
plt1.figure(figsize=(15,10),dpi=80)
plt1.plot(no_cores,execution_time,marker='s',label='exec time(sec)')
plt1.legend()
plt1.xlabel('number of threads')
plt1.ylabel('execution time(sec)')
plt1.savefig('degree_of_contention.pdf',format='pdf')
plt1.savefig('degree_of_contention')
plt1.show()
plt1.close()

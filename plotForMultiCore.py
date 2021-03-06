import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import numpy as np
ip_delay = [10,20,30,40,50,60,70,80,90,100]
throughput2 = [0.014656,0.0146284,0.0145029,0.014403,0.014106,0.013982,0.0139803,0.0137655,0.013576,0.012912]
throughput4 = [0.014759,0.0147050,0.01459534,0.0140839,0.01424846,0.0139104,0.0138645,0.013884598,0.013591,0.013760]
throughput8 = [0.013994,0.013959,0.0138094,0.0138103,0.0137599,0.013562,0.013422,0.013488,0.013396,0.0121952]
throughput16 = [0.0138859,0.013992,0.0137768,0.013609,0.013405,0.013503,0.01315,0.012811,0.012837,0.0121661]
plt.figure(figsize=(15,15), dpi=80)
plt.plot(ip_delay,throughput2,marker='s',linestyle='--',color='y',label='2 threads')
plt.plot( ip_delay, throughput4,marker='o',label='4 threads ')
plt.plot(ip_delay,throughput8,marker='+',linestyle='--',color='r',label='8 theads')
plt.plot(ip_delay,throughput16,marker='x',linestyle='-.',color='g',label='16 ms threads')

plt.legend()
plt.xlabel('mean inter-request delay time')
plt.ylabel('throughput(1000requests /ms)')
plt.savefig('system_load.pdf',format='pdf')
plt.savefig('system_load')
plt.show()
plt.close()
no_cores = [2,4,8,16,32]
execution_time = [121.275,120.887,119.495,120.240,142.367]
plt1.figure(figsize=(15,10),dpi=80)
plt1.plot(no_cores,execution_time,marker='s',label='exec time(sec)')
plt1.legend()
plt1.xlabel('number of threads')
plt1.ylabel('execution time(sec)')
plt1.savefig('degree_of_contention.pdf',format='pdf')
plt1.savefig('degree_of_contention')
plt1.show()
plt1.close()

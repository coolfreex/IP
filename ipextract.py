#python3
#ecoding='utf-8'

import time

localtime = time.asctime( time.localtime(time.time()) )

def ipsplit(filepath): #返回所有ip的列表
    with open(filepath,"r+") as f1:
        IP = set()
        IPLIST = []
        for line in f1:
            iplist = line.split( )
            if iplist != [] and len(iplist) == 1:
               iplist2 = ''.join(iplist)
               if iplist2 not in IP:       #查询是否重复
                  IPLIST.append(iplist2)
               else:
                 pass
        return IPLIST




def ipjudge(filepath):
     list = ipsplit(filepath)
     for i in range(len(list)):
      line = list[i]
      list2 = line.split(":")
      print(list2)
      port = int(list2[1])

      with open("%i ip地址.txt" %port, 'a', encoding='utf-8') as f2:
            f2.write(list2[0]+":"+str(port)+"\n")

     with open('ip_port.txt', mode='a') as f3:
      f3.write(localtime)



if __name__ == '__main__':
    filepath = "ip_port.txt"
    ipjudge(filepath)








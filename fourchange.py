#python3
# -*- coding: utf-8 -*-
import re
import time
import os


# errors = set()

def times(filename):
    localtime = time.asctime(time.localtime(time.time()))
    name = filename
    with open(name,"a") as f1:
        f1.write(localtime)


def mkdir():
    path = os.getcwd() + "\\changelog"
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + '创建成功')
    else:
        print(path + ' 目录已存在')
    return path



def read_log():     #读取文档存入集合中#
    logs = set()
    filepath_list = ["D:\ip-test\log\\ftp\success.log"]
    # filepath_list = ["http\success.log","smtp\success.log","ssh\success.log",
    #                  "telnet\success.log","ftp\success.log"]
    for i in range(len(filepath_list)):
      with open(filepath_list[i],"r+") as f1:
          for line in f1:
              if line not  in logs:
                  logs.add(line)
    return logs

def changeSSH():  #查找SSH#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        # print(log_list)
        if log_list[6] == "SSH":
            IP = log_list[3].split(":")
            port = IP[1]
            text = IP[0]+"|"+port+"|SSH"
            with open("changelog\SSHchange.log","a") as f2:
              f2.write(text+"\n")

    times("changelog\SSHchange.log")

def changeHTTP():  #查找 HTTP#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        if "HTTP" in log_list[6]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6].replace("(HTTP)","")
            text = IP[0]+"|"+port+"|HTTP|"+honeypot
            with open("changelog\HTTPchange.log","a") as f2:
              f2.write(text+"\n")

    times("changelog\HTTPchange.log")

def changeSMTP():  #查找SMTP#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        if len(log_list) == 9 and "SMTP" in  log_list[8]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text = IP[0] + "|" + port + "|SMTP|" + honeypot
            with open("changelog\SMTPchange.log","a") as f2:
              f2.write(text+"\n")

    times("changelog\SMTPchange.log")

def changeFTP():   #查找FTP#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        if len(log_list) == 9 and "FTP" in  log_list[8]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text_1 = IP[0] + "|" + port + "|FTP|" + honeypot
            with open("changelog\FTPchange.log","a") as f2:
              f2.write(text_1+"\n")

        elif len(log_list) == 10 and "FTP" in  log_list[8]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text_2 = IP[0] + "|" + port + "|FTP|" + honeypot+"|Nmap"  #Nmap扫描结果#
            with open("changelog\FTPchange.log","a") as f2:
              f2.write(text_2+"\n")


    times("changelog\FTPchange.log")


def changeTelnet():    #查找Telnet#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        if len(log_list) == 9 and "Telnet" in log_list[8]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text_1= IP[0] + "|" + port + "|Telnet|" + honeypot
            with open("changelog\Telnetchange.log","a") as f2:
              f2.write(text_1+"\n")

        elif len(log_list) == 8 and "Nmap" in log_list[7]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text_2 = IP[0]+"|"+port+"|Telnet|"+honeypot+"|Nmap"   #namp扫描#
            with open("changelog\Telnetchange.log","a") as f2:
              f2.write(text_2+"\n")


    times("changelog\Telnetchange.log")

# def errorslogs():
#     with open("error.log","a") as f1:
#         for error in errors:
#             f1.write(error+"\n")

def write():
    mkdir()
    changeSSH()
    changeHTTP()  #主函数，写入文档#
    changeSMTP()
    changeFTP()
    changeTelnet()




if __name__ == '__main__':
    write()

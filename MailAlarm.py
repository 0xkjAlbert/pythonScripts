te：   2020/06/08
## Autor：  kjAlbert
## Right：  2020kjAlbert
# 语音朗读模块
import pyttsx3
# pop3协议收邮件模块
import poplib
# base64编码解码模块
import base64
import os
# 时间模块
import time
# 多线程模块
import threading
# 导入播放音乐模块
from pygame import mixer
# 导入解码邮件信头模块
from email.header import decode_header
# 解码模块
from email.parser import Parser

# 全局变量，持续报警开关
flag = 0

# 持续报警函数
def alertAlways(saySomething = '大量警告', sayTime = 3):
    print(saySomething)
    global flag
    while True:
        sayEngine.say(saySomething)
        try:
            # 播放警铃音频
            mixer.music.play()
        except:
            pass
        time.sleep(sayTime)
        if flag == 0:
            break

# 收邮件函数
def receiveMail():
    global flag
    # 提供邮箱用户名密码服务器域名，登录服务器
    email = "xxx"
    password = "xxx"
    pop3_server = "xxx"
    emailServer = poplib.POP3_SSL(pop3_server)
    emailServer.user(email)
    emailServer.pass_(password)

    # 取得邮件列表，取得当前邮件数值
    resp, mails, octets = emailServer.list()
    mailCount = len(mails)# - 11
    emailServer.quit()
    LastTime = float(time.time())

    while True:
        # 检测网络问题,注意，这里的系统命令成功时，返回值为0
        if os.system('ping baidu.com -n 2 -w 1 > $null'):
            if os.system('ping 114.114.114.114 -n 2 -w 1 > $null'):
                if os.system('ping 路由器地址 -n 2 -w 1 > $null'):
                    flag = 1
                    threading.Thread(target = alertAlways, args = ['到路由器的网络不通，请检查网络',5,]).start()
                    while True:
                        inputSomething = input('输入pass停止报警：')
                        if inputSomething == 'pass':
                            flag = 0
                            break
                    continue
                else:
                    flag = 1
                    threading.Thread(target = alertAlways, args = ['外网不通，检查外网',4,]).start()
                    while True:
                        inputSomething = input('输入pass停止报警：')
                        if inputSomething == 'pass':
                            flag = 0
                            break
                    continue
            else:
                sayEngine.say('DNS解析可能有问提')
                print('DNS解析可能有问提')
        # 登录邮件服务器收取邮件
        try:
            emailServer = poplib.POP3_SSL(pop3_server)
            emailServer.user(email)
            emailServer.pass_(password)
            resp, mails, octets = emailServer.list()
        except:
            print('登录错误，等待一秒重新登录')
            time.sleep(1)
            continue
        print('收取邮件 时间：{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        if len(mails) > mailCount:
            apartTime = float(time.time()) - LastTime
            mailCountIn20s = len(mails)-mailCount
            #大量邮件报警阈值
            if mailCountIn20s > 5:
                print('警告，大量邮件请检查')
                sayEngine.say('警告，大量邮件请检查')
                sayEngine.say('{}秒钟内，收到新邮件{}封'.format(int(apartTime), mailCountIn20s))
                time.sleep(2)
                print('{}秒钟内，收到新邮件{}封'.format(int(apartTime), mailCountIn20s))
                flag = 1
                threading.Thread(target = alertAlways).start()
                while True:
                    inputSomething = input('输入pass停止报警：')
                    if inputSomething == 'pass':
                        flag = 0
                        break
            else:
                sayEngine.say('{}秒钟内，收到新邮件{}封'.format(int(apartTime), mailCountIn20s))
                print('{}秒钟内，收到新邮件{}封'.format(int(apartTime), mailCountIn20s))
                LastTime = float(time.time())
                for i in range(mailCount + 1, len(mails) + 1):
                    resp, lines, octets = emailServer.retr(i)
                    msg_content = b'\r\n'.join(lines).decode('utf-8')
                    msg = Parser().parsestr(msg_content)
                    msgDate = msg.get('Date')
                    msgSubject = msg.get('Subject') 
                    try:
                        msgs = decode_header(msgSubject)[0][0].decode('utf-8')
                    except:
                        print('有一封新邮件，解码错误无法朗读')
                        sayEngine.say('有一封新邮件，解码错误无法朗读')
                    else:
                        print(msgDate)
                        print(msgs)
                        if 'Prometheus' in msgs:
                            if 'url' in msgs and 'Read timed out' in msgs:
                                sayEngine.say('Prometheus')
                                if 'http://' in msgs:
                                    sayMsgs = msgs.split('xxx')[1].split('xxx')[0]
                                    #print(msgs.split('xxx')[1])
                                    #print(type(msgs.split('xxx')[1] ))
                                    sayEngine.say('xxx')
                                    sayEngine.say(sayMsgs)
                                elif 'xxx' in msgs:
                                    sayMsgs = msgs.split('xxx')[1].split('xxx')[0]
                                    sayEngine.say('xxx')
                                    sayEngine.say(sayMsgs)
                                else:
                                    sayEngine.say('xxx')
                                    sayEngine.say(msgs)
                            elif 'xxx' in msgs:
                                sayEngine.say('xxx')
                            elif 'xxx' in msgs:
                                sayEngine.say('xxx')
                            elif 'xxx' in msgs:
                                sayEngine.say('xxx')
                            else:
                                sayEngine.say('xxx')
                                sayEngine.say(msgs)
                        elif 'xxx' in msgs:
                            sayEngine.say('xxx')
                        elif 'xxx' in msgs:
                            sayEngine.say('xxx')
                        else:
                            sayEngine.say("xxx")
                            sayEngine.say(msgs)
                        print('---------------------------------')
            mailCount = len(mails)

        emailServer.quit()
        # 由于加了网络ping检测，所以为了保证20秒收一次邮件这里缩短三秒
        time.sleep(17)

if __name__ == '__main__':
    # 初始化mixer播放器
    mixer.init()
    # 加载报警音频文件
    try:
        mixer.music.load('alert.mp3')
    except:
        print('无法加载音频alert.mp3')
    # 初始化朗读模块
    sayEngine = pyttsx3.init()
    # 开启收邮件并且分类报警
    threading.Thread(target = receiveMail).start()
    # 打开朗读播放
    sayEngine.startLoop()


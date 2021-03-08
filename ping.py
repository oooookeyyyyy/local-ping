from socket import AF_INET, SOCK_STREAM, gethostbyname, gethostname, socket
from threading import Thread
from subprocess import check_output
from time import sleep

def ping(n) :
    ip = sub+str(n)
    if ip == selfip :
        out = str(check_output('getmac'))
        out = out.replace('\\n' , ' ')
        out = out.split()
        for i in range(len(out)) :
            if 'Device' in out[i] :
                mac = out[i-1].replace('-' , ':')
        print(ip + ' >> ' + mac + ' (this device)')
    else :
        s = socket(AF_INET , SOCK_STREAM)
        s.settimeout(4)
        r = s.connect_ex((ip,1))
        if r == 10061 :
            out = str(check_output('arp -a '+ip)).split()
            for i in range(len(out)) :
                if out[i] == ip :
                    mac = out[i+1].replace('-' , ':')
                    break
            print(ip + ' >> ' + mac)
        s.close()

selfip = gethostbyname(gethostname())
dot = selfip.rfind('.')
sub = selfip[:dot+1]
for n in range(1 , 255) :
    Thread(target=ping , args=(n,)).start()
    sleep(0.01)
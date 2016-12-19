import os

# usage 'os.system("python "+os.environ['HOME']+"/DavisCamrynLibrary/Help.py")'
# rewrite format function
def format(left,right,mode): # left side, right side, width (normal, wide, custom int)
    #maxWidth = int(os.popen('stty size', 'r').read().split()[1])#only works in a REAL terminal.
    maxWidth = 80
    basic_width = 78
    if(isinstance(mode,str)==False):
        basic_width = int(mode)
    if(mode=="normal"):
        basic_width = basic_width
    elif(mode=="wide"):
        basic_width = maxWidth
    elif(mode=="center"):# format("Hello World",".","center") >> .......Hello World.......
        space = int((maxWidth-(len(str(left))))/2)
        print(str(right)*space+left+str(right)*space)
    if(mode!="center"):
        space = basic_width-(len(str(left))+len(str(right)))
        print(str(left)+(space*"_")+str(right))
def typeOut(string,delay): #delay is in seconds
    if(delay>5):
        delay = delay/1000
    import sys,os,time
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)

def getHost():
    import socket
    login,host,ip = "","",""
    try:
        login = str(os.getlogin())
    except ValueError:
        login = "-N/A-"
    try:
        host = str(socket.gethostname())
    except ValueError:
        host = "-N/A-"
    try:
        ip = str(socket.gethostbyname(socket.gethostname()))
    except socket.gaierror:
        ip = "-N/A-"
    return login,host,ip

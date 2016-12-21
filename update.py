import os,socket
HOME = os.environ['HOME']
REPO = HOME+"/DavisCamrynLibrary/"
Github = "https://raw.githubusercontent.com/CamrynD/LibraryModules/master/"
urls = {
    "Library":[(Github+"Library.py"),REPO+"Library.py"],
    "Help":["None","None"],
    "ReadMe":[(Github+"README.md"),REPO+"ReadMe.txt"],
    "Changelog":["None","None"],
}
def is_connected():
    try:
        socket.gethostbyname("www.google.com")
        # s = socket.create_connection((host, 80), 2)# this does nothing asfar as i know.
        return True
    except:
        return False
def updateLib():
    try:
        # For Python 3.0 and later
        from urllib.request import urlopen as urlLibrary
    except ImportError:
        # Fall back to Python 2's urllib2
        from urllib2 import urlopen as urlLibrary
    def getFileAndWrite(urlToFile,pathToFileAndName):
        if((urlToFile=="None")or(urlToFile=="")):
            return "[404] url not found"
        data = (urlLibrary(urlToFile).read()).decode('utf-8')
        lib = open(pathToFileAndName, "w")
        lib.write(str(data))
        lib.close()

    for libName in urls.keys():
        if(is_connected()==True):
            getFileAndWrite(urls[libName][0],urls[libName][1])
        else:
            print("Offline: Unable to update/download Library")

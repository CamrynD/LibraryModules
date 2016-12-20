import os,socket
HOME = os.environ['HOME']
def is_connected():
    try:
        socket.gethostbyname("www.google.com")
        # s = socket.create_connection((host, 80), 2)# this does nothing asfar as i know.
        return True
    except:
        pass
        return False

def updateLib():
    try:
        # For Python 3.0 and later
        from urllib.request import urlopen as urlLibrary
    except ImportError:
        # Fall back to Python 2's urllib2
        from urllib2 import urlopen as urlLibrary
    def getFileAndWrite(urlToFile,pathToFileAndName):
        print("V1044")
        data = (urlLibrary(urlToFile).read()).decode('utf-8')
        lib = open(pathToFileAndName, "w")
        lib.write(str(data))
        lib.close()
    def updateLibrary():
        if(is_connected()==True):
            getFileAndWrite("https://raw.githubusercontent.com/CamrynD/LibraryModules/master/Library.py",HOME+"/DavisCamrynLibrary/Library.py")
        else:
            print("Offline: Unable to update Library")
        try:
            import Library
            return 0
        except ImportError:
            return ("Offline: No Internet Connection [ Library not created ]")
    def updateHelp():
        if(is_connected()==True):
            pass
            #getFileAndWrite("https://raw.githubusercontent.com/CamrynD/LibraryModules/master/Help.py",HOME+"/DavisCamrynLibrary/Help.py")
        else:
            print("Offline: Unable to update Library")
        try:
            import Library
            return 0
        except ImportError:
            return ("Offline: No Internet Connection [ Library not created ]")
    def updateReadMe():
        if(is_connected()==True):
            getFileAndWrite("https://raw.githubusercontent.com/CamrynD/LibraryModules/master/README.md",HOME+"/DavisCamrynLibrary/ReadMe.txt")
        else:
            print("Offline: Unable to update Library")
        try:
            import Library
            return 0
        except ImportError:
            return ("Offline: No Internet Connection [ Library not created ]")
    def updateChangelog():
        if(is_connected()==True):
            pass
            #getFileAndWrite("https://raw.githubusercontent.com/CamrynD/LibraryModules/master/Library.py",HOME+"/DavisCamrynLibrary/Library.py")
        else:
            print("Offline: Unable to update Library")
        try:
            import Library
            return 0
        except ImportError:
            return ("Offline: No Internet Connection [ Library not created ]")
    updateLibrary()
    updateHelp()
    updateReadMe()
    updateChangelog()

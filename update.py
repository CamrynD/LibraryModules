import os,socket
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
    if(is_connected()==True):
        data = (urlLibrary("https://raw.githubusercontent.com/CamrynD/LibraryModules/master/Library.py")).read()
        text = data.decode('utf-8')
        # i need some space #
        lib = open("Library.py", "w") # write contents of Github to file
        lib.write(str(text))
        lib.close()
    else:
        print("Offline: Unable to update Library")
    try:
        import Library
        return 0
    except ImportError:
        return ("Offline: No Internet Connection [ Library not created ]")

import urllib3
import re
from colorama import Fore

# Class urlAutomationMachine
# Defines a urlAutomationMachine object which initiates the request in order to determine the status
# code of the url. If a file is passed, a regex will be processed on all lines in the file in order
# to pull out the urls and for each url, a network request attempt will occur.

class urlAutomationMachine:

    def __init__(self, input):
        self.input = input
        self.listOfUrls = []
        self.http = urllib3.PoolManager()


    def processUrl(self):
        self.makeRequest(self.input)

    def processFile(self):
        fileToCheck = open(self.input, 'r')
        self.listOfUrls = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', fileToCheck.read())

        for line in self.listOfUrls:
            line = line.strip()
            self.makeRequest(line)

    
    def makeRequest(self, url):
        try:
            r = self.http.request('HEAD', url)
            if (r.status == 200):
                print(Fore.GREEN + f"[SUCCESS]: {url} passes automation. This url is working properly!" )
            elif (r.status == 400 or r.status == 404):
                print(Fore.RED + f"[FAILURE]: {url} fails automation. This url is broken unfortunately!")
            else:
                print(Fore.WHITE + f"[UNKNOWN] {url} gives off a warning. This url is fishy!") 
        except urllib3.exceptions.MaxRetryError: # At this point, the connection attempt timed out and therfore, the url cannot be reached, so in this case, we skip the url entirely.
           pass       
           
          

    
 
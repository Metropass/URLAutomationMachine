import urllib3
import re
from colorama import Fore, init

# Class urlAutomationMachine
# Defines a urlAutomationMachine object which initiates the request in order to determine the status
# code of the url. If a file is passed, a regex will be processed on all lines in the file in order
# to pull out the urls and for each url, a network request attempt will occur.

class urlAutomationMachine:

    def __init__(self, input, isJson=False, ignore=None):
        self.input = input
        self.listOfUrls = []
        self.isJson = isJson
        self.http = urllib3.PoolManager()
        self.ignore = ignore


    def processUrl(self, ignore_list = None):
        self.makeRequest(self.input)

    def processFile(self,ignore_list):
        fileToCheck = open(self.input, 'r')
        self.listOfUrls = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', fileToCheck.read())

        for line in self.listOfUrls:
            line = line.strip()
            if line not in ignore_list:
                self.makeRequest(line)

    def ignore_urls(self):
        ignore_file = open(self.ignore, 'r')
        ignore_list = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', ignore_file.read())
        return ignore_list


    def makeRequest(self, url):
        init()
        try:
            r = self.http.request('HEAD', url)
            self.printOutput(r, url)
        except urllib3.exceptions.MaxRetryError: # At this point, the connection attempt timed out and therfore, the url cannot be reached, so in this case, we skip the url entirely.
           pass


    def printOutput(self, r, url):
        if self.isJson:
            jsonURL = {"url": url, "status_code": r.status}
            if (r.status == 200):
                print(Fore.GREEN + f"[SUCCESS]: {jsonURL} passes automation. This url is working properly!" )
            elif (r.status == 400 or r.status == 404):
                print(Fore.RED + f"[FAILURE]: {jsonURL} fails automation. This url is broken unfortunately!")
            else:
                print(Fore.WHITE + f"[UNKNOWN] {jsonURL} gives off a warning. This url is fishy!")
        else:
            if (r.status == 200):
                print(Fore.GREEN + f"[SUCCESS]: {url} passes automation. This url is working properly!" )
            elif (r.status == 400 or r.status == 404):
                print(Fore.RED + f"[FAILURE]: {url} fails automation. This url is broken unfortunately!")
            else:
                print(Fore.WHITE + f"[UNKNOWN] {url} gives off a warning. This url is fishy!")

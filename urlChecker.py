import argparse
import re
from colorama import Fore
import urllib3
import sys

# Main function parses each line looking for urls to check and make requests
# to check whether the url is broken or not
# Param: inputFile
# Return: Void


def main(fileInput):
    try:
        fileToCheck = open(fileInput, 'r')
        linesInFile = fileToCheck.readlines()
        http = urllib3.PoolManager()
        for line in linesInFile:
            line = line.strip()
            urlLines = re.match(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', line)
            r = http.request('GET', line)
            if (r.status == 200):
                print(Fore.GREEN + f"{urlLines} passes automation. This url is working properly!" )
            elif (r.status == 403):
                print(Fore.BLACK + f"{urlLines} gives off a warning. This url is fishy!")
            else:
                print(Fore.RED + f"{urlLines} fails automation. This url is broken unfortunately!")
    except OSError:
        print("Cannot Open The File! Make sure it's readable.")
    except:
        print("Unexpected Error: ", sys.exc_info()[0])
if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Checks the file input for any broken HTML urls")
    parse.add_argument('-f', help="The input file to check")
    parse.add_argument('-v', action="store_true", help="Displays current version of program")
    args = parse.parse_args()
    if (args.v):
        print("UrlAtuomationMachine ver 1.0")
    elif (args.f):
        main(args.f)
    else:
        print("This program has two arguments, one for inputting the file, the second one displays the current version of the program")
        print("Usage: urlChecker [-f] inputFile: The input file to be processed")
        print("Usage: urlChecker [-v]: Displays current version of the program")

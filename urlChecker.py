import threading
import sys
import argparse
from urlClass import urlAutomationMachine

# checkURL function parses a url and make a request to check whether the url is broken or not.
# Displays output based on -j argument
# Params: inputFile, isJson
# Return: void


def checkURL(fileInput, isJson=False):
  if isJson:
    input = urlAutomationMachine(fileInput, isJson)
    input.processUrl()
  else:
    input = urlAutomationMachine(fileInput)
    input.processUrl()

# checkFile function parses each line looking for urls to check and make requests
# to check whether the url is broken or not. Displays output based on -j argument
# Params: inputFile, isJson
# Return: void


def checkFile(fileInput, isJson=False, ignore=None):
   if isJson:
    input = urlAutomationMachine(fileInput, isJson, ignore)
    input.processFile()
   else:
    input = urlAutomationMachine(fileInput,False,ignore)
    input.processFile()


# Main function parses each line looking for urls to check and make requests
# to check whether the url is broken or not. Calls the appropriate check function
# based on the argument passed
# Param: inputFile
# Return: void


def main(args):
    if (args.f):
      try:
        threading.Thread(target=checkFile(args.f, args.j, args.i)).start()
      except:
        sys.stderr.write("No URLS are good, exiting")
        sys.exit(1)
      sys.exit(0)
    elif (args.u):
      try:
        threading.Thread(target=checkURL(args.u, args.j)).start()
      except:
        sys.stderr.write("No URLS are good, exiting")
        sys.exit(1)
      sys.exit(0)
    elif (args.v):
      print("URLAutomationMachine Ver 2.0")
    else:
      print("This program has two arguments, one for inputting the file, the second one displays the current version of the program")
      print("Usage: urlChecker [-f] inputFile: The input file to be processed")
      print("Usage: urlChecker [-v]: Displays current version of the program")
      print("Usage: urlChecker [-u] inputUrl: Checks URL to see if it works or not")
      print("Usage: urlChecker [-j]: Displays result in JSON format")
      print("Usage: urlChecker [-i]: Ignores the URL that's passed as an argument")


if __name__ == "__main__":

   parse = argparse.ArgumentParser(description="Checks the file input for any broken HTML urls")
   parse.add_argument('-f', help="The input file to check")
   parse.add_argument('-v', action="store_true", help="Displays current version of program")
   parse.add_argument('-u', help="The URL to check")
   parse.add_argument('-j', action="store_true", help="Displays output in JSON format")
   parse.add_argument('-i', help="Ignores any url that matches the argument")
   args = parse.parse_args()

   main(args)

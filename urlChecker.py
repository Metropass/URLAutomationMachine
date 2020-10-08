import threading
import sys
import argparse
from urlClass import urlAutomationMachine

# Main function parses each line looking for urls to check and make requests
# to check whether the url is broken or not. Calls the appropriate check function
# based on the argument passed
# Param: inputFile
# Return: void


def checkURL(fileInput, isJson):
  if isJson:
    input = urlAutomationMachine(fileInput, isJson)
    input.processUrl()
  else:
    input = urlAutomationMachine(fileInput)
    input.processUrl()
    
    
def checkFile(fileInput, isJson):
   if isJson:
    input = urlAutomationMachine(fileInput, isJson)
    input.processFile()
   else:
    input = urlAutomationMachine(fileInput)
    input.processFile()


def main(args):
    if (args.f):
      try:
        threading.Thread(target=checkFile(args.f)).start()
      except:
        sys.exit(1)
      sys.exit(0)
    elif (args.u):
      try:
        threading.Thread(target=checkURL(args.u)).start()
      except:
        sys.exit(1)
      sys.exit(0)
    elif (args.v):
      print("URLAutomationMachine Ver 1.1")
    else:
      print("This program has two arguments, one for inputting the file, the second one displays the current version of the program")
      print("Usage: urlChecker [-f] inputFile: The input file to be processed")   
      print("Usage: urlChecker [-v]: Displays current version of the program")
      print("Usage: urlChecker [-u] inputUrl: Checks URL to see if it works or not")

   
if __name__ == "__main__":

   parse = argparse.ArgumentParser(description="Checks the file input for any broken HTML urls")
   parse.add_argument('-f', help="The input file to check")
   parse.add_argument('-v', action="store_true", help="Displays current version of program")
   parse.add_argument('-u', help="The URL to check")
   parse.add_argument('-j', '--json', action="store_true", help="Displays output in JSON format")

   args = parse.parse_args()

   main(args)

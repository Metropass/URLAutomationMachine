import argparse
import threading
from urlClass import urlAutomationMachine

# Main function parses each line looking for urls to check and make requests
# to check whether the url is broken or not. Calls the appropriate check function
# based on the argument passed
# Param: inputFile
# Return: void


def checkURL(fileInput):
    input = urlAutomationMachine(fileInput)
    input.processUrl()


def checkFile(fileInput):
   input = urlAutomationMachine(fileInput)
   input.processFile()


def main(args):
    if (args.f):
      threading.Thread(target=checkFile(args.f)).start()
    elif (args.u):
      threading.Thread(target=checkURL(args.u)).start()
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

   args = parse.parse_args()

   main(args)

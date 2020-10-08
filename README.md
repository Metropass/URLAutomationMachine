# URLAutomationMachine

The machine we all need but the one we most likely do not deserve. The url checking program we all desire


# Usage

Usage can be found by typing ```urlChecker --help```

Used by typing in:

```urlChecker -f inputFile```

Check the version of the program by typing in:

```urlChecker -v```

To check a single url, type the following:

```urlChecker -u NAMEOFURL```

To see your output in a JSON format, type the following:

```urlChecker -j ```


To run the program as written above, enter the following into your terminal

```pip3 install --editable .```

This will install all necessary libraries as well as setup the terminal to run the program as described above

# Features

- Uses regex to parse each line for a url
- Processes each request and checks status code for successful attempt
- Any url with a status code around ```200``` will pass automation
- Urls with a status code of ```404``` or ```400``` will fail automation
- Urls with a status code that is unknown ```403``` will fail automation but will be displayed in grey colouring
- Flags are used to pass in filenames and describe the version of the file.
- ```-j``` option allows for program to display the output in a JSON format
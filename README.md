mathsfunctions
==============

Mathsfunctions is a library of python scripts for solving high level classroom maths problems. 

The scripts all follow a regimented inheritance of the Mathsfunction class. This allows them to run easily standalone, or integrate easily into other python scripts.

Call a script with it's inputs from the command line, or import the script, create in instance of it's class in your own python script, then call instance.solve(*inputs) to get the raw answer.

Passing the -format's flag from the command line allows you to specify the format of the given answer.

Current scripts:
* solvequadratic.py - solves quadratic equations. Inputs: a, b, c. Formats: listring.
* primefactors.py - gives all prime factors of a number. Inputs: a. Formats: listring, powerstring.
* lcm.py - gives the lowest common multiple of two numbers. Inputs: a, b. Formats: string.
* hcf.py - gives the highest common factor of two numbers. Inputs: a, b. Formats: string.

Help for all scripts can be called using --help.

mf.py is the core library. It parses command line arguaments, returning them as integers, and runs the help commands when called for.

Please feel free to contribute!

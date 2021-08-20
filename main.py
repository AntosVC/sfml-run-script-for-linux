'''
This script is fast compiling and running sfml games on linux.
Program takes only one argument which is name of file with surce code written in C++.
before run paste this command in terminal:

export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0

'''

import os, sys

if len(sys.argv) <= 1:
  sys.stderr.write("Please specife file with soruce code\n")
  sys.stderr.flush()
else:
  my_file = sys.argv[1]
  os.system("g++ -c " + my_file)
  os.system("g++ {}.o -o sfml-app -lsfml-graphics -lsfml-window -lsfml-system -lsfml-audio -lsfml-network".format(my_file[:4]))
  os.system("./sfml-app")

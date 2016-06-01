#bootstrap for project remoteCam on RPi3
import sys,os
if __import__("sys").version_info[:2]<(2,7,0):
  sys.stderr.write("You need python 2.7 or later to run this script\n")
  exit(1)
 print("Ready.")
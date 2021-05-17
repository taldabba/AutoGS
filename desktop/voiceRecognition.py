import time
from subprocess import *
import threading
from threading import Thread
from queue import Queue
import serial
import logging
import sys
import sched
import random
import collections	


def consoleThreadFunc():
	while True:
		userInput = input("Enter y to let me listen to your voice: ")

consoleThreadFunc()
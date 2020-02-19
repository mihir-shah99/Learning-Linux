# -*- coding: utf-8 -*-
# @Author: Mihir Shah
import os
from colors.colors import *
from shell import TrainingWheelsShellClass

class TrainingWheelsWrapperClass():

	def __init__( self ):
		
		os.system("clear")
		print 	B("_" * 79 + "\n\n" ) + c(\
" ... this tool was developed by SHAHENSHAH. If you're curious about it, ask!\n"+
			  	B("_" * 79 + "\n\n"))


	def run( self ):

		TraingWheelsShell = TrainingWheelsShellClass()
		TraingWheelsShell.run()

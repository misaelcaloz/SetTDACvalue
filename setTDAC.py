						#
						#
						#
		#####################################################################################################
		#																									#
		# 	Script to change the TDAC value of a specific pixel and give a modified text file				#
		#																									#
		#####################################################################################################
						#
						#
						#
						#
# --------packages 

import sys
sys.path.append("/usr/local/lib/root")
import ROOT
from ROOT import gROOT, TCanvas, TF1, TGraph, TLegend, TMath, TMultiGraph, TFile, TH2F, TH1F, TDirectory,TH2D, TH1D, TLatex, gPad, TH2I
from array import array
import numpy
import math
import pylab

#------------ input data

TDACfile_input = sys.argv[1]
TDACfile_output=sys.argv[2]
data=open(TDACfile_input)



#------------ create 1D and 2D histograms and fitting function

#TDAC2D = TH2I("TDAC2D", "TDAC2D",24,0,24,60,0,60)
#TDAC1D=TH1F("TDAC1D", "TDAC distribution;TDAC",16,0,16)


#------------ create canvas

#c1 = TCanvas("Plot")
#c1.SetGrid()
#c1.SetFillColor(0)
#c1.cd()


#---------- TDAC FILE ANALYSIS


row=int(raw_input('Raw ? : '))

print row

col=int(raw_input('Col ? : '))

print col

newTDAC=int(raw_input('new TDAC ? : '))

print newTDAC








lineNum_TDAC=0
TDAC_list=[]

for line in data:
	lineNum_TDAC+=1
	TDAC_value=line.split()
	TDAC_list.append(int(TDAC_value[0]))
	#	if lineNum_TDAC > 288 and lineNum_TDAC < 1153:
	#		TDAC1D.Fill(float(TDAC_value[0]))
	#else:
#	a=1.#print 'rad hard pixel'

print 'TDAC list', TDAC_list


cnt=0
for i in range(60) :
	#print '-'
	for j in range(24):
		#print'+'
		#TDAC2D.Fill(i,j,TDAC_list[cnt])
		if j==row and i==col:
			TDAC_list[cnt]=newTDAC
		#print 'cnt', cnt
		print 'cnt', cnt
		cnt+=1

file = open(TDACfile_output, "r+")


cnt2=0
for i in TDAC_list:
	if cnt2 <1439:
		print cnt2+1
		print TDAC_list[cnt2]
		file.write(""+str(TDAC_list[cnt2])+"\n")
		#file.write("\n")
		cnt2+=1
	else:										#necessary to avoid the last blank line in the output file
		file.write(str(TDAC_list[cnt2]))		#TODO: check if this is necessary for the software

		cnt2+=1

file.close()


#TDAC2D.Draw("colz")

print range(60)

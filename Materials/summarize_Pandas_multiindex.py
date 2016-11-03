#!/usr/bin/env python
# demonstration of data exploration code for Comp Bio course, Fall 2016
# James A. Foster
# WARNING: not completely error checked

'''
Usage:
   summarize_Pandas.py inputFile

where inputfile is a tab delimited summary of a Hiseq dataset, as in Homework 5, with headers

Questions to answer:

- how many times does THIS gene appear in THAT country?
- what is average GC content for THIS gene in THAT country?
'''      

import sys
import pandas as pd
from pandas import Series, DataFrame

# read data from input file
try:
   allDataFrame = pd.read_table( sys.argv[1], 
      comment='#', 
      usecols=[ 'Gene','Country','gcContent' ] )
except OSError as err:
   print( "**ERROR** Cannot open %s, error: %s" % ( sys.argv[1], err ) )
except:
   print( "**ERROR** unknown error with %s: %s" % ( sys.argv[1], sys.exc_info()[0] ) )

allDataFrame['GeneFamily'] = [x[:x.find('_')] for x in allDataFrame['Gene'] ]
allDataFrame['highGC'] = allDataFrame.gcContent > 0.4
allDataFrame['lowGC']  = allDataFrame.gcContent < 0.4

allDataFrame.set_index(['Country','GeneFamily','Gene'], inplace=True)

allDataFrame.std()
allDataFrame.mean()

allDataFrame.mean(level='GeneFamily')
allDataFrame.count(level='Country')

allDataFrame.mean(level='Country')
summaryByCountryGene = DataFrame()
summaryByCountryGene['mean'] = allDataFrame.mean(level=['Country', 'GeneFamily'])['gcContent']
summaryByCountryGene['std'] = allDataFrame.std(level=['Country', 'GeneFamily'])['gcContent']

sBCGu = summaryByCountryGene.unstack()

sBCGu.cov().ix['mean']
sBCGu.corr().ix['mean']




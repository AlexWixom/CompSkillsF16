# Homework 9
In this assignment you will make plots from the OTU relative abundances from previous assignments. 

## Things to Do by midnight, **12/1**, or Sooner ##
Write a program called *plots.py* that uses matplotlib to create some plots/charts to analyze microbiome data from previous assignments (do what you need to to get the data into a usable format). For each of these, either turn in all work in a jupyter notebook or create separate png files named *MicrobiomeByWoman.png* and *DiversityByWoman.png* (respectively for each step 1--2 below, and *DiversityAllData.png* for step 3.)

1. Make horizontal stacked barcharts of each woman's microbiome that looks like this (pay attention to titles and axis lables). Data are from HW7, *summaryByWoman.txt*, and I have put a copy in the *Homework/Resources* directory. Save figure to *MicrobiomeByWoman.png* (note, that is a png file). 

![Relative abundance by woman](MicrobiomeByWoman.png)

3. Plot average Shannon and Simpson diversity indexes in blue and red, respectively,  by woman. Add dotted horizontal line in the same color for the mean average index. Data are in *Homework/Resources/summaryByWoman.txt*. Save figure to *DiversityByWoman.png* (note, that is a png file). 

![Diversity index averages](DiversityByWoman.png)

3. (extra credit) Plot histogram of Shannon diversity scores for all the data. Data are in  *Resources/summaryByDay.txt*. Save figure to *DiversityAllData.png* (note, that is a png file).

![Diversity values for all data](DiversityAllData.png)
	
## Turn in homework
1. Commit your work
2. Update your local master
3. Sync with the remote master (that is how we will turn in homework!).
## Hints and Suggestions ##

* If you increase the xlim setting, you will get more room on the right of your bars in (1)
* Font sizes are:

Font size | item
--------------------	| ---------
title	| xx-large
x, y lables 	| large
legend 	| medium
color (in 3)	| 'darkgray'

* It may help to get the patient ids onto axis labels with somthing like this
>patientIDs = otuData.index

	and then using that to *set_xticklabels* and *set_xticks*
* There is known bug in matplotlib with the *fig.tight_layout()* command on macs. Instead, use *fig.set_tight_layout(True)*. This works when sending a plot a file.
* If you can't see the figures in this document, view the document on github.com. 

## Grading
Grades will be determined as follows:

Grade | Criteria 
-------- | --------------
0          | Nothing turned in
1          | *plots.py*  turned in but doesn't run, or is incorrect, or figures turned in but they don't meet the specifications
2          | *plots.py* accurate and figures correctly formatted
3          | Code uses good style. Or does extra credit question
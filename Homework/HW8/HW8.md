# Homework 8:
In this assignment you will continue human microbiome analysis by merging metadata and microbiome profile datasets and looking for correlations. There will be one or two assignments due after break that will plot data from these studies.

The metadata, in *Homework/Resources/vaginal_metadata.txt*, summarizes diary entries for each of the 25 women in this study for the first four days of weeks 1 and 10 (the full dataset is available online). The fields in this dataset are:


Field 	| meaning
------- 	| ---------
ID	| a unique identifier for this entry 
DIA_DAY	| day of the week the entry is made (1--4)
DIA_WEEK	| week of the study (either 1 or 10)
DAYOFWK	| Monday through Friday, coded numerically
RDATE	| date of the entry
Woman	| identifier for this woman
Score	| Nugent score, diagnosis of *bacterial vaginosis*. 7--10 indicates BV, lower scores are lack of BV with decreasing confidence
VAG_INT	|sexual intercourse occurred
COND_USE	|condom used
SPER_USE	|spermicide used
PARTNER	|number of sexual partners
MENSTRUA	|menstruation, 1: light, 2: heavy
TAMPON	|tampon used
MEDS	|medication used
MEDS_SP	|type(s) of medication used



## Readings
1. Read text chapter 8, pages 217--236
2. Read text chapter 7, pages 175--192
## Coding: due by 11/29, midnight ##
**Note that the due date is the *Tuesday* after break**. But don't put this off. HW9 is due the **Thursday** after break. 

Write a program called *microbiome_analysis.py* that does the following:

1. Read *summaryByDay.txt* from homework 7 into a pandas dataframe, index by woman, week, and day
2. Read *Homework/Resources/vaginal_metadata.txt* (a tab-delimited file) into another pandas dataframe, index by woman, week, and day
3. Merge the first dataframe from above into the second. There are two ways to do this, either by "ID" or by the indexes. Indexes are a better way.

	Beware, there may be some rows that don't match up. This is real data, and that sort of thing happens.

4. Compute the correlations of the Shannon and Simpson diversity indexes with each other. If they are highly correlated, then we can use either one as a proxy for microbial community diversity. Are they correlated? Answer in a markdown file called *Analysis.md*.

5. Compute the correlations of the metadata items ("Score" through "Meds") with the Shannon diversity index. 

	a. Store these correlations in a file named *Correlations.txt* (it is probably easiest to print them to stdout and then redirect the output to this file, but feel free to do otherwise).

	b. Are any of them highly correlated? How do you interpret that, biologically? Put your answers in *Analysis.md*.

6. Compute the correlations of the OTU relative abundances with **Score** and **Meds**. 

	a. Add these correlations to *Correlations.txt*

	b. Are any of them highly correlated? How do you interpret that, biologically? Put your answers in *Analysis.md*

## Turn in homework
1. Commit your work
2. Update your local master
3. Sync with the remote master (that is how we will turn in homework!).

## Grading
Grades will be determined as follows:

Grade | Criteria 
-------- | --------------
0          | Nothing turned in
1          | *microbiome_analysis.py*  turned in but doesn't run, or is incorrect
2          |   Accuracy of *Correlations.txt*, reasonable answers in *Analysis.md*
3          |  Code uses good style, or analysis is really, really good (but this isn't a research paper, so don't go overboard). In particular, if you examine correlations conditional on the appropriate events (for example, number of sexual partners or spermicide use conditional on having intercourse), or recoding Nugent scores to BV positive or negative.
Why I made this?
================
I use [iBank4](http://www.iggsoftware.com/ibank/) to manage my finances, I live in Japan and my main credit card is a [Mitsui Sumitomo Bank](https://www.smbc-card.com/) (a.k.a. SMBC) managed VISA.

SMBC stopped providing nicely packaged QIF files some time ago and now only offers a CSV file for downloading your card statements. Unfortunately, that CSV is Shift-JIS encoded (unicode is not that widely used in Japan) which iBank does not understand and the date format `YYYY/MM/DD`, although pretty standard, cannot be parsed by iBank.

After a couple months of struggling with character encoding conversions in Textedit and date format modifications in Numbers, I decided to write a python script to do it for me.

What will it do?
================
1. Change the file's character encoding from Shift-JIS to UTF-8
2. Reformat the dates from `YYYY/MM/DD` to `YYYY-MM-DD` which iBank detects automagically

How to run it?
==============
    smbc-convert infile [outfile]

+ *infile* is your CSV file from the SMBC site
+ *outfile* is the cleaned up file, if omitted the output got to stdout
# ADBS
Convert dates from [BS](https://www.wikiwand.com/en/Bikram_Sambat) to [AD](https://www.wikiwand.com/en/Gregorian_calendar) and vice-versa.

# Introduction
The ubiquitous calendar with the date '1st Jan 2022' is the [Gregorian](https://www.wikiwand.com/en/Gregorian_calendar) calendar. Being used in most parts of the world, it is the only supported calendar in most softwares. But there exists other calendars, too.

[Bikram Sambat](https://www.wikiwand.com/en/Bikram_Samvat) is **the official** calendar in [Nepal](https://www.wikiwand.com/en/Nepal). Currently it is 'Year 2079' in Bikram Sambat whereas it is 'Year 2022' in the Gregorian. Bikram Sambat is ~57 years ahead of Gregorian. Dates are commonly written as **2022-01-01 AD** in the Gregorian, and **2079-01-01 BS** in the Bikram Sambat. So, they are commonly reffered as *AD date* and *BS date* here in Nepal, and thus the name of this project.

# Implementation
The Gregorian calendar is simple. Each month has the same number of days except for February, in leap years. Bikram Sambat calendar doesn't have fixed number of days in months. A database if provided for upto few decades in the future.

Prerequisite: A known day in both date systems (1918-4-13 AD = 1975-1-1 BS). Let's call them base dates.

## AD to BS
- The number of days (d) between the entered AD date and the AD base date is calculated.
- d is added to the BS base date by looping/advancing through the BS database.
- The required BS date is obtained.
![](ad2bs.gif)

- 1 is subtracted to make the base date 'day 1' instead of 'day 0'.

## BS to AD
- The number of days (d) between the entered BS date and the BS base date is calculated.
- d is added to the AD base date 

# More info on Bikram Sambat calendar:
- Both calendars have 12 months.
- The BS months are: Baisakh to Chaitra.
- Baisakh 1st falls on April 13th or 14th.
- The fiscal year however starts from the 4th month. For example, currently the fiscal year is 2079/2080, which started on 2079-04-01 *(2022 Jul 17)*, and will end on 2080-03-31 *(2022-Jul 16)*.

## For software developers
The conversion is just a simple arithmetic. Please provide BS calendar in your programs. You need not code any fancy date picker or calendar widget, just allow the user to choose this calendar system. And, an entry widget is enough.

# Installation
Download executable from the [Releases page.](https://github.com/pragyanone/adbs/releases)

Or, clone the repo.

# Please upvote my feedbacks 
- Microsoft Windows: https://aka.ms/AAhq6wb
- GnuCash: https://bugs.gnucash.org/show_bug.cgi?id=798602
- Debitum: https://github.com/Marmo/debitum/issues/116
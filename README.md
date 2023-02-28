Executive Summary


For the first set of information – the financial records of my company – I found an overall profit margin of $22.5 million dollars over the 86 month span of the dataset. Meanwhile, the clear winner of the poll was Diana DeGette, who amassed 73.8% of the almost 370k votes cast. She outpaced her closest competitor by over 185,000 votes.


Introduction


The data provided for the PyBank code is a series of profit/loss margins over the course of 86 months. Each month profits or losses over the last month were calculated and input into the sheet. The purpose of this analysis is to determine the average change, which month had the greatest increase or decrease in profits respectively, and the net profit over the entire data set. 

For the PyPoll data, we were provided with a dataset comprised of voter ID, county, and the candidate which was voted for. The goal here was to tally all the votes, determine the complete list of candidates who received votes, give a percentage of votes each candidate received, and also determine the given winner of the poll.   

Data Collection and Preparation


PyBank: This data was collected by determining the profit/loss margin for a given month and recording that data. The data was collected as a csv file so I had it passed through the csv reader when creating the code for this assignment.


PyPoll: For this dataset, we were given a file with poll data composed of three columns.  The data was collected as a csv file so I had it passed through the csv reader when creating the code for this assignment.



Data Exploration and Cleaning


Before beginning any tasks, I first made sure to look through the datasets to better understand the information provided. In doing so it made clear the the PyBank information was the profit margin for a given month and each month should be looked at individually. 

Data Analysis


PyBank: For this dataset I created a code that looped through each month and recorded that months profit/loss. From there, the date and amount of the greatest increase and decrease were recorded. Then the current_profit_loss was saved into previous_profit_loss and began recording the next months info. After the loop is completed, I had that information printed out and also exported to a text file with the results of the analysis. Those results showed a total profit of $22,564,198 over 86 months with the strongest month being August of 2016, and the weakest being February 2014. 


PyPoll: For PyPoll, I had a code that looped through the list of votes and tallied votes for candidates. It would increase the tally by one when a candidates name was chosen, and would add a candidate if their name had not been tallied before.  The clear leader of this poll was Diana DeGette who amassed 272,892 votes out of 369,711, while her closest competitor – Charles Casper Stockham – came in with only 85,213 votes. Lastly Raymon Anthony Doane received 11,606 votes. 


Conclusion


The key findings for this analysis are fairly clear to state. The PyBank information showed that over a span of 86 months, my company has had a net profit of $22,564,198. The PyPoll analysis revealed a runaway winner in Diana DeGette, who outpaced her closest in the poll by garnering a whopping 50% more of the vote.

This data provided for both analyses was fairly limited and failed to allow for a more indepth look at the election or my companies financial records. However, the information is sufficient to reach these more high level conclusions. 

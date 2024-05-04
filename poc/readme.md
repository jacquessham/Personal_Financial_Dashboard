# Proof of Concept
The goal of the proof of concept phase is to scratch out how the expected dashboard should look like and observe the details are required to build the dashboard. 

## Data
The proof of concept dashboard will only utilize a limited amount of data - One credit card statement and one checking account statement from Bank of America.
<ul>
	<li>boa_cc_example_raw.csv</li>
	<li>boa_chk_example_raw.csv</li>
	<li>boa_cc_example.csv</li>
	<li>boa_chk_example.csv</li>
</ul>

<i>boa_chk_example_raw.csv</i> and <i>boa_cc_example_raw.csv</i> are the CSV sample with the format downloaded from Bank of America (The data is made up). <i>boa_chk_example.csv</i> and <i>boa_cc_example.csv</i> are the transformed version of <i>boa_chk_example_raw.csv</i> and <i>boa_cc_example_raw.csv</i>. 

### Data Requirement
In the proof of concept stage, it is required to manually add <b>Expense_Category</b> to both credit card and checking account statement. Add <b>Expense_Category</b> the column to both CSV files, as well as the entry of that column. If it is not an expense item, leave it blank. The script will ignore that row in the expense visualizations.

## Dashboards
### POC Version 1
POC Version 1 would display 3 visualizations that shows Personal Network in line chart, Credit Card expense and All expense (Credit Card and Checking accounts) in Donut Chart. Those visualizations will be generated in three objects usinging Plotly.

### POC Version 2
POC Version 2 would put all the visualizations generated in Version 1 into one dynamic 3-tabs dashboard using Dash. The users may choose one of the visualizations by clicking the tab. The interactivity will be introduced the full version.

## Scripts
[POC Version 1](/Version1) folder contains <i>boa_docs.py</i> and <i>poc_dashboard.py</i> that powers the visualizations. <i>poc_dashboard.py</i> will generate 3 visualizations in 3 HTML pages. <i>boa_docs.py</i> is the package built for Bank of America statements, and the full version will have one package for each targeted financial institute.
<br><br>
[POC Version 2](/Version2) folder contains <i>boa_docs.py</i>, <i>vis.py</i> and <i>poc_dashboard.py</i> that powers the visualizations. Although POC Version 2 <i>poc_dashboard.py</i> has the same name as the POC Version 1 counterpart, the script works differently. The POC Version 2 will power a dynamic dashboard using Dash that will display the 3 visualizations in POC Version 1 in a 3-tabs dashboard.


## Result and Gallery
The POC Version 2 works as expected and the full version will be developed based on this version. Here are the captured images:

<img src=Images/dash_networth.png>
<img src=Images/dash_all_expense.png>

<br><br>
Here are the visualizations captured in POC Version 1.
<img src=Images/net_worth_vis.png>
<img src=Images/cc_expense_vis.png>
<img src=Images/all_expense_vis.png>


## Next Step
The next step is to develop the full version, the requirements can be found in the [homepage](..). The full version can be found in the [Dashboard](../Dashboard) folder.


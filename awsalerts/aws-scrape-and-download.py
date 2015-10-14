#!/usr/bin/env python
from mechanize import Browser
from bs4 import BeautifulSoup
import re

mech = Browser()
url = "http://status.aws.amazon.com/"
page = mech.open(url)
html = page.read()

#Pull down all the HTML from AWS's status page
soup = BeautifulSoup(html)
#print soup.prettify()

#Extract out just the North American Region stuff
NA_Div = soup.find(id="NA_block")
#print NA_Div

#Strip off the DIV tags and keep just the table
table = NA_Div.find("table")
#print table

#Get all table rows
#row = table.findAll("tr")
#print row


#In this table, pull out the strings with Service Name and Status
for string in table.stripped_strings:#(re.compile("(N. California)")):
    alerts = (repr(string))
    print alerts


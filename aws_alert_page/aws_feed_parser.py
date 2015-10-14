####
# Based on script at 
# https://everydayscripting.wordpress.com/2008/09/23/parsing-xml-feeds-ridiculously-straight-forward-examples/
#
###
from urllib2 import urlopen
from xml.dom import minidom

import jinja2
import os

feed = urlopen("http://status.aws.amazon.com/rss/ec2-us-west-1.rss")

doc = minidom.parse(feed)

#Get all relevant parts of an alert
alert_date = doc.getElementsByTagName("pubDate") #Get alert date
alert_title = doc.getElementsByTagName("title") #Get alert headline
alert_message = doc.getElementsByTagName("description") #Get alert message

alerts = zip(alert_date, alert_title, alert_message)
for adate_node, aheadline_node, amessage_node in alerts:
    date = adate_node.childNodes[0].nodeValue
    headline = aheadline_node.childNodes[0].nodeValue
    message = amessage_node.childNodes[0].nodeValue
    print "%s %s: %s" % (date, headline, message)

#Now that the alert info has been pulled down, load it into a Jinja template:

#Create loader and tell Jinja to get template file from the current working directory
alert_loader = jinja2.FileSystemLoader(os.getcwd())
#print alert_loader

#Create Jinja environmnent and tell it that its loader is the loader we just made. Also preserve whitespace with trim blocks and lstrip blocks.
jenv = jinja2.Environment(loader=alert_loader, trim_blocks=True, lstrip_blocks=True)
#print jenv

#Tell Jinja which template to use
template = jenv.get_template('alert_page.j2')
#print template

#Render HTML with alert values inserted:
print template.render(alert_title=headline, alert_date=date, alert_message=message)


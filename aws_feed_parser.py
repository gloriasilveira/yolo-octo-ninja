####
# Based on script at 
# https://everydayscripting.wordpress.com/2008/09/23/parsing-xml-feeds-ridiculously-straight-forward-examples/
#
###
from urllib2 import urlopen
from xml.dom import minidom

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
    print "%s %s: %s" % (date, headline, message)#

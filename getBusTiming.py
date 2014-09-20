#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup as BS
import re
import time
def getAgenciesList():
	agenciesList_req = urllib2.Request('''http://services.my511.org/Transit2.0/GetAgencies.aspx?token=aeeb38de-5385-482a-abde-692dfb2769e3''')

	xml_resp = urllib2.urlopen(agenciesList_req)
	soup = BS(xml_resp.read(),'lxml')
	print soup.prettify()

	agencies = soup.find_all('agency')
	for a in agencies:
		print a['name']

def getBusList(busCodes):
	api_url = '''http://services.my511.org/Transit2.0/GetRoutesForAgencies.aspx
		?token=aeeb38de-5385-482a-abde-692dfb2769e3
		&agencyNames=SF-MUNI'''
	req = urllib2.urlopen(''.join(api_url.split()))
	soup = BS(req.read(),'lxml')
	routes = soup.find_all('route')
	for route in routes:
		if route['code'] in busCodes:
			print route.prettify()

def getBusStopsList():
	api_url = '''http://services.my511.org/Transit2.0/GetStopsForRoute.aspx
		?token=aeeb38de-5385-482a-abde-692dfb2769e3
		&routeIDF=SF-MUNI~8X~Inbound'''
	req = urllib2.urlopen(''.join(api_url.split()))
	soup = BS(req.read(),'lxml')
	print soup.prettify()

# getBusList(['8X','8AX'])

def getNextDepartures(stopcode,buscode):
	api_url = '''http://services.my511.org/Transit2.0/
		GetNextDeparturesByStopCode.aspx
		?token=aeeb38de-5385-482a-abde-692dfb2769e3
		&stopcode=%s'''%stopcode

	req = urllib2.urlopen(''.join(api_url.split()))
	soup = BS(req.read(),'lxml')
	# print soup.prettify()
	route = soup.find('route',{'code':buscode})

	l = route.departuretimelist.getText().split()
	
	if l:
		print '-- %s\t%s (mins)'%(buscode,', '.join(l))
	else:
		print '-- %s\tUnavailable'%buscode

	return l
if __name__ == '__main__':
	print 'BUS TIMING... :D\n'
	print time.ctime(time.time())
	
	print 'San Bruno Ave & Thornton Ave'
	getNextDepartures(16367,'8X')
	getNextDepartures(16367,'8AX')
	getNextDepartures(16367,'9')
	getNextDepartures(16367,'90')

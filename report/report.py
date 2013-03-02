#!/usr/bin/env python

import sys
import re
from collections import defaultdict
import time

# stats
hosts = defaultdict(int)
earliestDate = sys.maxint
latestDate = 0

# read in the raw data
entries = sys.stdin.readlines()

for entry in entries:
    
    # parse the entry
    s = entry.split(' ',1)

    (host,path,method) = re.search('([^/]+)(.*):(.*)', s[0]).group(1,2,3)
    attrs = eval(s[1])

    hostParts = host.split('.')
    hostParts.reverse()
    host = '.'.join(hostParts)
    
    date = attrs['arcFileDate']
    
    # record the stats
    hosts[host] += 1

    if (date < earliestDate):
        earliestDate = date

    if (date > latestDate):
        latestDate = date

print 'Crawled between', time.ctime(earliestDate/1000), 'and', time.ctime(latestDate/1000)
print ''

for host in sorted(hosts, key=hosts.get, reverse=True):
    print "{:5d} {:s}".format(hosts[host], host)

print ''

print 'Total URLs: ', len(entries)
print 'Total hostnames: ', len(hosts.keys())




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
    
    # parse each entry
    s = entry.split(' ',1)

    m = re.search('([^/]+)(.*):(.*)', s[0])

    host = m.group(1).split('.')
    host.reverse()
    host = '.'.join(host)
    
    path = m.group(2)
    method = m.group(3)

    attrs = eval(s[1])
    date = attrs['arcFileDate']
    
    #print host, path, method, attrs

    # record the stats for this entry
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




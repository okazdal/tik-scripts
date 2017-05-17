__author__ = 'okazdal'
# whois -h whois.radb.net -- '-i origin AS714' | grep -Eo "([0-9.]+){4}/[0-9]+" | head
# GOOGLE  AS15169
# YOUTUBE AS36040
import re
import subprocess
import shlex

command = shlex.split('whois -h whois.radb.net -- \'-i origin AS714\' | grep -Eo "([0-9.]+){4}/[0-9]+" | head')
# subprocess

file = 'youtube.txt'
address_list_name = 'youtube'

fh = open(file, mode='r')

dest_file = open('google.rsc', mode='w')
lines = fh.readlines()
fh.close()

for line in lines:
    # line = re.sub(r'route:\W+',
    #              '',
    #              line)
    # line = re.sub(r'\W$', '', line)
    # line.rstrip('\n')
    # print line
    chunks = line.split()
    print chunks[0]
#     /ip firewall address-list add address=1.1.1.1 list=testlistesi
    print '/ip firewall address-list add address=' + chunks[0] + ' list=' + address_list_name
    dest_file.write('/ip firewall address-list add address=' + chunks[0] + ' list=' + address_list_name + '\n')

dest_file.close()



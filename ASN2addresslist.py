__author__ = 'okazdal'
# whois -h whois.radb.net -- '-i origin AS15169' | grep -Eo "([0-9.]+){4}/[0-9]+"
# GOOGLE  AS15169
# YOUTUBE AS36040
import subprocess
import shlex

ASN = 'AS15169'

command = shlex.split('''whois -h whois.radb.net -i origin AS36040''')
grep_command = shlex.split('grep -Eo "([0-9.]+){4}/[0-9]+"')

p1 = subprocess.Popen(command, stdout=subprocess.PIPE)
p2 = subprocess.Popen(grep_command, stdin=p1.stdout, stdout=subprocess.PIPE)

address_list_name = ASN

dest_file = open(ASN + '.rsc', mode='w')
lines = p2.stdout.readlines()


for line in lines:
    chunks = line.split()
    # print chunks[0]
    # print '/ip firewall address-list add address=' + chunks[0] + ' list=' + address_list_name
    dest_file.write('/ip firewall address-list add address=' + chunks[0] + ' list=' + address_list_name + '\n')

dest_file.close()



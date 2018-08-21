import re
import socket


#NameAge = '''
#Janice is 22 and Theon is 33
#Gabriel is 44 and Joey is 21
#'''
#



log_file = '/var/log/auth.log'

with open(log_file , 'r') as fil:
    read = fil.read()
    ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', read)
    for ip in ips:
        if socket.inet_aton(ip):
            print ip + " " + socket.gethostbyaddr(nvr)

    fil.close()


#print NameAge

#ages = re.findall(r'\d{1,3}', NameAge)
#names = re.findall(r'[A-Z][a-z]*', NameAge)





 

#dict = {}
#i = 0
#for age in ages:
#    dict[names[i]] = age
#    i = i + 1
#  
#print dict







   
        



    



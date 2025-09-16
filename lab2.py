import re


pattern = r"\d+\.\d+\.\d+\.\d+"
text = ""

with open('auth.log', 'r') as f:
    for line in f: 
        print({line.strip()})

with open('auth.log', 'r') as f:
    for line in f: 
        found_ips= re.findall(pattern, text)
       
ips = []   
for ip in found_ips:
        ips.append(ip)

print[ips]







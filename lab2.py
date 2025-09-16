import re

ips = [] 
pattern = r"\d+\.\d+\.\d+\.\d+"

with open('auth.log', 'r') as f:
    for line in f: 
        print({line.strip()})

with open('auth.log', 'r') as f:
    for line in f: 
        found_ips= re.findall(pattern, line)
        for ip in found_ips:
         ips.append(ip)

unique_ips = set(ips)

print("Unique IPs: ", unique_ips)

with open("unique_ips.txt", "w") as dst:
    for ip in unique_ips:
        dst.write(ip + "\n")







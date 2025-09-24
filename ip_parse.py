READ = "sample_auth_small.log" # Input from logfile
from collections import defaultdict
count = 0
ipcount = 0
ips = []
counts = defaultdict(int)


def ip_parser(line): # Method created and called ip_parser

    if " from " in line: # If from is in line (Because IP is printed after "from")
        parts = line.split() # Split the line into parts
        try:
            anchor = parts.index("from") # Anchor = the postion "from is at"
            ip = parts[anchor+1] # Ip is the location of from in the string +1 
            ip.strip
            ips.append(ip)
            return ip.strip()
        except (ValueError, IndexError):
            return None 

    return None 

if __name__ == "__main__":

    with open(READ, "r") as f:
        for line in f:
           print (ip_parser(line.strip()))
           count += 1

unique_ips = list(dict.fromkeys(ips))

print("Total lines read =",count)
print("The number of unique IPs found was",len(set(ips)))
print("The first 10 unique IPs were:",unique_ips[:10])

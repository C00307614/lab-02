READ = "sample_auth_small.log" # Input from logfile
count = 0
ip count = 0
ips = []
unique_ip = []
unique = ""

def ip_parser(line): # Method created and called ip_parser

    if " from " in line: # If from is in line (Because IP is printed after "from")
        parts = line.split() # Split the line into parts
        try:
            anchor = parts.index("from") # Anchor = the postion "from is at"
            ip = parts[anchor+1] # Ip is the location of from in the string +1 
            ip.strip
                if ipcount < 9:
                    if unique_ip.count(ip) = 0 
                    ip + unique
            ips.append(ip)
            return ip.strip()

        except (ValueError, IndexError):
            return None # If no IP return none

    return None # If no "from" return non

if __name__ == "__main__":

    with open(READ, "r") as f:
        for line in f:
           print (ip_parser(line.strip()))
           count += 1

print("Total lines read =",count)
print("The number of unique IPs found was",len(set(ips)))
print()



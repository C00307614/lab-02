READ = "sample_auth_small.log" # Input from logfile
from collections import defaultdict
count = 0
ipcount = 0
ips = []
counts = defaultdict(int)
import time



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
           print (ip_parser(line.strip()),end="\n\n") ## Print every Ip found including repeats
           count += 1 # Counting how many IPs read

unique_ips = list(dict.fromkeys(ips))

print("Total lines read =",count,end="\n\n") # Total lines read
print("The number of unique IPs found was",len(set(ips)),end="\n\n") # Set removes duplicates then we check how many items in set
print("The first 10 unique IPs were:",unique_ips[:10],end="\n\n") # First 10 unique IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line: # Find lines with these phrases 
            # extract ip
            ip = ip_parser(line) # Extract IP from these lines
            if ip:
                counts[ip] += 1 # Count how many times each IP appears
                
                
print("The number of login attempts for each IP was: ",counts,end="\n\n") # Print number of login attempts for each IP

start = time.time()
with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line: # Find lines with these phrases
            ip = ip_parser(line) # IP extracted
            if ip:
                counts[ip] += 1 # IP counted and added to dict
                with open("failed_counts.txt", "w") as dst: # Write to failed counts file
                    dst.write("The number of login attempts for each IP was:\n") # Header text
                    for count in counts:
                        dst.write(f"{count}: {counts[count]}\n") # Write every IP and number of login attempts
                def top_n(counts, n=5): # IPs with 5 most login attempts
                        return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]
                        return finish
                        return begin
end = time.time()
count = 0 # Reset count
print("Top 5 Attacker IPs:","\n") # Header Text

for line in top_n(counts): # For each IP printed include Rank (from 1 to 5)
    count = count + 1 
    print(count,"-", line,"\n") # Rank - "IP"

print("Elapsed:", end-start, "seconds")
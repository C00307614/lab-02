count = 1

with open('sample.txt', 'r') as f:
    for line in f:
        print(f"{count}: {line.strip()}")
        count += 1
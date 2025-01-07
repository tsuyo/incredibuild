import sys, re

def extract_timestamp_and_initiators(filename):
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r'\[([^\]]+)\].*Available Floating Initiators: (\d+)', line)
            if match:
                timestamp, initiators = match.groups()
                print(f"[{timestamp}] Available Floating Initiators: {initiators}")

for arg in sys.argv[1:]:
    # print("====================")
    # print(arg)
    # print("====================")
    extract_timestamp_and_initiators(arg)

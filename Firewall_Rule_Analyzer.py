# Import the 're' module to use regular expressions for parsing rule lines
import re

# Function to load firewall rules from a text file
def load_rules(filepath):
    # Open the file at the given path in read mode
    with open(filepath, 'r') as file:
        # Read all lines and return them as a list
        return file.readlines()
    
# Function to analyze firewall rules and flag risky configurations
def analyze_rules(rules):
    print("[*] Analyzing firewall rules...\n")

    # Loop through each rule line in the list
    for line in rules:
        line = line.strip()  # Remove leading/trailing whitespace

        # Check if the rule allows traffic (ACCEPT)
        if "ACCEPT" in line:
            # Extract source IP using regex pattern '-s <IP>'
            src_match = re.search(r'-s (\S+)', line)

            # Extract destination port using '--dport <port>'
            port_match = re.search(r'--dport (\d+)', line)

            # Extract protocol using '-p <protocol>'
            proto_match = re.search(r'-p (\w+)', line)

            # Get matched values or fallback to default labels
            src = src_match.group(1) if src_match else "Unknown"
            port = port_match.group(1) if port_match else "Any"
            proto = proto_match.group(1) if proto_match else "Any"

            # Print a summary of the rule
            print(f"[+] Rule: {proto.upper()} port {port} from {src}")

            # Flag risky rules: open access to sensitive ports from any IP
            if src == "0.0.0.0/0" and port in ["22", "23", "3389"]:
                print("⚠️  Risky: Open access to sensitive port from any IP!")

# Main execution block: runs only when the script is executed directly
if __name__ == "__main__":
    # Prompt the user to enter the path to the firewall rules file
    path = input("Enter path to firewall rules file: ")

    # Load the rules from the specified file
    rules = load_rules(path)

    # Analyze the loaded rules
    analyze_rules(rules)
from collections import defaultdict
import matplotlib.pyplot as plt

# Read SSH failed login logs
with open('ssh_failed_logins.txt') as f:
    logs = f.readlines()

attempts = defaultdict(int)

for line in logs:
    if "Failed password" in line:
        parts = line.split()
        ip_index = parts.index("from") + 1
        ip_address = parts[ip_index]
        attempts[ip_address] += 1

# Print to terminal
for ip, count in attempts.items():
    print(f"{ip}: {count} failed attempts")

# Plotting
ips = list(attempts.keys())
counts = list(attempts.values())

plt.figure(figsize=(10, 6))
plt.bar(ips, counts, color='orange')
plt.xlabel('IP Address')
plt.ylabel('Failed Login Attempts')
plt.title('Failed SSH Login Attempts by IP')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("failed_logins_report.png")
plt.show()

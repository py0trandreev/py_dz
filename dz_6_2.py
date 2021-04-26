FILE_NAME = "nginx_logs.txt"

ip_addresses_dict = {}
with open(FILE_NAME, 'r', encoding="utf-8") as f:
    for line in f:
        ip_addresses_dict[line.split()[0]] = ip_addresses_dict.setdefault(line.split()[0], 0) + 1

max_requests_ip = max(ip_addresses_dict, key=ip_addresses_dict.get)
print(max_requests_ip)
print(ip_addresses_dict[max_requests_ip])

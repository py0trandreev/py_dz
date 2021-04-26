FILE_NAME = "nginx_logs.txt"

with open(FILE_NAME, 'r', encoding="utf-8") as f:
    adr_request_resource_ls = [(line.split()[0], line.split()[5].replace('"',''), line.split()[6]) for line in f ]
    print(adr_request_resource_ls)



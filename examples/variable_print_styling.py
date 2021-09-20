from __future__ import print_function, unicode_literals

ip_addr1 = '172.16.1.1'
ip_addr2 = '172.31.17.99'
ip_addr3 = '217.88.17.1'

# Print a new line
print("\n")
# Print a "banner" of 80 "-" characters 
print("-" * 80)
# Print the defined variables centered in a column 20 characters wide, each
# "<" = left aligned, ">" = right aligned, "^" = center aligned
print("{my_ip:^20}{ip:^20}{ip_alt:^20}".format(ip_alt=ip_addr1, ip=ip_addr2, my_ip=ip_addr3))
print("-" * 80)
print("\n")

import re

ntp = "ntp server 1.1.1.1"
def test(line):
    match = re.search(
        "(ntp\\sserver\\s)(vrf\\s\\w+\\s)?(\\d+\\.\\d+\\.\\d+\\.\\d+)", line, re.M
        )

    if match.group(2) and match.group(3):
        vrf = match.group(2)
        server = match.group(3)

        return vrf, server

    if match.group(3):
        vrf = None
        server = match.group(3)

        return vrf, server



match = re.search("ntp (\\S+)", ntp, re.M)

if match:
    vrf, server = test(ntp)




#vrf, server=test(ntp)

print(vrf)
print(server)
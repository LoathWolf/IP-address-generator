import random

def ip_generator ():
    return str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255))
print (ip_generator())

def ipbin(ip=ip_generator()):
    ans = []
    for x in ip.split('.'):
        ans.append(bin(int(x)+256)[3:])
    return '.'.join(ans)
print(ipbin())

def iphex(hexip=ip_generator()):
    lstHEX = hexip.split('.')
    sum = 0
    ans = ''
    for octet in lstHEX:
        ans += str(hex(int(octet)))
    return ans
print('{}' '{}'.format(iphex(), '/'))













#ip = ip_generator.format?
#print '.'.join([bin(int(x)+256)[3:]for x in ip.split('.')])

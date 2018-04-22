# M1
s = '   abc  123  '
print s.strip()
print s.lstrip()
print s.rstrip()

s = '--abc++++'
print s.strip('+-')

# M2
s = 'abc:123'
print s[:3] + s[4:]  # abc123

# M3
s = '\tabc\t112\txyz'
s.replace('\t', '')

s = '\tabc\t112\tx\ryz'
import re

print re.sub('[\t\r]', '', s)

# M4
s = 'abc12323s02xyz'
import string

t = string.maketrans('abcxyz', 'xyzabc')
print s.translate(t)

s= 'abc\refg\n2131\t'
print s.translate(None, '\t\r\n')

u = u'ni\u0301 ha\u030co'
print u.translate(dict.fromkeys([0x0301,0x030c]))

import re

s = '2016-04-12'

print re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s)  # 04/12/2016
print re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', s)  # 04/12/2016

import json

l = [1, 2, 'abc', {'name': 'Bob'}]
print json.dumps(l, sort_keys=True)

j = '[1, 2, "abc", {"name": "Bob"}]'
print json.loads(j)

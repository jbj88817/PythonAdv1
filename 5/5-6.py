from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile()
f.write('abcdf' * 100000)
f.seek(0)

print f.read(100)

ntf = NamedTemporaryFile()
print ntf.name

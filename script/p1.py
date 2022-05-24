import os

cmd = 'ls -a ../'
v1 = os.popen(cmd)
#res = val.read()  
#for line in res.splitlines():  
#	print(line)

for i in v1.readlines():
  print(i)

import os

#val = os.popen('nvme write -s 0 -c 0 -z 4096 -d ECB_19_4096_input.bin /dev/nvme0n1')
#for i in val.readlines():
#  print(i)  


v1 = os.popen('nvme read -s 0 -c 0 -z 4096 -d xx.bin /dev/nvme0n1')
for i in v1.readlines():
  print(i)



v2 = os.popen('diff xx.bin ECB_192_4096_output.bin')
print("diff:")
for i in v2.readlines():
  print(i)
print("\n")

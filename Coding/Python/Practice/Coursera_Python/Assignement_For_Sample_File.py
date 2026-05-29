import re
sum1=0
stuff=[]
Sample_file=open("Sample_file.txt")
for lines in Sample_file:
    lines=lines.rstrip()
    #print(lines)
    y=re.findall('[0-9]+', lines)
    for i in y:
        sum1=sum1+int(i)
print(sum1)

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()
for line in handle :
    if line.startswith('From ') :
        colon = line.find(':')
        hour = line[ colon - 2 : colon]
        d[hour] = d.get(hour,0) + 1

l = list()
for k,v in d.items() :
    l.append( ( k , v ) )

l.sort()

for k,v in l :
    print k, v

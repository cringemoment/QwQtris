from os import system as ossystem

def system(command):
    print(command)
    ossystem(command)

fumen = "v115@HhA8IeC8EeF8DeB8JeAgWHAqyjPCaXdBA"
queue = "JLSJZOI"
queue = ','.join([i for i in queue])
clear = 4

system(f"java -jar sfinder.jar path -t {fumen} -p {queue} --clear {clear} --hold avoid -split yes -f csv -k pattern -o output/path.csv -K kicks/jstris180.properties -d 180 > ezsfinder.txt")

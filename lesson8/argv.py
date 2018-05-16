import sys

print (len(sys.argv))
for arg in range(len(sys.argv)):
    print sys.argv[arg]

'''Students-MacBook-Pro:lesson8 student$ python argv.py 1 3 4 5 6
 6
 argv.py
 1
 3
 4
 5
 6   
 '''

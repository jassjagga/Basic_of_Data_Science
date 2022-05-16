import simplefunction
#other way to import fucntion is also like
#import simplefunction as fun

#if the function is in another directory then you have to provide th loaction then
#import (FOLDER NAME).simplefunction as fun

#if the code is totally in deferent folder or location then we have to use system path
#eg import sys
#sys.path.append("C:\pycode")
#import simplefunction as fun

area = simplefunction.cal_squ_area(5)
print(area)

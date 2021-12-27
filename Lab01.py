
from datetime import datetime

nCurYear = datetime.today().year

sName = input('Enter your name: ')
nAge = int(input('Enter your : '))

n100Year = nCurYear + 100 - nAge
if n100Year<nCurYear:
    sVerb = 'was'
else:
    sVerb = 'is going to be'

print(sName+', the year of your 100th birthday ' + sVerb + ' in ' +str(n100Year))
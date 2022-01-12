#company challenge
import functions2
from functions import my_nick
def designs(completed, pending):
    while pending:
        curentdesign =  pending.pop()
        print('we are designing'+ curentdesign)
        completed.append(curentdesign)
        #return pending

def finisher(completed):
    for complete in completed:
        print('design is completed for'+ complete)

pending= ['carcase',' roboticc arm', 'gearbox']
completed = []

designs(completed,pending)
finisher(completed)
#how to call a function from another module
#functions2.namez('Jojo','Fachi')
my_nick('josh','orkuma')
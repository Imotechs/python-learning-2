values = [1,2,3,4,5,6,7,8,9]
#index are0,1,2,3,4,5,6,7,8
web = 'http://fees.uam.edu.ng'
print (web[7:-3])
#           [start:end:step]
print(values[:8:3])
x= 'global x'
def test():
    x= 'outer x'
    def test():
        x = 'inner x'
        print(x)
    test()
    print(x)
test()
print(x)
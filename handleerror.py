try:
    f = open('testss.txt')
except Exception:
    print('file not found')
#Exception: as used, handles general errors lets try to be specific to differenciate b/w errors
try:
    f = open('testss.txt')
except FileNotFoundError:
    print('Kwame!! no existence')
#so we ussually make the Exception: block last to know more about our 
# errors in real programing

try:
    f = open('fakefile.txt')
except FileNotFoundError:
    print('file not Found!!')
except Exception:
    print('Fatal Error!!')

# to know about the error that is thrown, we go about it this way
try:
    f = open('fakefile.txt')
except FileNotFoundError as error:
    print(error)
except Exception as error:
    print(error)
""" the above is the best method for try stmt cos it tells the nature of foult"""

# we finally include an else statement to do the main work if no error is gotten
try:
    f = open('file2.txt')
except FileNotFoundError as error:
    print(error)
except Exception as error:
    print(error)
else:
    print(f.read())
    f.close()
# finally: the finnaly block will run regardless of what happens. i.e it is the defaoult
# value that is available when an error is thrown and the programmer feels
# the user should acces a default recources
try:
    f = open('file2.txt')
except FileNotFoundError as error:
    print(error)
except Exception as error:
    print(error)
else:
    print(f.read())
    f.close()
finally:
    print('executing finnaly...')
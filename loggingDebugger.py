#turn off logging messages easily, as opposed to using print
'''
Five logging levels (lowest to highest) DEBUG, INFO, WARNING, ERROR, CRITICAL
'''

import logging

#use this to determine where the logging will go 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#this disables logging, so we get no meesages at CRITICAL or Lower
logging.disable(logging.CRITICAL)

#basic level debugging
logging.debug('start program')

def factorial(n):
    logging.debug('start of function')
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    return total

print(factorial(5))

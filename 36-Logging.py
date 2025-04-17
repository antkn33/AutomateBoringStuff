#
# logging setup code
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# log to file by adding this right before level
# filename='logfile.txt', 

# disable ctrical messages and below
# logging.disable(logging.CRITICAL)


# Factorial 
# ex. Factorial 4 is: 1*2*3*4 = 24

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    # need to start the range at 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(8))

logging.debug('End  of program')


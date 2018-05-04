import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s:	%(filename)s: %(name)s')

file_handler = logging.FileHandler('sample_test_logging.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


stream_handler = logging.StreamHandler()


#logFmt = logging.Formatter('%(asctime)s\t%(levelname)s -- %(filename)s:%(lineno)s -- %(message)s')
#print(logging.getLogger('Extract'))

#print(log)

#############################################
#Logging Levels
#############################################
#DEBUG : Detailed information, typically of interest when identifying the problem
#INFO : Confirmation that things are working as expected
#WARNING : Indication that something unexpected happened or will happen in the future. Still works as expected.
#ERROR : Due to more seriouse problem, it is not able to perform some function
#CRITICAL : A serious error, indicating program itself may be not able to execute/


#logging.basicConfig(filename = 'test_logging.log', level=logging.DEBUG,
 #                   format ='%(asctime)s:%(levelname)s:%(message)s:	%(filename)s')

def add(x,y):
    return x+y


def sub(x,y):
    return x-y

def div(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        logger.exception('divide by zero not valid')
    else:
        return result

x = 5
y = 0

logger.debug(div(x,y))
add_result = add(x,y)
logger.debug(add_result)
logger.debug(sub(x,y))


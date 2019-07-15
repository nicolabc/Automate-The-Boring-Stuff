#! python3
import sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
if __name__ == '__main__':
    #raise Exception('This is the error message')
    # podBayDoorStatus = 'open'
    # assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
    # podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
    # assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

    ## Assertion. This is to be certain that a variable has the correct critical value
    
    # value = 1
    # assert value == 1,'HAS TO BE 1!'
    # value += 1
    # assert value == 1,'HAS TO BE 1!!'
    # print(value)

    #logging.debug()
    #logging.info()
    #logging.warning()
    #logging.error()
    #logging.critical()
    logging.disable(logging.CRITICAL)
    
    # Logging is preferred over printing as a printing may interfere with the execution of the code
    
    sys.exit()

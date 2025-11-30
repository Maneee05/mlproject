import sys
import logging

def error_message_detail(error,error_detail:sys):   # error detail will be present in sys module
    _,_,exc_tb=error_detail.exc_info()
    ''' 
    exc_info() gives 3 values (type, value, traceback)
    we only care about the 3rd value, ignore other 2
    so exc_tb holds traceback which shows where the error happened — file, line number, stack.
    '''
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):  #CustomException class inherits from Python's built-in class Exception, ie, class Child(Parent):
    def __init__(self,error_message,error_detail:sys): #init is a constructor called automatically when an obj is created
        super().__init__(error_message)   # init to inherit the exception class. super() calls the parent class. here we store the error message  in the parent class as well simply bcoz it always expects a value
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self): # str controls what Python should print when print() for the object is called 
        '''
        Without __str__, printing the object shows something ugly like:
        <__main__.Person object at 0x000001>
        '''
        return self.error_message

'''    just for trial if it works or not
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)
'''
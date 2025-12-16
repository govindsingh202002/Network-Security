import sys

def get_error_detail_message(error,error_details)-> str:
    _,_,exc_tb=error_details.exc_info()

    if exc_tb is None:
        error_message=f"Error message without error location details : {str(error)}"
        return error_message

    error_message_line_number=exc_tb.tb_lineno
    error_message_file_name=exc_tb.tb_frame.f_code.co_filename

    error_message="Error occurred in file name [{0}] at line number [{1}] and error message is [{2}]".format(error_message_file_name,error_message_line_number,str(error))
    return error_message

class NetworkSecurityException(Exception):
    def __init__(self,error,error_details):
        super().__init__(str(error))
        self.error_message=get_error_detail_message(error,error_details)

    def __str__(self):
        return self.error_message


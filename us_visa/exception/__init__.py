import os 
import sys

def error_message_details(error, error_detail=sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in file [{0}] on line number [{1}] and error is [{2}]".format(filename, exc_tb.tb_lineno, str(error)
    )

    return error_message


class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message


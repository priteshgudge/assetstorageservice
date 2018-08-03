from datetime import datetime
from assetstorageservice.utils.exceptions.custom_error import CustomError
from assetstorageservice.utils.response_utils import error_response
from assetstorageservice.utils.logger_utils import get_logger
import traceback
from jsonschema import ValidationError

logger = get_logger()


class ErrorHandler(object):
    def __init__(self, api_key, app):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.api_key = api_key
        self.app = app
        self.logger = logger


    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args, **kwargs):
            try:

                start = datetime.now()
                output = f(*args, **kwargs)
                self.logger.info("Time taken for %s is %s", self.api_key,
                                 datetime.now() - start)
                return output

            except KeyError as e:
                exception_trace = traceback.format_exc()
                self.logger.error("Exception in %s API:\n%s",
                                  self.api_key, exception_trace)
                self.logger.error("Missing key : {}".format(e))
                return error_response(400, "{} is required".format(e))

            except ValueError as e:
                exception_trace = traceback.format_exc()
                self.logger.error("Exception in %s API:\n%s",
                                  self.api_key, exception_trace)
                return error_response(400,
                                      "Bad Request. Incorrect Parameter types")

            except CustomError as error:
                exception_trace = traceback.format_exc()
                self.logger.error("Exception in %s API: %s\n%s",
                                  self.api_key,
                                  error.get_message(),
                                  exception_trace)
                return error_response(error.get_error_code(),
                                      error.get_message())
            except ValidationError as e:
                exception_trace = traceback.format_exc()
                self.logger.error("Exception in %s API:\n%s",
                                  self.api_key, exception_trace)
                return error_response(400,
                                      "Bad Request. Incorrect Parameters")
            except:
                exception_trace = traceback.format_exc()
                self.logger.error("Exception in %s API:\n%s",
                                  self.api_key, exception_trace)
                return error_response(500, "Internal Server Error")
            finally:
                pass

        return wrapped_f

from typing import Dict
from .queue import ProcessQueue, Queue


class Response:
    def __init__(self, sucess:bool, requester_service_name:str, response_data:dict=None):
        self.sucess = sucess
        self.response_data = response_data
        self.requester_service_name = requester_service_name

class Request:
    '''Stores some request info.
    '''

    def __init__(self, service_name:str, operation_name:str, response_service_name:str, request_info:dict=None):
        '''Request constructor

            :param service_name: Name of requested service
            :type service_name: str

            :param operation_name: Name of requested operation
            :type operation_name: str

            :param request_info: Request parameters
            :type request_info: dict

            :param response_queue: Queue to send response
            :type response_queue: breath.api_interface.Queue
        '''
        
        self.service_name = service_name
        self.operation_name = operation_name
        self.request_info = request_info
        self.response_service_name = response_service_name

    def create_response(self, sucess:bool, response_data:dict=None) -> Response:
        return Response(sucess, self.response_service_name, response_data)

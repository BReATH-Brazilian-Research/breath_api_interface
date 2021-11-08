import time

from .request import Request, Response

from .queue import Queue

class ServiceProxy:
    '''Provides acess for BReATH services.

        :ivar manager_queue: Queue for send requests
        :type manager_queue: breath.api_interface.Queue

        :ivar response_queue: Queue for getting requests responses
        :type response_queue: breath.api_interface.Queue
    '''

    def __init__(self, manager_queue:Queue, response_queue:Queue):
        '''ServiceProxy constructor.

            :param manager_queue: Queue for send requests
            :type manager_queue: breath.api_interface.Queue

            :param response_queue: Queue for getting requests responses
            :type response_queue: breath.api_interface.Queue
        '''
        self.manager_queue = manager_queue
        self.response_queue = response_queue

    def send_request(self, request: Request) -> Response:
        '''
            Send some service request.

            Blocks the code while waiting for response. It might be better to use multithreading.
        
            :param request: Request to be send.
            :type request: breath.api_interface.Request

            :return: Request response
            :rtype: Response
        '''

        request.responseQueue = self.response_queue
        
        while self.manager_queue.full():
            continue

        
        
        self.manager_queue.insert(request)

        while self.response_queue.empty():
            time.sleep(1E-3)

        response = self.response_queue.get()

        return response
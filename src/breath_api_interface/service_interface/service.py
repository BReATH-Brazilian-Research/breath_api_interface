from abc import ABC, abstractmethod
from typing import Union

from breath_api_interface import ServiceProxy, Queue, Request


class Service(ABC):
    '''BReATH service base class.
    '''

    def __init__(self, proxy:ServiceProxy, request_queue:Queue):
        '''Service constructor.

            :param proxy: Proxy for sending requests
            :type proxy: breath_api_interface.ServiceProxy

            :param request_queue: Queue for getting requests
            :type request_queue: Queue
        '''
        self._proxy = proxy
        self._request_queue = request_queue

    def start(self):
        pass

    @property
    def request_queue(self) -> Queue:
        '''Get the queue for sending requests.
        '''
        return self._request_queue

    def _get_request(self) -> Union[Request, None]:
        '''Get some request, if available
        '''
        if not self._request_queue.empty():
            return self._request_queue.pop()
        else:
            return None
    
    def run_forever(self):
        self.start()
        while(True):
            self.run()

    @abstractmethod
    def run(self):
        '''Run the service.
        '''
        ...
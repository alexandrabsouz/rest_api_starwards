from collections import namedtuple
from typing import Type, Dict, Tuple

import requests
from requests import Request
from src.errors import HttpRequestError


class SwapiApiConsumer:
    
    ''' Class to consume swapi api with http requests '''
    
    def __init__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starships', 'status_code request response')
    
    
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        req = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships/',
            params={'page': page}
        )
        
        req_prepared = req.prepare()
        
        response = self.__send_http_request(req_prepared)
        status_code = response.status_code
        
        if status_code >= 200 and status_code <= 299:
            return self.get_starships_response(
                status_code=response.status_code, request=req, response=response.json()
            )
            
        else:
            raise HttpRequestError(
                message=response.json()['detail'], status_code=status_code
            )
        
    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        '''
            Prepare a session and send http request
            :param - req_prepare: Resquest Object with all params
            :response - Http response raw
        '''
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
        
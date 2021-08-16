from .swapi_api_consumer import SwapiApiConsumer

def test_get_starships():
    swapi_api_consumer = SwapiApiConsumer()
    response = swapi_api_consumer.get_starships(page=10)
    
    print(response)
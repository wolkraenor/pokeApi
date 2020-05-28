from app.settings import URL_POKE_API
import requests
import json


class PokemonsRequest():
    def request_data(self, url, offset=None):
        params = {
            'offset': offset
        }
        request = requests.get(url, params=params)
        response = json.loads(request.text)
        return response

    def request_data_by_id(self, identification_number):
        url = URL_POKE_API + "/" + str(identification_number)
        request = requests.get(url=url)
        response = json.loads(request.text)
        return response

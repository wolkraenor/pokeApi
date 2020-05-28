from app.adapter import PokemonsRequest
from app.settings import URL_POKE_API
import json

class PokemonRest():
    def __init__(self):
        self.data = PokemonsRequest()

    def get_all_pokemons(self):
        response = self.data.request_data(url=URL_POKE_API)
        pokelist = self.__next_pokemons(response)
        return pokelist

    def get_pokemon_by_id(self, identification_number):
        pokemon = self.data.request_data_by_id(identification_number=identification_number)
        return pokemon

    def get_pokemon_by_name(self, name, offset=20, limit=0, sort='asc'):
        response = self.data.request_data(url=URL_POKE_API)
        pokelist = self.__next_pokemons(response)
        match = self.__attach_pokemon_by_name(pokelist, sort, name=name)
        return match

    def __next_pokemons(self, response):
        pokelist = []
        for x in response["results"]:
            pokelist.append(x)
        all_pokemons = response.get("count")
        while len(pokelist) != all_pokemons:
            url = response.get("next")
            if url is not None:
                response = self.data.request_data(url=url)
            else:
                response = self.data.request_data(url=URL_POKE_API, offset=len(pokelist))
                for x in response["results"]:
                    pokelist.append(x)

        return pokelist

    def __attach_pokemon_by_name(self, pokelist, sort, name):
        attach = []
        sort = False
        for i in range(len(pokelist)):
            pokemon_name = pokelist[i].get('name')
            if name in pokemon_name:
                attach.append(pokelist[i])
                print(attach)
        if sort == "desc":
            sort = True
        result = sorted(attach, key=lambda x: x['name'], reverse=sort)
        return result

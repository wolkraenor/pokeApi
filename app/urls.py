from app import app
from flask import jsonify, request
from app.service import PokemonRest

poke = PokemonRest()


@app.route('/status')
def status():
    return {'response': 'OK'}, 200


@app.route('/pokemon', methods=['GET'])
def get_pokemons():
    print("hello")
    response = poke.get_all_pokemons()
    return jsonify(dict(data=response)), 200


@app.route('/pokemon/<int:id>', methods=['GET'])
def get_pokemons_by_id(id):
    response = poke.get_pokemon_by_id(identification_number=id)
    return jsonify(dict(pokemon=response)), 200


@app.route('/pokemon/<string:name>', methods=['GET'])
def get_pokemons_by_name(name):
    offset = request.args.get('offset')
    limit = request.args.get('limit')
    sort = request.args.get('sort')
    response = poke.get_pokemon_by_name(name, offset, limit, sort)
    return jsonify(dict(data=response)), 200

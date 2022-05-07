def search_for_intelligence(name_list, host, token):

    from pprint import pp, pprint
    import requests

    dict_intell ={}

    for name in name_list:
        resp = requests.get(f"{host}/{token}/search/{name}")
        dict_intell[name] = int(resp.json()['results'][0]['powerstats']['intelligence'])

    for name_hero, vol in dict_intell.items():
        if vol == max(dict_intell.values()):
            print(f"Самый умный из супергероев - {name_hero} c показателем intelligence {vol}")

search_for_intelligence(['Hulk', 'Captain America', 'Thanos'], 'https://superheroapi.com/api', '2619421814940190')
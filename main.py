from pycricbuzz import Cricbuzz
now = Cricbuzz()
matches = now.matches()

for match in matches:
    print(match)
    if(match['mchstate'] != 'nextlive'):
        print(now.livescore(match['id']))
        print(now.commentary(match['id']))
        print(now.scorecard(match['id']))

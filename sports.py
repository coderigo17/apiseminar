import json, os, requests, webbrowser

def main():
    # Submit a GET request to api
    res = requests.get('https://www.thesportsdb.com/api/v1/json/1/searchteams.php',
                       params={'t': 'Barcelona'})

    # Check that everything worked
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')

    # Convert response to JSON and print out info nicely
    json_data = json.dumps(res.json(), indent=4, separators=(',', ': '))

    # Retrieve url and open in chrome
    webbrowser.get('/usr/bin/google-chrome %s').open(json.loads(json_data)['teams'][0]['strWebsite'])

if __name__ == '__main__':
    main()

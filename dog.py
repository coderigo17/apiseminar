import json, os, requests, webbrowser

def main():
    # Submit a GET request to api
    res = requests.get('https://dog.ceo/api/breeds/image/random')

    # Check that everything worked
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')

    # Convert response to JSON and print out info nicely
    json_data = json.dumps(res.json(), indent=4, separators=(',', ': '))

    # Retrieve url and open in chrome
    webbrowser.get('/usr/bin/google-chrome %s').open(json.loads(json_data)['message'])

if __name__ == '__main__':
    main()

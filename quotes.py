import json, os, requests

def main():
    # Submit a GET request to api
    res = requests.get('http://quotesondesign.com/wp-json/posts',
                       params={'filter[orderby]': 'rand',
                               'filter[posts_per_page]': 5})

    # Check that everything worked
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')

    # Convert OrderedDict to JSON and print out info nicely
    json_data = json.dumps(res.json(), indent=4, separators=(',', ': '))
    print(json_data)

if __name__ == '__main__':
    main()

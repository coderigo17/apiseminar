import json, os, requests, xmltodict

def main():
    # Submit a GET request to api
    res = requests.get('http://thecatapi.com/api/images/get',
                       params={'format': 'xml',
                               'results_per_page': 5})

    # Check that everything worked
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')

    # Convert the response to XML data
    xml_data = res.content

    # Convert XML data to OrderedDict
    res_dict = xmltodict.parse(xml_data)

    # Convert OrderedDict to JSON and print out info
    json_data = json.dumps(res_dict, indent=4, separators=(',', ': '))
    print(json_data)

if __name__ == '__main__':
    main()

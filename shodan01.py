#region Prep

import shodan # version 1.28.0

SHODAN_API_KEY = "______get_your_own_please_______"

api = shodan.Shodan(SHODAN_API_KEY)

#endregion

# Wrap the request in a try/ except block to catch errors
try:
    # Search Shodan
    results = api.search('city:"hurghada"')

    # Show the results
    print('Results found: {}'.format(results["total"]))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')

except shodan.APIError as e:
    print('Error: {}'.format(e))

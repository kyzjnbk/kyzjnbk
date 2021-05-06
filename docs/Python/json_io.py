import json
from pprint import pprint

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23,
    'dict': {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23,
        'dict': {
            'name': 'ACME',
            'shares': 100,
            'price': 542.23,
            'dict': {
                'name': 'ACME',
                'shares': 100,
                'price': 542.23
            }
        }
    }
}

print(json_str := json.dumps(data))
print(json.loads(json_str))
pprint(data)

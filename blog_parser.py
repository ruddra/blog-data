import json
import datetime

data = json.load(open('db.json'))

_data = []

for item in data:
    if item.get('status') == 'published':
        _item = {
            'id': item.get('id'),
            'title': item.get('title'),
            'markdown': item.get('markdown'),
            'published_at': datetime.datetime.fromtimestamp(
                int(item.get('published_at'))/100
                ).strftime('%Y-%m-%d %H:%M:%S')
        }
        _data.append(_item)

with open('data_updated.json', 'w') as outfile:
    json.dump(_data, outfile)
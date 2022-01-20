news_article = [
    {'id': 123, 'title': 'Happy New Year', 'date': '01-01-2022', 'desc': 'Wishing you a happy new year!', 'type': 'General'},
    {'id': 123, 'title': 'Happy New Year', 'date': '01-01-2022', 'desc': 'Wishing you a happy new year!', 'type': 'General'},
    {'id': 123, 'title': 'Happy New Year', 'date': '01-01-2022', 'desc': 'Wishing you a happy new year!', 'type': 'General'},
    {'id': 123, 'title': 'Happy New Year', 'date': '01-01-2022', 'desc': 'Wishing you a happy new year!', 'type': 'General'},
    {'id': 123, 'title': 'Happy New Year', 'date': '01-01-2022', 'desc': 'Wishing you a happy new year!', 'type': 'General'},
    {'id': 123, 'title': 'Happy New Year', 'date': '01-01-2022', 'desc': 'Wishing you a happy new year!', 'type': 'General'}
]

#news_article = {'id': [123,124,125,126..], 'title': ...}
print(news_article)

for i in news_article:
    print(i.get('type'))
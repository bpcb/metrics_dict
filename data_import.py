import datetime

fixture = []

i = 1
for metric in metrics_dict:
    f = dict()
    f['model'] = 'metrics.Metric'
    f['pk'] = i
    f['fields'] = {
        'metric_name': metric,
        'metric_text': ' '.join(metrics_dict[metric].split()),
        'update_date': str(datetime.datetime.now()),
        'experience': 'Web',
    }
    
    i += 1
    
    fixture.append(f)
    
with open('fixture.json', 'w') as outfile: 
    json.dump(fixture, outfile)
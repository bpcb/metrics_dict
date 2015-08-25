# this approach works when there were only "metrics", no definitions. sql code was saved to the Metric model, as was the experience
# the code was (from the command line) something like 'python manage.py loaddata fixtures.json'
# as a result, our metrics_dict was temporarily stored exclusively in metric objects.

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

# from the python shell ('python manage.py shell'), the following allowed me to take the sql code stored in the metric_text
# field in a given metric object and save it to (and create) a definition object.

from metrics.models import Metric, Definition

for metric in Metric.objects.all():
    d = Definition(metric = metric, sql = metric.metric_text)
    d.save()

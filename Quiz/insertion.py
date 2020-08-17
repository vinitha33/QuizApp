'''

"This happens in 'python manage.py shell',since we dont want this to be added
each time using this way"

import csv
from Questions.models import Question
from django.db import IntegrityError

with open("questions.csv", encoding='utf-8-sig') as f:
    read = csv.DictReader(f)
    for i in read:
        print(i)
        print("This is happening!!!!")
        try:
            p = Question(Question=i['Question'], Option_A=i['Option A'],
                          Option_B=i['Option B'], Option_C=i['Option C'],
                          Option_D=i['Option D'], Answers=i['Answer'])
            p.save()
        except IntegrityError:
            print("ERROR: Question already exists!")
'''
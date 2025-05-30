import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
# \/ Assim é que faz o django funcionar \/
# os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)

# Final do segundo erro
#   File "C:\Users\emers\OneDrive\Documentos\projeto_agenda_2\venv\Lib\site-packages\django\conf\__init__.py", line 166, in __init__
#     mod = importlib.import_module(self.SETTINGS_MODULE)
#   File "C:\Users\emers\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py", line 88, in import_module
#     return _bootstrap._gcd_import(name[level:], package, level)
#   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
#   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
#   File "<frozen importlib._bootstrap>", line 1310, in _find_and_load_unlocked
#   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
#   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
#   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
#   File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
# ModuleNotFoundError: No module named 'project'
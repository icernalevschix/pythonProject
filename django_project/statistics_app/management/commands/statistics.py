from django.core.management.base import BaseCommand, CommandError
from job_list.models import Post
import spacy
from spacy.matcher import Matcher

from .draw_graphs import totals_graph

nlp = spacy.load("en_core_web_sm")
# nlp = spacy.load('xx_ent_wiki_sm')
matcher = Matcher(nlp.vocab)

obj_c_pattern1 = [{'LOWER': 'objective'},
                {'IS_PUNCT': True, 'OP': '?'},
                {'LOWER': 'c'}]
python_pattern = [{'LOWER': 'python'}]
c_pattern = [{'LOWER': 'c'},
           {'IS_ASCII': True, 'OP': '?'},
           {'LOWER': 'c++'}]
c_pattern2 = [{'ORTH': 'С/С++'}]
c_pattern3 = [{'ORTH': 'С'},
           {'IS_ASCII': True, 'OP': '?'},
           {'ORTH': 'С++'}]
c_pattern4 = [{'LOWER': 'c++'}]
java_pattern = [{'LOWER': 'java'}]
java_pattern2 = [{'LOWER': 'android'}]
c_sharp_pattern = [{'ORTH': 'С'},
                  {'ORTH': '#'}]
c_sharp_pattern2 = [{'ORTH': 'С#'}]
c_sharp_pattern3 = [{'LOWER': 'c'},
                    {'ORTH': '#'}]
c_sharp_pattern4 = [{'LOWER': '.net'}]
javascript_pattern = [{'LOWER': 'javascript'}]
javascript_pattern2 = [{'LOWER': 'js'}]
php_pattern = [{'LOWER': 'php'}]
swift_pattern = [{'LOWER': 'swift'}]

matcher.add('OBJECTIVE-C', None, obj_c_pattern1) 
matcher.add('PYTHON', None, python_pattern)
matcher.add('C/C++', None, c_pattern, c_pattern2, c_pattern3, c_pattern4)
matcher.add('JAVA', None, java_pattern, java_pattern2)
matcher.add('C#', None, c_sharp_pattern, c_sharp_pattern2, c_sharp_pattern3, c_sharp_pattern4)
matcher.add('JAVASCRIPT', None, javascript_pattern, javascript_pattern2)
matcher.add('PHP', None, php_pattern)
matcher.add('SWIFT', None, swift_pattern)

languages = {}

class Command(BaseCommand):

    def handle(self, *args, **options):

        for post in Post.objects.all():
            print('\n', post.title)
            nlp_title = nlp(post.title + ' ' + post.content)
            print('\n', nlp_title)
            matches = matcher(nlp_title)

            match_ids = set()

            for match_id, start, end in matches:
                lang = nlp.vocab.strings[match_id]
                print(nlp_title[start:end])
                print(matches)

                if lang not in match_ids:
                    languages[lang] = languages.get(lang, 0) + 1

                match_ids.add(lang)
            print(match_ids)

        print(languages)
        graph1 = totals_graph(sorted(languages.items(), key=lambda x: x[1], reverse = True))
        graph1.savefig('media/statistics/totals_chart.jpg')

        
        


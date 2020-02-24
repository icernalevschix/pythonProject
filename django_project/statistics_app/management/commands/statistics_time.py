from django.core.management.base import BaseCommand, CommandError
from job_list.models import Post
from datetime import date
import requests
import timeit

class Command(BaseCommand):

    @staticmethod
    def run_request(query, url):
        request = requests.post(url, json={'query': query})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

    @staticmethod
    def run_query():
        return Post.objects.all()

    def handle(self, *args, **options):

        query = 'query{jobs {\
                    title\
                    content\
                    }}'
        url = 'http://localhost:8080/graphql/'

        start_time = timeit.default_timer()
        print(self.run_request(query, url))
        elapsed = timeit.default_timer() - start_time
        print('Function took {time} seconds to complete.'.format(time=elapsed))
        
        start_time = timeit.default_timer()
        print(self.run_query())
        elapsed = timeit.default_timer() - start_time
        print('Function took {time} seconds to complete.'.format(time=elapsed))



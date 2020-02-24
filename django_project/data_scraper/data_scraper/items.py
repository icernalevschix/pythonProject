from scrapy_djangoitem import DjangoItem
from job_list.models import Post


class PostItem(DjangoItem):
    django_model = Post
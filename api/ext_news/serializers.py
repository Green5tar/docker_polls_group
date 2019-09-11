from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = News
        fields = ('id', 'title', 'discription', 'news_link', 'images_link', 'is_checked',)
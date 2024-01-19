from rest_framework import serializers
# serializing these models, if filed not here serialize parent
from .models import BlogCategory,HomePage,Tag,BlogPage,BasePage
from .fields import TagField,CategoryField
from wagtail.api.v2.serializers import StreamField
from wagtail.images.api.fields import ImageRenditionField 
from wagtail import fields
from wagtail.api.v2 import serializers as wagtail_serializers



class BlogPageSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPage
        # fields=BasePageSerializer.Meta.fields
        fields=["id","slug","title","url","last_published_at"]

class HomePageSerializer(serializers.ModelSerializer):
    # all the tags would go in here; be serialized into dict and then be passed further
    tags=TagField()
    categories=CategoryField()
    contents = StreamField()
    header_image = ImageRenditionField("max-1000x800") 
    class Meta:
        model=HomePage
        # fields=BasePageSerializer.Meta.fields+["tags","categories","body","header_image"]
        fields=["id","slug","title","url","last_published_at","tags","categories","body","header_image"]

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogCategory
        fields=['id','slug','name']

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model=Tag
        fields=['id','slug','name']
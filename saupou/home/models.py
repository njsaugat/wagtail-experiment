from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from taggit.models import Tag as TaggitTag
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from modelcluster.tags import ClusterTaggableManager
from wagtail.fields import StreamField
from wagtail import blocks

from wagtail.images.blocks import ImageChooserBlock

class BlogPage(Page):
    pass

class HomePage(Page):
    body = RichTextField(blank=True)
    contents= StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('page', blocks.PageChooserBlock()),
        ('image', ImageChooserBlock()),
    ], null=True, blank=True,use_json_field=True)
    
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    tags = ClusterTaggableManager(through="home.HomePageTag", blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('header_image'),
        InlinePanel("categories", label="category"),
        FieldPanel("tags"),
        FieldPanel('contents'),
        
    ]
    

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True



class HomePageBlogCategory(models.Model):
    # acts as link table -->page related to which blog category
    page = ParentalKey(
        "home.HomePage", on_delete=models.CASCADE, related_name="categories"
    )
    blog_category = models.ForeignKey(
        "home.BlogCategory", on_delete=models.CASCADE, related_name="post_pages"
    )

    panels = [
        FieldPanel("blog_category"),
    ]

    class Meta:
        unique_together = ("page", "blog_category")

class HomePageTag(TaggedItemBase):
    content_object = ParentalKey("home.HomePage", related_name="post_tags")

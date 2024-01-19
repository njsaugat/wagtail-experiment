from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.blocks import ImageChooserBlock


# could be in blocks class:
class CustomImageChooserBlock(ImageChooserBlock):
    def __init__(self, *args, **kwargs):
        self.rendition = kwargs.pop("rendition", "original")
        super().__init__(**kwargs)

    def get_api_representation(self, value, context=None):
        return ImageRenditionField(self.rendition).to_representation(value)
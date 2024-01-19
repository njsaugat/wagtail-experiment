from rest_framework.fields import Field

class TagField(Field):
    def to_representation(self, tags):
        print("tags----------------",tags)
        try:
            return [
                {"name":tag.name,"slug":tag.slug,"id":tag.id} for tag in tags.all()
            ]
        except Exception:
            return []
        


class CategoryField(Field):
    def to_representation(self, categories):
        try:
            return [
                {"name":category.name,"slug":category.slug,"id":category.id} for category in categories.all()
            ]
        except Exception:
            return []
Django image field with thumb and size check.


#models.py

    from cms_images.fields import CmsImageField
    from cms_images.models import Image

    class Item(models.Model):
        #single image
        img = CmsImageField(u'Image', help_text=u'...', upload_to='items')

        #generic relation
        img_more = GenericRelation(Image)



#admin.py

    from ..cms_images.admin import ImageInline

    class ItemAdmin(admin.ModelAdmin):
        #generic relation
        inlines  = [ImageInline, ]
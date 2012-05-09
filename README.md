Django image field with thumb and size checking.


#models.py

    from advanced_imagefield.fields import AdvancedImageField
    from advanced_imagefield.models import AdvancedImage

    class Item(models.Model):
        #single image
        img = AdvancedImageField(u'Image', upload_to='items')

        #generic relation
        img_more = GenericRelation(AdvancedImage)



#admin.py

    from advanced_imagefield.admin import ImageInline

    class ItemAdmin(admin.ModelAdmin):
        #generic relation
        inlines  = [AdvancedImageInline, ]
from django.db import models

# Create your models here.
class Image(models.Model):
    image_link = models.ImageField(upload_to ='pics/')
    name = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.ForeignKey('Location',null = True,on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null =True,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,link):
        cls.objects.filter(id = id).update(image_link=link)

    @classmethod
    def get_image_by_id(cls,id):
        imge = cls.objects.filter(id =id).all()
        return imge

    @classmethod
    def search_by_cate(cls,cat):
        image = cls.objects.filter(category__category_name__icontains=cat).all()
        return image

    @classmethod
    def search_by_loc(cls,loc):
        image = cls.objects.filter(location__location_name=loc).all()
        return image

class Location(models.Model):
    location_name = models.CharField(max_length = 60)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,new_loc):
        cls.objects.filter(id =id).update(location_name=new_loc)

class Category(models.Model):
    category_name = models.CharField(max_length = 60)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,new_cate):
        cls.objects.filter(id=id).update(category_name=new_cate)

from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name = 'dubai')
        self.location.save()
        self.category = Category(category_name = 'travel')
        self.category.save()
        self.new_image=Image(image_link = 'snaps/img.png',name = 'car',description = 'An exclusive picture of the limited edition range rover velar',location= self.location,category=self.category)
        self.new_image.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_delete_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.new_image.delete_image()
        self.assertTrue(len(images)==0)
    def test_update_method(self):
        self.new_image.save_image()
        self.new_image.update_image(self.new_image.id,'snaps/img1.png')
        image = Image.objects.filter(image_link= 'snaps/img1.png').all()
        self.assertTrue(len(image)==1)
    def test_get_image_by_id(self):
        find_img = self.new_image.get_image_by_id(self.new_image.id)
        img = Image.objects.filter(id = self.new_image.id)
        self.assertTrue(find_img,img)
    def test_search_image_by_category(self):
        find_img = self.new_image.search_by_cate('travel')
        self.assertTrue(len(find_img)==1)
    def test_search_image_by_location(self):
        find_img = self.new_image.search_by_loc('dubai')
        self.assertTrue(len(find_img)==1)
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class LocationTestClass(TestCase):
    def setUp(self):
        self.location=Location(location_name='dubai')
        self.location.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
    def test_save_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)
    def test_delete_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.location.delete_location()
        self.assertTrue(len(location)==0)
    def test_update_method(self):
        new_location_name = 'maldives'
        self.location.update_location(self.location.id,new_location_name)
        new_location = Location.objects.filter(location_name='maldives')
        self.assertTrue(len(new_location)==1)
    def tearDown(self):
        Location.objects.all().delete()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category=Category(category_name='food')
        self.category.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
    def test_save_method(self):
        self.category.save_category()
        category =Category.objects.all()
        self.assertTrue(len(category)>0)
    def test_delete_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.category.delete_category()
        self.assertTrue(len(category)==0)
    def test_update_method(self):
        new_category_name = 'music'
        self.category.update_category(self.category.id,new_category_name)
        new_category = Category.objects.filter(category_name='music')
        self.assertTrue(len(new_category)==1)
    def tearDown(self):
        Category.objects.all().delete()

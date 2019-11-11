from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(location = 'USA')
        
    def tearDown(self):
        Location.objects.all().delete()
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
        
        
    def test_save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)
        
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all().delete()
        self.assertTrue(len(location)==0)
        
    def test _update_location(self):
        _new_location_name ='Kenya'
        
    
    
        
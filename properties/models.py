from django.db import models
import uuid
import locale
from user.models import UserDetails


PROP_STATE = (
    ('deleted','Deleted'),
    ('active','Active'),
    ('suspented','Suspented'),
    ('draft','Draft'),
    ('sold','Sold'),
    ('pending','Pending'),
    ('cancel','Cancel'),
)

PROP_TYPE = (
    ('none','None'),
    ('rent','Rent'),
    ('lease','Lease'),
    ('sale','Sale'),
)

PROP_CATEG = (
    ('none','None'),
    ('apartment','Apartment'),
    ('villas','Villas'),
    ('commercial','Commercial'),
    ('office','Office'),
    ('flat','Flat'),
    ('house','House'),
    ('land','House'),
)

PROP_FRUN = (
    ('semi','Semi'),
    ('fully','Fully'),
    ('not','Not'),
)

PROP_AGE = (
    ('1','0-5'),
    ('2','0-10'),
    ('3','0-15'),
    ('4','0-20'),
    ('20+','20+'),
)


class PropertyImages(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    property = models.ForeignKey('Properties',on_delete=models.CASCADE, null=True, blank=True, related_name='property_img')
    image = models.ImageField(upload_to='properties/images/',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Property Images'
    
    def __str__(self):
        return str(self.uid)


class Properties(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    slug = models.CharField(max_length=250,unique=False,null=True,blank=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True, blank=True)

    heading = models.CharField(max_length=250, unique=False, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField(blank=True, null=True)
      
    address = models.CharField(max_length=250, unique=False, blank=True, null=True)
    zipcode = models.CharField(max_length=20, unique=False, blank=True, null=True)
    place = models.CharField(max_length=100, unique=False, blank=True, null=True)
    city = models.CharField(max_length=100, unique=False, blank=True, null=True)
    state = models.CharField(max_length=100, unique=False, blank=True, null=True)

    building_age = models.CharField(max_length=20, default=1, choices=PROP_AGE, unique=False, blank=True, null=True)
    parking = models.IntegerField(default=0, unique=False, blank=True, null=True)

    rooms = models.CharField(default='1', max_length=20, unique=False, blank=True, null=True)
    bedroom = models.CharField(default='1', max_length=20, null=True, blank=True)
    bathroom = models.CharField(default='1', max_length=20, null=True, blank=True)
    area = models.FloatField(default=0.00, null=True, blank=True)

    type = models.CharField(max_length=100,unique=False,null=True,blank=True,choices=PROP_TYPE,default='none')
    category = models.CharField(max_length=100,unique=False,null=True,blank=True,choices=PROP_CATEG,default='none')
    furnished = models.CharField(max_length=100,unique=False,null=True,blank=True,choices=PROP_FRUN,default='not')
    status = models.CharField(max_length=100,unique=False,null=True,blank=True,choices=PROP_STATE,default='active')

    contact_name = models.CharField(max_length=100, unique=False, blank=True, null=True)
    contact_email = models.EmailField(max_length=100, unique=False, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, unique=False, blank=True, null=True)

    floor_plan = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = str(self.heading).lower().replace(' ','-')
        super(Properties,self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return str(self.heading)

    @property
    def currency(self):
        locale.setlocale(locale.LC_MONETARY, 'en_IN')
        price = locale.currency(self.price, grouping=True)
        return price
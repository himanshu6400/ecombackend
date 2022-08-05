from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.forms import CharField

#Create your models here. 
class UserManager(BaseUserManager): 
    def create_user(self, email, name, tc, mobile, password=None, password2=None):  
        if not email: 
            raise ValueError('Users must have an email address') 
        
        user = self.model( 
            email=self.normalize_email(email),
            name = name, 
            tc = tc, 
            mobile = mobile,       
        ) 

        user.set_password(password) 
        user.save(using=self._db) 
        return user 

    def create_superuser(self, email, name, mobile, tc, password=None): 
        user = self.create_user( 
            email, 
            password=password, 
            name = name, 
            tc = tc,
            mobile = mobile,  
        ) 

        user.is_admin = True 
        user.save(using=self._db) 
        return user 



class User(AbstractBaseUser): 
    email = models.EmailField( verbose_name='Email', max_length=255, unique=True, ) 
    name = models.CharField(max_length=255, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    tc = models.BooleanField() 
    is_active = models.BooleanField(default=True) 
    is_admin = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    objects = UserManager() 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tc', 'name', 'mobile'] 
    
    def __str__(self): 
        return self.email 

    def has_perm(self, perm, obj=None):
        return self.is_admin 
        
    def has_module_perms(self, app_label): 
        return True 
        
    @property 
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    gender = models.CharField(max_length=20)
    locality = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    address = models.TextField(max_length=300)
    pin = models.IntegerField()
    state = models.CharField(max_length=70)
    profile_image = models.ImageField(upload_to='user_profile_image', blank=True)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    pin = models.IntegerField()
    state = models.CharField(max_length=50)

    def __str__ (self):
        return str(self.id)

CHOICES_CATEGORY =(
    ('Cosmetic','Cosmetic'),
    ('Toys','Toys'),
    ('Jeans','Jeans'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CHOICES_CATEGORY)
    product_image = models.ImageField(upload_to='product_image', blank = True)

    def __str__ (self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='cart')
    quantity = models.PositiveIntegerField()

    def __str__ (self):
        return str(self.id)

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderplaced')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orderplaced')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orderplaced')
    quantity = models.PositiveIntegerField(default=1)
    ordered_data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__ (self):
        return str(self.id)


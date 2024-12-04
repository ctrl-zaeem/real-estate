from django.db import models

class Person(models.Model):
    USER_TYPE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    verification_state = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('flat', 'Flat'),
        ('commercial', 'Commercial'),
    ]

    property_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    condition = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPE_CHOICES)
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Listings(models.Model):
    L_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    listing_status = models.BooleanField(default=True)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"Listing {self.L_id} - {self.property.title}"

class Messages(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='received_messages')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    message = models.TextField()
    sent_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.message_id} from {self.sender.name} to {self.receiver.name}"

class Bids(models.Model):
    bid_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_status = models.BooleanField(default=False)
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Bid {self.bid_id} - {self.bid_amount} PKR"

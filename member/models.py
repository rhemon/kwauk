from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    photo = models.ImageField(upload_to="", default="default.jpg")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=100)
    uk_address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    bd_address = models.CharField(max_length=500)
    union = models.CharField(max_length=100)
    # choices=[
    #     ("Union1", "Union1"),
    #     ("Union2", "Union2"),
    #     ("Union3", "Union3"),
    #     ("Union4", "Union4"),
    #     ("Union5", "Union5"),
    #     ("Union6", "Union6"),
    #     ("Union7", "Union7"),
    #     ("Union8", "Union8"),
    #     ("Union9", "Union9"),
    #     ("10 Pourosoba", "10 Pourosoba"),
    
    member_type = models.CharField(max_length=100) 
    # choices=[
    #     ('general', "General"),
    #     ('executive', "Executive"),
    #     ('honarary', "Honarary")
    # ])

class MemberFee(models.Model):
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)
    paydate = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=20)



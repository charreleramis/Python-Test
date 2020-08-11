from django.db import models

# python manage.py makemigrations App
# python manage.py migrate

class Values_Principle(models.Model):
    class Meta:
        db_table = "Values_Principle"
        default_permissions = ('view','add','change','delete')
    
    id = models.AutoField(primary_key=True)
    context_id = models.IntegerField(default=0)
    context = models.TextField()
    context_type = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.id)


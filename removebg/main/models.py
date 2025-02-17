from django.db import models

# Create your models here.

class Remove(models.Model):
    Original_img = models.ImageField(upload_to="E:\Projects\Liftoff\Remove.bg\Remove.bg\removebg\Static\Uploads\Original")
    Final_img = models.ImageField(upload_to="E:\Projects\Liftoff\Remove.bg\Remove.bg\removebg\Static\Uploads\Final",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Image {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
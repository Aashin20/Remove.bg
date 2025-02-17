from django.db import models



class Remove(models.Model):
    Original_img = models.ImageField(upload_to="\Uploads\Original")
    Final_img = models.ImageField(upload_to="\Uploads\Final",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Image {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"